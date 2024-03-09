import json
import logging
from typing import List

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import convert_to_messages, messages_to_dict

logger = logging.getLogger(__name__)

# set logging level to info
logging.basicConfig(level=logging.INFO)


# adjusted from ragas: https://github.com/explodinggradients/ragas/blob/main/src/ragas/metrics/_context_precision.py
# precision = (number of relevant docs) / (number of total retrieved docs)

CONTEXT_PRECISION_CHAT_PROMPT = [
    {
        "role": "system",
        "content": """You are an expert evaluation system for a question answering chatbot.

You are given the following information:
- question
- answer
- context

Your job is to verify if the context was used in arriving at the given answer. Give score as "1" if useful and "0" if not with json output.""",
    },
    {
        "role": "user",
        "content": '''question: "What can you tell me about albert Albert Einstein?"
context: "Albert Einstein (14 March 1879 – 18 April 1955) was a German-born theoretical physicist, widely held to be one of the greatest and most influential scientists of all time. Best known for developing the theory of relativity, he also made important contributions to quantum mechanics, and was thus a central figure in the revolutionary reshaping of the scientific understanding of nature that modern physics accomplished in the first decades of the twentieth century. His mass–energy equivalence formula E = mc2, which arises from relativity theory, has been called \"the world's most famous equation\". He received the 1921 Nobel Prize in Physics \"for his services to theoretical physics, and especially for his discovery of the law of the photoelectric effect\", a pivotal step in the development of quantum theory. His work is also known for its influence on the philosophy of science. In a 1999 poll of 130 leading physicists worldwide by the British journal Physics World, Einstein was ranked the greatest physicist of all time. His intellectual achievements and originality have made Einstein synonymous with genius."
answer: "Albert Einstein born in 14 March 1879 was German-born theoretical physicist, widely held to be one of the greatest and most influential scientists of all time. He received the 1921 Nobel Prize in Physics for his services to theoretical physics. He published 4 papers in 1905. Einstein moved to Switzerland in 1895"''',
    },
    {
        "role": "assistant",
        "content": """{"verification": {"reason": "The provided context was indeed useful in arriving at the given answer. The context includes key information about Albert Einstein's life and contributions, which are reflected in the answer.", "score": "1"}}""",
    },
    {
        "role": "user",
        "content": '''question: "who won 2020 icc world cup?"
context: "The 2022 ICC Men's T20 World Cup, held from October 16 to November 13, 2022, in Australia, was the eighth edition of the tournament. Originally scheduled for 2020, it was postponed due to the COVID-19 pandemic. England emerged victorious, defeating Pakistan by five wickets in the final to clinch their second ICC Men's T20 World Cup title."
answer: "England"''',
    },
    {
        "role": "assistant",
        "content": """{"verification": {"reason": "the context was useful in clarifying the situation regarding the 2020 ICC World Cup and indicating that England was the winner of the tournament that was intended to be held in 2020 but actually took place in 2022.", "score": "1"}}""",
    },
    {
        "role": "user",
        "content": '''question: "What is the tallest mountain in the world?"
context: "The Andes is the longest continental mountain range in the world, located in South America. It stretches across seven countries and features many of the highest peaks in the Western Hemisphere. The range is known for its diverse ecosystems, including the high-altitude Andean Plateau and the Amazon rainforest."
answer: "Mount Everest."''',
    },
    {
        "role": "assistant",
        "content": """{"verification": {"reason": "the provided context discusses the Andes mountain range, which, while impressive, does not include Mount Everest or directly relate to the question about the world's tallest mountain.", "score": "0"}}""",
    },
]


class ContextPrecision:
    """From: https://docs.ragas.io/en/latest/concepts/metrics/context_precision.html
    Context Precision is a metric that evaluates whether all of the ground-truth relevant items present in the contexts are ranked higher or not. Ideally all the relevant chunks must appear at the top ranks. This metric is computed using the question and the contexts, with values ranging between 0 and 1, where higher scores indicate better precision.
    Example:
    >>> from easyrag.metrics import ContextPrecision
    >>> context_precision = ContextPrecision(llm=llm,verbose=True)
    >>>
    >>> sample =  {
          "question": "What is the capital of France?",
          "ground_truth": "Paris",
          "answer": "Paris",
          "contexts": ["Paris is the capital of France." , "Charlie likes to eat chocolate.", "1776 Paris was the center of a war."],
        }
    >>> context_precision.compute(quesiton=fake["question"], answer=fake["answer"], contexts=fake["contexts"])
    >>> 0.66666
    """

    name = "context_precision"
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

    def get_prompt(self, question: str, context: str, answer: str):
        # generate prompt and call llm
        messages = CONTEXT_PRECISION_CHAT_PROMPT.copy()
        messages.append(
            {
                "role": "user",
                "content": f'''question: "{question}"\ncontext: "{context}"\nanswer: "{answer}"''',
            }
        )
        prompt = convert_to_messages(messages)
        return prompt

    def get_instruct_prompt(self, question: str, context: str, answer: str):
        prompt = self.get_prompt(question, context, answer)
        messages = messages_to_dict(prompt)
        string_prompt = ""
        for m in messages:
            string_prompt += m["data"]["content"] + "\n"
        return string_prompt

    def compute(
        self,
        question: str = None,
        context: List[str] = None,
        ground_truth: str = None,
        **kwargs,
    ) -> float:
        """
        Given a context and an answer, analyze each sentence in the answer and classify if the sentence can be attributed to the given context or not. Use only "Yes" (1) or "No" (0) as a binary classification. Output json with reason.
        """
        precision = []
        # iterate over each context
        for c in context:
            if self.use_instruct_prompt:
                prompt = self.get_instruct_prompt(question, c, ground_truth)
            else:
                prompt = self.get_prompt(question, c, ground_truth)
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
                continue
            # get verification
            verification = response.get("verification", None)
            if verification is None:
                logger.error(
                    f"Response from LLM does not contain 'verification' key: {response}, returning None"
                )
                continue
            verdict = int(float((verification.get("score").strip())))
            precision.append(verdict)
            # calculate the recall
        recall = sum(precision) / len(precision)
        return float(recall)

    async def acompute(
        self,
        question: str = None,
        context: List[str] = None,
        ground_truth: str = None,
        **kwargs,
    ) -> float:
        """
        Asynchronous version of compute
        """
        precision = []
        # iterate over each context
        for c in context:
            if self.use_instruct_prompt:
                prompt = self.get_instruct_prompt(question, c, ground_truth)
            else:
                prompt = self.get_prompt(question, c, ground_truth)
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
                continue
            # get verification
            verification = response.get("verification", None)
            if verification is None:
                logger.error(
                    f"Response from LLM does not contain 'verification' key: {response}, returning None"
                )
                continue
            verdict = int(float((verification.get("score").strip())))
            precision.append(verdict)
            # calculate the recall
        recall = sum(precision) / len(precision)
        return float(recall)
