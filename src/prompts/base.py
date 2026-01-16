## Creating BaseLoader(Using Abstract method)
from abc import ABC, abstractmethod
from typing import List
from langchain_core.prompts.chat import ChatPromptTemplate

class BasePrompt(ABC):
    """
    Defining the structure for all prompt templates.
    """

    @abstractmethod
    def prompt(self) -> ChatPromptTemplate:
        """
        Get the prompt template.
        Returns:
            ChatPromptTemplate: The chat prompt template.
        """

        pass