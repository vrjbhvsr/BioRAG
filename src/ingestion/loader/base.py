## Creating BaseLoader(Using Abstract method)

from abc import ABC, abstractmethod
from typing import List
from langchain_core.documents import Document

class BaseLoader(ABC):
    """
    Deifing the structure for all document loaders.
    """

    @abstractmethod
    def load(self) -> List[Document]:
        """
        Load documents from the source.

        Returns:
            List[Document]: Langchain Document Objects
        """

        pass