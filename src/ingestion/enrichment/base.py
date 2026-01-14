## Creating BaseSummarizer(Using Abstract method)

from abc import ABC, abstractmethod
from typing import List
from langchain_core.documents import Document

class BaseSummarizer(ABC):
    """
    Deifing the structure to clean any document/data.
    """

    @abstractmethod
    def summarize(self, documents: List[Document]) -> str:
        """
        Summarize the given table or images

        Args:
            documents: Raw documents

        Returns:
            summarized tablea or images
        """

        pass