from models.Llama import model
from prompts.map_prompt import map_prompt
from config.logging import log
from config.exception import CustomException
import sys
from langchain_core.runnables.base import RunnableSequence, RunnableLambda
from Normalisers.map_normaliser import map_normaliser
from constants import *
from Parsers.output_parser import Map_parser
from langchain_core.output_parsers import PydanticOutputParser


logger = log()
log = logger.get_logger(__name__)

class map_chain:
    """
    A chain for mapping tasks.
    """
    def __init__(self):
        
            self.model_pipe = model().load()
            self.model = self.model_pipe.bind(skip_prompt = True,
                                            pipeline_kwargs={
                                            "do_sample": MAP_DO_SAMPLE,
                                            "temperature": MAP_TEMPERATURE,
                                            "max_new_tokens": MAP_MAX_NEW_TOKENS,
                                            "repetition_penalty": MAP_REPETITION_PENALTY,
                                            "top_p": MAP_TOP_P,

                                                    })
            self.prompt = map_prompt().prompt()
            self.normaliser = RunnableLambda(map_normaliser)
            self.parser = PydanticOutputParser(pydantic_object=Map_parser)

    def chain(self) -> RunnableSequence:
        """
        Initialize the map chain.
        Returns:
            RunnableSequence: The initialized map chain.
        """
        try:
            log.info("Initializing map chain...")
            map_chain = self.prompt | self.model | self.normaliser | self.parser
            log.info("Map chain initialized successfully.")
            return map_chain
        except Exception as e:
            log.error("Error initializing map chain.")
            raise CustomException(e, sys)
