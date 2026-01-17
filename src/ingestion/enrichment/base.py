## Creating BaseSummarizer(Using Abstract method)

from abc import ABC, abstractmethod
from typing import List
from langchain_core.documents import Document

class BaseSummarizer(ABC):
    """
    Deifing the structure to clean any document/data.
    """

    @abstractmethod
    def summarize(self, txt_as_html: str, caption: str) -> str:
        """
        Summarize the given table or images

        Args:
            txt_as_html: Table text in html format
            caption: Caption for the table or image

        Returns:
            summarized table or images
        """

        pass