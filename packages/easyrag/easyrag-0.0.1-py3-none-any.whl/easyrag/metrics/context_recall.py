import json
import logging
from typing import List

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import convert_to_messages, messages_to_dict

logger = logging.getLogger(__name__)

# set logging level to info
logging.basicConfig(level=logging.INFO)


# adjusted from ragas: https://github.com/explodinggradients/ragas/blob/317a2d88c2917fecc24dd4804cb7e12d79a6bac5/src/ragas/metrics/_context_recall.py#L20
CONTEXT_RECALL_CHAT_PROMPT = [
    {
        "role": "system",
        "content": """You are an expert evaluation system for a question answering chatbot.

You are given the following information:
- context
- answer

Your job is to analyze each sentence in the answer and classify if the sentence can be attributed to the given context or not. Use only 'Yes' (1) or 'No' (0) as a binary classification. Output json with reason. Output in only valid JSON format.""",
    },
    {
        "role": "user",
        "content": '''context: "Albert Einstein (14 March 1879 – 18 April 1955) was a German-born theoretical physicist, widely held to be one of the greatest and most influential scientists of all time. Best known for developing the theory of relativity, he also made important contributions to quantum mechanics, and was thus a central figure in the revolutionary reshaping of the scientific understanding of nature that modern physics accomplished in the first decades of the twentieth century. His mass–energy equivalence formula E = mc2, which arises from relativity theory, has been called 'the world's most famous equation'. He received the 1921 Nobel Prize in Physics 'for his services to theoretical physics, and especially for his discovery of the law of the photoelectric effect', a pivotal step in the development of quantum theory. His work is also known for its influence on the philosophy of science. In a 1999 poll of 130 leading physicists worldwide by the British journal Physics World, Einstein was ranked the greatest physicist of all time. His intellectual achievements and originality have made Einstein synonymous with genius."
answer: "Albert Einstein born in 14 March 1879 was German-born theoretical physicist, widely held to be one of the greatest and most influential scientists of all time. He received the 1921 Nobel Prize in Physics for his services to theoretical physics. He published 4 papers in 1905. Einstein moved to Switzerland in 1895"''',
    },
    {
        "role": "assistant",
        "content": """{"classification": [{"sentence_1": "Albert Einstein born in 14 March 1879 was German-born theoretical physicist, widely held to be one of the greatest and most influential scientists of all time.", "reason": "The date of birth of Einstein is mentioned clearly in the context.", "Attributed": "1"}, {"sentence_2": "He received the 1921 Nobel Prize in Physics for his services to theoretical physics.", "reason": "The exact sentence is present in the given context.", "Attributed": "1"}, {"sentence_3": "He published 4 papers in 1905.", "reason": "There is no mention about papers he wrote in the given context.", "Attributed": "0"}, {"sentence_4": "Einstein moved to Switzerland in 1895.", "reason": "There is no supporting evidence for this in the given context.", "Attributed": "0"}]}""",
    },
    {
        "role": "user",
        "content": '''context: "The 2022 ICC Men's T20 World Cup, held from October 16 to November 13, 2022, in Australia, was the eighth edition of the tournament. Originally scheduled for 2020, it was postponed due to the COVID-19 pandemic. England emerged victorious, defeating Pakistan by five wickets in the final to clinch their second ICC Men's T20 World Cup title."
answer: "England won the 2022 ICC Men's T20 World Cup."''',
    },
    {
        "role": "assistant",
        "content": """{"classification": [{"sentence_1": "England won the 2022 ICC Men's T20 World Cup.", "reason": "From context it is clear that England defeated Pakistan to win the World Cup.", "Attributed": "1"}]}""",
    },
]


