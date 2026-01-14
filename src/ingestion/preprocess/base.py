## Creating BaseCleaner(Using Abstract method)

from abc import ABC, abstractmethod
from typing import List
from langchain_core.documents import Document

class BaseCleaner(ABC):
    """
    Deifing the structure to clean any document/data.
    """

    @abstractmethod
    def clean(self, documents: List[Document]) -> List[Document]:
        """
        Clean and normalize documents.

        Args:
            documents: Raw documents

        Returns:
            Cleaned documents
        """

        pass