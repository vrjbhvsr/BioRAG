from src.models.Llama import model
from prompts.table_summariser_prompt import table_summariser_prompt
from config.logging import log
from config.exception import CustomException
import sys
from langchain_core.runnables.base import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from constants import *

logger = log()
log = logger.get_logger(__name__)

class table_summary_chain:
    """
    A chain for table summarization tasks.
    """
    def __init__(self):
        
            self.model_pipe = model().load()
            self.model = self.model_pipe.bind(skip_prompt = True,pipeline_kwargs={
                                            "do_sample": DO_SAMPLE,
                                            "temperature": TEMPERATURE,
                                            "max_new_tokens": MAX_NEW_TOKENS,
                                            "repetition_penalty": REPETITION_PENALTY,
                                            
                                                    })
            self.prompt = table_summariser_prompt().prompt()
            self.parser = StrOutputParser()

    def chain(self) -> RunnableSequence:
        """
        Initialize the table summary chain.
        Returns:
            RunnableSequence: The initialized table summary chain.
        """
        try:
            log.info("Initializing table summary chain...")
            table_summary_chain = self.prompt | self.model | self.parser
            log.info("Table summary chain initialized successfully.")
            return table_summary_chain
        except Exception as e:
            log.error("Error initializing table summary chain.")
            raise CustomException(e, sys)