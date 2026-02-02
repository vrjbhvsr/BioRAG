from models.Llama import model
from prompts.query_rewrite_prompt import QueryRewritePrompt
from config.logging import log
from config.exception import CustomException
import sys
from langchain_core.runnables.base import RunnableSequence
from Parsers.output_parser import query_parser
from constants import *
from langchain_core.output_parsers import PydanticOutputParser

logger = log()
log = logger.get_logger(__name__)

class QueryRewriteChain:
    """
    A chain for query rewriting tasks.
    """
    def __init__(self, model):
        '''self.model_pipe = model().load()
        self.model = self.model_pipe.bind(skip_prompt = QUERY_SKIP_PROMPT,
                                          pipeline_kwargs={
                                        "do_sample": QUERY_DO_SAMPLE,
                                        "temperature": QUERY_TEMPERATURE,
                                        "max_new_tokens": QUERY_MAX_NEW_TOKENS,
                                        "repetition_penalty": QUERY_REPETITION_PENALTY,
                                        "top_p": QUERY_TOP_P,
                                        #"dtype": QUERY_DTYPE,
                                        #"device_map": QUERY_DEVICE_MAP,
                                                })'''
        self.model = model
        self.prompt = QueryRewritePrompt().prompt()
        self.parser = PydanticOutputParser(pydantic_object=query_parser)

    def chain(self) -> RunnableSequence:
        """
        Initialize the query rewrite chain.
        Returns:
            RunnableSequence: The initialized query rewrite chain.
        """
        try:
            log.info("Initializing query rewrite chain...")
            query_rewrite_chain = self.prompt | self.model | self.parser
            log.info("Query rewrite chain initialized successfully.")
            return query_rewrite_chain
        except Exception as e:
            log.error("Error initializing query rewrite chain.")
            raise CustomException(e, sys)
        