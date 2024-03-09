import json
import logging

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import convert_to_messages, messages_to_dict

logger = logging.getLogger(__name__)

# set logging level to info
logging.basicConfig(level=logging.INFO)


# adjusted from llamaindex: https://docs.llamaindex.ai/en/latest/examples/low_level/evaluation.html#building-a-correctness-evaluator
# and ragas: https://github.com/explodinggradients/ragas/blob/main/src/ragas/metrics/_answer_correctness.py
ANSWER_CORRECTNESS_CHAT_PROMPT = [
    {
        "role": "system",
        "content": """You are an expert evaluation system for a question answering chatbot.

You are given the following information:
- question
- ground_truth
- answer

Your job is to score the correctness of the answer. Use only 'Correct' (1) if ground_trurh and answer are correct in terms of content. Use 'Incorrect' (0) if they are different, ground_truth is the correct answer. Output json with reason. Output in only valid JSON format.
""",
    },
    {
        "role": "user",
        "content": '''question: "What powers the sun and what is its primary function?"
ground_truth: "The sun is actually powered by nuclear fusion, not fission. In its core, hydrogen atoms fuse to form helium, releasing a tremendous amount of energy. This energy is what lights up the sun and provides heat and light, essential for life on Earth. The sun's light also plays a critical role in Earth's climate system and helps to drive the weather and ocean currents."
answer: "The sun is powered by nuclear fission, similar to nuclear reactors on Earth, and its primary function is to provide light to the solar system."''',
    },
    {
        "role": "assistant",
        "content": """{"result": {"reason": "The answer provided incorrectly states the process that powers the sun as nuclear fission, while the correct process is nuclear fusion, as mentioned in the ground truth. Nuclear fusion, not fission, is the reaction in which hydrogen atoms fuse to form helium in the sun's core, releasing a significant amount of energy. This energy is indeed crucial for providing light and heat to the Earth, which are essential for life and for driving Earth's climate and weather patterns.", "score": "0"}}""",
    },
    {
        "role": "user",
        "content": '''question: "who won 2020 icc world cup?"
ground_truth: "Based on the context you've provided, there seems to be a misunderstanding in your question. The ICC Men's T20 World Cup that was originally scheduled for 2020 was postponed to 2022 due to the COVID-19 pandemic. England won the 2022 ICC Men's T20 World Cup, defeating Pakistan by five wickets in the final. This victory marked England's second ICC Men's T20 World Cup title. Therefore, there was no ICC World Cup held in 2020 due to the postponement."
answer: "There was no ICC in 2020. The 2020 ICC was post poned which was won by England"''',
    },
    {
        "role": "assistant",
        "content": """{"result": {"reason": "There was no ICC in 2020. The 2020 ICC was post poned which was won by England", "score": "1"}}""",
    },
    {
        "role": "user",
        "content": '''question: "What is the boiling point of water?"
ground_truth: "The boiling point of water is 100 degrees Celsius (212 degrees Fahrenheit) at sea level, but it can change with altitude."
answer: "The boiling point of water is 100 degrees Celsius at sea level."''',
    },
    {
        "role": "assistant",
        "content": """{"result": {"reason": "The answer provided is correct based on the question and the context given. The question asks for the boiling point of water, and the answer correctly states that it is 100 degrees Celsius at sea level, which is in agreement with the context provided. The answer specifically addresses the condition "at sea level," which is crucial because, as noted in the context, the boiling point of water can change with altitude.", "score": "1"}}""",
    },
    {
        "role": "user",
        "content": '''question: "What is the gross margin rate of apple in 2020?"
ground_truth: "In 2020, Apple had a gross margin percentage of 38.2%."
answer: "Apple's gross margin rate in 2021 is approximately 35.91%. Note that this is an estimation and not an official figure provided by Apple. The actual gross margin rate for 2021 may vary depending on the company's actual financial results."''',
    },
    {
        "role": "assistant",
        "content": """{"result": {"reason": "The provided answer does not accurately address the question asked. The question specifically inquires about Apple's gross margin rate in 2020, but the answer discusses the estimated gross margin rate for 2021. There is a discrepancy in the year of interest, making the response irrelevant to the question. The answer fails to provide the requested information for the correct year, 2020, and instead offers an estimation for a different year without acknowledging or correcting the discrepancy. Given this, the answer is incorrect as it does not match the year specified in the question nor does it align with the provided ground truth.", "score": "0"}}""",
    },
]


