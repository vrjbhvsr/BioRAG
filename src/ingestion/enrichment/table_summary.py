from ingestion.enrichment.base import BaseSummarizer
from chains.table_summary_chain import table_summary_chain
from config.logging import log
from config.exception import CustomException
import sys


logger = log()
log = logger.get_logger(__name__)

class Table_Image_Summary(BaseSummarizer):
    """
    A summarizer for tables and images.
    """
    def __init__(self):
        try:
            log.info("Initializing Table/Image Summarizer...")
            self.chain = table_summary_chain().chain()
            log.info("Table/Image Summarizer initialized successfully.")
        except Exception as e:
            log.error("Error initializing Table/Image Summarizer.")
            raise CustomException(e, sys)

    def summarize(self, documents: list) -> str:
        """
        Summarize the given table or images

        Args:
            documents: Raw documents

        Returns:
            summarized table or images
        """
        try:
            log.info("Summarizing documents...")
            summaries = []
            for doc in documents:
                summary = self.chain.invoke({"text": doc.page_content})
                summaries.append(summary)
            final_summary = "\n".join(summaries)
            log.info("Documents summarized successfully.")
            return final_summary
        except Exception as e:
            log.error("Error summarizing documents.")
            raise CustomException(e, sys)