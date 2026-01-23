from langchain_core.prompts import ChatPromptTemplate
from config.logging import log
from config.exception import CustomException
import sys
from prompts.base import BasePrompt
from langchain_core.output_parsers import PydanticOutputParser
from Parsers.output_parser import ReduceParser
from constants import *
from langchain_core.runnables import RunnableLambda
from Normalisers.reduce_normaliser import reduce_normaliser

logger = log()
log = logger.get_logger(__name__)

class reduce_prompt(BasePrompt):
    """
    A prompt template for reducing tasks.
    """
    def __init__(self):
        self.system_prompt = REDUCE_PROMPT
        self.parser = PydanticOutputParser(pydantic_object=ReduceParser)
        
    def prompt(self) -> ChatPromptTemplate:
        """
        Create a chat prompt template for reducing tasks.

        Returns:
            ChatPromptTemplate: The created chat prompt template.
        """
        try:
            log.info("Creating reduce prompt template...")
            prompt = ChatPromptTemplate.from_messages([
                ("system", self.system_prompt)
            ]).partial(format_instructions=self.parser.get_format_instructions())
            log.info("Reduce prompt template created successfully.")
            return prompt
        except Exception as e:
            log.error("Error creating reduce prompt template.")
            raise CustomException(e, sys)