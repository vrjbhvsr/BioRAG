from constants import *
from langchain_core.prompt import ChatPromptTemplate
from config.logging import log
from config.exception import CustomException
import sys
from prompts.base import BasePrompt
from Parsers import Map_parser
from langchain_core.output_parsers import PydanticOutputParser

logger = log()
log = logger.get_logger(__name__)

class map_prompt(BasePrompt):
    """
    A prompt template for mapping tasks.
    """
    def __init__(self):
        self.system_prompt = MAP_PROMPT
        self.parser = PydanticOutputParser(pydantic_object=Map_parser)
    def prompt(self) -> ChatPromptTemplate:
        """
        Create a chat prompt template for mapping tasks.

        Returns:
            ChatPromptTemplate: The created chat prompt template.
        """
        try:
            log.info("Creating map prompt template...")
            prompt = ChatPromptTemplate.from_messages([
                ("system", self.system_prompt), 
                ("user", "Query: {user_query}\nText: {text_chunk}")]
                ).partial(format_instructions=self.parser.get_format_instructions())
            log.info("Map prompt template created successfully.")
            return prompt
        except Exception as e:
            log.error("Error creating map prompt template.")
            raise CustomException(e, sys)