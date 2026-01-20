from langchain_core.prompts import ChatPromptTemplate
from prompts.base import BasePrompt
from constants import *
from config.logging import log
from config.exception import CustomException
import sys  
from Parsers.output_parser import query_parser
from langchain_core.output_parsers import PydanticOutputParser

logger = log()
log = logger.get_logger(__name__)

class QueryRewritePrompt(BasePrompt):
    """
    A class to create a prompt template for query rewriting.
    """
    def __init__(self):
        
        self.system_msg = QUERY_REWRITE_SYSTEM_MSG
        self.parser = PydanticOutputParser(pydantic_object=query_parser)
    def prompt(self) -> ChatPromptTemplate:
        """
        Get the ChatPromptTemplate instance.

        Returns:
            ChatPromptTemplate: The prompt template instance.
        """

        try:
            log.info("Creating query rewrite prompt template...")
            query_prompt = ChatPromptTemplate.from_messages(
                                                            [
                                                                ("system", self.system_msg),
                                                            ]
                                                        ).partial(format_instructions=self.parser.get_format_instructions())
            log.info("Query rewrite prompt template created successfully.")
            return query_prompt
        except Exception as e:
            log.error("Error creating query rewrite prompt template.")
            raise CustomException(e, sys)