## Creating BaseSplitter(Using Abstract method)

from abc import ABC, abstractmethod
from typing import List
from langchain_core.documents import Document

class BaseSplitter(ABC):
    """
    Deifing the structure to clean any document/data.
    """

    @abstractmethod
    def split(self, documents: List[Document]) -> List[Document]:
        """
        Semantically split the Documents.

        Args:
            documents: Raw documents

        Returns:
            Semantically splitted documents
        """

        pass