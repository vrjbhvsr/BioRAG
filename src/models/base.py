## Creating BaseLoader(Using Abstract method)
from abc import ABC, abstractmethod
from typing import List
from langchain_core.runnables.base import RunnableBinding

class BaseModelLoader(ABC):
    """
    Deifing the structure for all document loaders.
    """

    @abstractmethod
    def load(self) -> RunnableBinding:
        """
        Load the model .

        Returns:
            RunnableBinding: A runnable binding for the model.
        """

        pass