class ContextRecall:
    """From: https://docs.ragas.io/en/latest/concepts/metrics/context_recall.html
    Context recall measures the extent to which the retrieved context aligns with the annotated answer, treated as the ground truth. It is computed based on the ground truth and the retrieved context, and the values range between 0 and 1, with higher values indicating better performance.
    Example:
    >>> from easyrag.metrics import ContextRecall
    >>> context_recall = ContextRecall(llm=llm,verbose=True)
    >>>
    >>> sample =  {
          "question": "What is the capital of France?",
          "ground_truth": "Paris",
          "answer": "Paris",
          "contexts": ["Paris is the capital of France." , "Charlie likes to eat chocolate.", "1776 Paris was the center of a war."],
        }
    >>> context_recall.compute(contexts=sample["contexts"], ground_truth=sample["ground_truth"])
    >>> 0.3333333333333333
    """

    name = "context_recall"
    llm: BaseChatModel
    verbose: bool = False
    use_instruct_prompt: bool = True

    def __init__(
        self,
        llm: BaseChatModel,
        verbose: bool = False,
        use_instruct_prompt: bool = True,
    ):
        self.llm = llm
        self.verbose = verbose
        self.use_instruct_prompt = use_instruct_prompt

    def get_prompt(self, context: str, ground_truth: str):
        # generate prompt and call llm
        messages = CONTEXT_RECALL_CHAT_PROMPT.copy()
        messages.append(
            {
                "role": "user",
                "content": f'''context: "{context}"\nanswer: "{ground_truth}"''',
            }
        )
        prompt = convert_to_messages(messages)
        return prompt

    def get_instruct_prompt(self, context: str, ground_truth: str):
        prompt = self.get_prompt(context, ground_truth)
        messages = messages_to_dict(prompt)
        string_prompt = ""
        for m in messages:
            string_prompt += m["data"]["content"] + "\n"
        return string_prompt

    def compute(
        self, context: List[str] = None, ground_truth: str = None, **kwargs
    ) -> float:
        """
        Given a context and an answer, analyze each sentence in the answer and classify if the sentence can be attributed to the given context or not. Use only "Yes" (1) or "No" (0) as a binary classification. Output json with reason.
        Output in only valid JSON format.
        """
        # generate prompt and call llm
        context = "\n".join(context)
        if self.use_instruct_prompt:
            prompt = self.get_instruct_prompt(context, ground_truth)
        else:
            prompt = self.get_prompt(context, ground_truth)
        if self.verbose:
            logger.info(f"LLM prompt: {prompt}")

        response = self.llm.invoke(prompt)
        # try to parse the response
        try:
            response = json.loads(response.content)
            if self.verbose:
                logger.info(f"LLM response parsed: {response}")
        except json.JSONDecodeError:
            logger.error(
                f"Response from LLM is not valid JSON: {response.content}, returning None"
            )
            return None
        # get attribution
        classification = response.get("classification", None)
        if classification is None:
            logger.error(
                f"Response from LLM does not contain 'classification' key: {response}, returning None"
            )
            return None
        attributions = []
        for c in classification:
            attribution = int(c.get("Attributed").strip())
            attributions.append(attribution)
        # calculate the recall
        recall = sum(attributions) / len(attributions)
        return float(recall)

    async def acompute(
        self, context: List[str] = None, ground_truth: str = None, **kwargs
    ) -> float:
        """
        Asynchronous version of compute
        """
        # generate prompt and call llm
        context = "\n".join(context)
        if self.use_instruct_prompt:
            prompt = self.get_instruct_prompt(context, ground_truth)
        else:
            prompt = self.get_prompt(context, ground_truth)
        if self.verbose:
            logger.info(f"LLM prompt: {prompt}")

        response = await self.llm.ainvoke(prompt)
        # try to parse the response
        try:
            response = json.loads(response.content)
            if self.verbose:
                logger.info(f"LLM response parsed: {response}")
        except json.JSONDecodeError:
            logger.error(
                f"Response from LLM is not valid JSON: {response.content}, returning None"
            )
            return None
        # get attribution
        classification = response.get("classification", None)
        if classification is None:
            logger.error(
                f"Response from LLM does not contain 'classification' key: {response}, returning None"
            )
            return None
        attributions = []
        for c in classification:
            attribution = int(c.get("Attributed").strip())
            attributions.append(attribution)
        # calculate the recall
        recall = sum(attributions) / len(attributions)
        return float(recall)
