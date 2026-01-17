from prompts.base import BasePrompt
from langchain_core.prompts import ChatPromptTemplate
from constants import *
from config.logging import log
from config.exception import CustomException
import sys

logger = log()
log = logger.get_logger(__name__)

class table_summariser_prompt(BasePrompt):
    """
    A prompt template for table summarization tasks.
    """
    def __init__(self):
        self.system_msg = TABLE_SUMMURISER_SYSTEM_MSG

    def prompt(self) -> ChatPromptTemplate:
        """
        Get the table summarization prompt template.

        Returns:
            ChatPromptTemplate: The chat prompt template for table summarization.
        """
        try:
            log.info("Creating table summarization prompt template...")
            prompt = ChatPromptTemplate([
                                        ("system", self.system_msg),
                                        ("human", "Please generate summary, Table content: \n{table_content}\nCaption: {table_caption}")
                                    ],
                                    )
            log.info("Table summarization prompt template created successfully.")
            return prompt
        except Exception as e:
            log.error("Error creating table summarization prompt template.")
            raise CustomException(e, sys)