class AnswerCorrectness:
    """From: https://docs.ragas.io/en/latest/concepts/metrics/context_precision.html
    The assessment of Answer Correctness involves gauging the accuracy of the generated answer when compared to the ground truth. This evaluation relies on the ground truth and the answer, with scores ranging from 0 to 1. A higher score indicates a closer alignment between the generated answer and the ground truth, signifying better correctness.
    Example:
    >>> from easyrag.metrics import AnswerCorrectness
    >>> answer_correctness = AnswerCorrectness(llm=llm,verbose=True)
    >>>
    >>> sample =  {
          "question": "What is the capital of France?",
          "ground_truth": "Paris",
          "answer": "Paris",
          "contexts": ["Paris is the capital of France." , "Charlie likes to eat chocolate.", "1776 Paris was the center of a war."],
        }
    >>> answer_correctness.compute(contexts=sample["contexts"], ground_truth=sample["ground_truth"])
    >>> 1.0
    """

    name = "answer_correctness"
    llm: BaseChatModel

    def __init__(
        self,
        llm: BaseChatModel,
        verbose: bool = False,
        use_instruct_prompt: bool = True,
    ):
        self.llm = llm
        self.verbose = verbose
        self.use_instruct_prompt = use_instruct_prompt

    def get_prompt(self, question: str, ground_truth: str, answer: str):
        # generate prompt and call llm
        messages = ANSWER_CORRECTNESS_CHAT_PROMPT.copy()
        messages.append(
            {
                "role": "user",
                "content": f'''question: "{question}"\nground_truth: "{ground_truth}"\nanswer: "{answer}"''',
            }
        )
        prompt = convert_to_messages(messages)
        return prompt

    def get_instruct_prompt(self, question: str, ground_truth: str, answer: str):
        prompt = self.get_prompt(question, ground_truth, answer)
        messages = messages_to_dict(prompt)
        string_prompt = ""
        for m in messages:
            string_prompt += m["data"]["content"] + "\n"
        return string_prompt

    def compute(
        self,
        question: str = None,
        ground_truth: str = None,
        answer: str = None,
        **kwargs,
    ) -> str:
        """
        Given a context and an answer, analyze each sentence in the answer and classify if the sentence can be attributed to the given context or not. Use only "Yes" (1) or "No" (0) as a binary classification. Output json with reason.
        """
        if self.use_instruct_prompt:
            prompt = self.get_instruct_prompt(question, ground_truth, answer)
        else:
            prompt = self.get_prompt(question, ground_truth, answer)
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
        # get verification
        verification = response.get("result", None)
        if verification is None:
            logger.error(
                f"Response from LLM does not contain 'verification' key: {response}, returning None"
            )
            return None
        return float(verification.get("score").strip())

    async def acompute(
        self,
        question: str = None,
        ground_truth: str = None,
        answer: str = None,
        **kwargs,
    ) -> float:
        """
        Asynchronous version of the compute method to evaluate answer correctness.
        """
        if self.use_instruct_prompt:
            prompt = self.get_instruct_prompt(question, ground_truth, answer)
        else:
            prompt = self.get_prompt(question, ground_truth, answer)

        if self.verbose:
            logger.info(f"LLM async prompt: {prompt}")
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
        # get verification
        verification = response.get("result", None)
        if verification is None:
            logger.error(
                f"Response from LLM does not contain 'verification' key: {response}, returning None"
            )
            return None
        return float(verification.get("score").strip())
