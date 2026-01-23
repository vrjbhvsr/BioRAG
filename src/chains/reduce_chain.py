from models.Llama import model
from constants import *
from langchain_core.runnables import RunnableSequence, RunnableLambda
from Parsers.output_parser import ReduceParser
from prompts.reduce_prompt import reduce_prompt
from Normalisers.reduce_normaliser import reduce_normaliser
from langchain_core.output_parsers import PydanticOutputParser
from config.logging import log
from config.exception import CustomException
import sys

logger = log()
log = logger.get_logger(__name__)

class reduce_chain:
    """
    A chain for reducing tasks using a language model.
    """
    def __init__(self):
        self.model_pipe = model().load()
        self.model = self.model_pipe.bind(skip_prompt = SKIP_PROMPT,
                                          pipeline_kwargs={
                                              "do_sample": MAP_DO_SAMPLE,
                                            "temperature": MAP_TEMPERATURE,
                                            "max_new_tokens": MAP_MAX_NEW_TOKENS,
                                            "repetition_penalty": MAP_REPETITION_PENALTY,
                                            "top_p": MAP_TOP_P,})
        self.prompt = reduce_prompt().prompt()
        self.normaliser = RunnableLambda(reduce_normaliser)
        self.parser = PydanticOutputParser(pydantic_object=ReduceParser)

    def chain(self) -> RunnableSequence:
        """
        Initialize the reduce chain.
        Returns:
            RunnableSequence: The initialized reduce chain.
        """
        try:
            log.info("Initializing reduce chain...")
            reduce_chain = self.prompt | self.model | self.normaliser | self.parser
            log.info("Reduce chain initialized successfully.")
            return reduce_chain
        except Exception as e:
            log.error("Error initializing reduce chain.")
            raise CustomException(e, sys)