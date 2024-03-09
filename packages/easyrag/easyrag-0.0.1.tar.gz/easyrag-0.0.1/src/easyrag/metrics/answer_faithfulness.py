import json
import logging
from typing import List, Union

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import convert_to_messages, messages_to_dict

logger = logging.getLogger(__name__)

# set logging level to info
logging.basicConfig(level=logging.INFO)


# adjusted from llamaindex: https://docs.llamaindex.ai/en/latest/examples/low_level/evaluation.html#building-a-faithfulness-evaluator
# and ragas: https://github.com/explodinggradients/ragas/blob/main/src/ragas/metrics/_faithfulness.py
ANSWER_FAITHFULNESS_CHAT_PROMPT = [
    {
        "role": "system",
        "content": """You are an expert evaluation system for a question answering chatbot.

You are given the following information:
- context, including information
- generated answer

Your job is to classify if the answer is supported by the context. Use only 'Faithfull' (1) if the any of the contexts supports the answer, even if most of the context is unrelated. Use 'Unfaithfull' (0) if the context doesn't provide any support for the answer. Output json with reason. Output in only valid JSON format.
""",
    },
    {
        "role": "user",
        "content": '''context: "John is a student at XYZ University. He is pursuing a degree in Computer Science. He is enrolled in several courses this semester, including Data Structures, Algorithms, and Database Management. John is a diligent student and spends a significant amount of time studying and completing assignments. He often stays late in the library to work on his projects."
answer: "John is majoring in Biology."''',
    },
    {
        "role": "assistant",
        "content": """{"result": {"reason": "John's major is explicitly mentioned as Computer Science. There is no information suggesting he is majoring in Biology.", "score": "0"}}""",
    },
    {
        "role": "user",
        "content": '''context: "Uruguay's capital, Montevideo, was founded by the Spanish in the early 18th century as a military stronghold; its natural harbor soon developed into a commercial center competing with Argentina's capital, Buenos Aires. Uruguay's early 19th century history was shaped by ongoing conflicts between the British, Spanish, Portuguese, and colonial forces for dominance in the Argentina-Brazil-Uruguay region. /ref> In 1806 and 1807, the British army attempted to seize Buenos Aires as part of their war with Spain. As a result, at the beginning of 1807, Montevideo was occupied by a 10,000-strong British force who held it until the middle of the year when they left to attack Buenos Aires."
answer: "The early 19th-century geopolitical landscape of the Argentina-Brazil-Uruguay region was marked by intense rivalry and conflict involving major colonial and European powers, namely the British, Spanish, and Portuguese. "''',
    },
    {
        "role": "assistant",
        "content": """{"result": {"reason": "The context discusses the conflicts and rivalries in the Argentina-Brazil-Uruguay region during the early 19th century, involving the British, Spanish, Portuguese, and colonial forces, which directly supports the answer.","score": "1"}}""",
    },
    {
        "role": "user",
        "content": '''context: "It is vital for all known forms of life, despite not providing food energy or organic micronutrients. Its chemical formula, H2O, indicates that each of its molecules contains one oxygen and two hydrogen atoms, connected by covalent bonds. The hydrogen atoms are attached to the oxygen atom at an angle of 104.45°.[20] "Water" is also the name of the liquid state of H2O at standard temperature and pressure.\n\nThe boiling point of water is 212 degrees Fahrenheit or 100 degrees Celsius at sea level. That means in most places this is the temperatures of boiled water. However, as you rise above sea level water will boil at a lower temperature.\n\nCan water boil at 200 degrees?\nThe temperature at which water boils varies based on elevation."
answer: "The boiling point of water is 100 degrees Celsius (212 degrees Fahrenheit) at sea level, but it can change with altitude."''',
    },
    {
        "role": "assistant",
        "content": """{"result": {"reason": "The context explains that water boils at 212 degrees Fahrenheit (100 degrees Celsius) at sea level and also mentions that the boiling point decreases with elevation, directly supporting the answer.", "score": "1"}}""",
    },
    {
        "role": "user",
        "content": '''context: "Photosynthesis is the process by which plants, algae, and some bacteria convert light energy from the sun into chemical energy in the form of glucose. This process occurs in specialized structures called chloroplasts, which are found in the leaves of plants and other photosynthetic organisms."
answer: "Apple's gross margin rate in 2021 is approximately 35.91%. Note that this is an estimation and not an official figure provided by Apple. The actual gross margin rate for 2021 may vary depending on the company's actual financial results."''',
    },
    {
        "role": "assistant",
        "content": """{"result": {"reason": "The context provides information about the process of photosynthesis, which is unrelated to the financial metrics of a technology company like Apple.", "score": "0"}}""",
    },
]


class AnswerFaithfulness:
    """From: https://docs.ragas.io/en/latest/concepts/metrics/faithfulness.html & https://docs.llamaindex.ai/en/latest/examples/low_level/evaluation.html#building-a-faithfulness-evaluator
    The Answer Faithfulness is metric evaluates whether the response is faithful to any of the retrieved contexts. It is computed using the retrieved contexts, and the generated answer, and returns a score with 0 NOT FAITHFUL and 1 FAITHFUL.
    Example:
    >>> from easyrag.metrics import AnswerFaithfulness
    >>> answer_faithfulness = AnswerFaithfulness(llm=llm,verbose=True)
    >>>
    >>> sample =  {
          "question": "What is the capital of France?",
          "ground_truth": "Paris",
          "answer": "Paris",
          "contexts": ["Paris is the capital of France." , "Charlie likes to eat chocolate.", "1776 Paris was the center of a war."],
        }
    >>> answer_faithfulness.compute(context=sample["contexts"], answer=sample["answer"])
    >>> 1.0
    """

    name = "answer_faithfulness"
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

    def get_prompt(self, context: str, answer: str):
        # generate prompt and call llm
        messages = ANSWER_FAITHFULNESS_CHAT_PROMPT.copy()
        messages.append(
            {
                "role": "user",
                "content": f'''context: "{context}"\nanswer: "{answer}"''',
            }
        )
        prompt = convert_to_messages(messages)
        return prompt

    def get_instruct_prompt(self, context: str, answer: str):
        prompt = self.get_prompt(context, answer)
        messages = messages_to_dict(prompt)
        string_prompt = ""
        for m in messages:
            string_prompt += m["data"]["content"] + "\n"
        return string_prompt

    def compute(
        self, context: Union[List[str], str] = None, answer: str = None, **kwargs
    ) -> float:
        """
        Compute the faithfulness of the answer given the context
        """
        context = context if isinstance(context, str) else "\n".join(context)
        if self.use_instruct_prompt:
            prompt = self.get_instruct_prompt(context, answer)
        else:
            prompt = self.get_prompt(context, answer)
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
        faithfulness = response.get("result", None)
        if faithfulness is None:
            logger.error(
                f"Response from LLM does not contain 'faithfulness' key: {response}, returning None"
            )
            return None
        return float(faithfulness.get("score").strip())

    async def acompute(
        self, context: Union[List[str], str] = None, answer: str = None, **kwargs
    ) -> float:
        """
        Compute the faithfulness of the answer given the context
        """
        context = context if isinstance(context, str) else "\n".join(context)
        if self.use_instruct_prompt:
            prompt = self.get_instruct_prompt(context, answer)
        else:
            prompt = self.get_prompt(context, answer)
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
        # get verification
        faithfulness = response.get("result", None)
        if faithfulness is None:
            logger.error(
                f"Response from LLM does not contain 'faithfulness' key: {response}, returning None"
            )
            return None
        return float(faithfulness.get("score").strip())
