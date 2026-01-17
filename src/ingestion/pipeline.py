from typing import List
from langchain_core.documents import Document
from ingestion.loader.base import BaseLoader
from ingestion.preprocess.base import BaseCleaner
from ingestion.splitting.base import BaseSplitter
from ingestion.enrichment.base import BaseSummarizer
from config.logging import log
from config.exception import CustomException
import sys
from constants import *

logger = log()

log = logger.get_logger(__name__)

class IngestionPipeline:
    def __init__(self,
                loader: BaseLoader,
                 cleaner: BaseCleaner,
                 splitter: BaseSplitter,
                ):
        self.loader = loader
        self.cleaner = cleaner
        self.splitter = splitter
    
    
    def run(self) -> List[Document]: #-> None:
        """This Function run the complete pipeline and ingest all the data to the vector database.
        Args:
        loader: BaseLoader = To loader the data. It can be anything pdf, csv, url.
        cleaner: BaseCleaner = To preprocess the data such as, removing boiler plate, unnecessary test, etc.
        splitter: BaseSplitter = To split the data either a function or a text splitter.
        summarizer: BaseSummarizer = To generate summaries
        """    

        try:
            log.info(
                "\n"
                "================ Document Loading started ================\n"
            )

            
            # Loading Documents
            documents = self.loader.load()
            #print(documents)
            log.info("Documents loaded successfully. The number of documents [%d]", len(documents))

            # Cleaning Documents
            log.info(
                "\n"
                "================ Document cleaning started ================\n"
            )
            documents = self.cleaner.clean(documents)
            log.info("Documents are cleaned successfully.")


            # Splitting Documents
            log.info(
                "\n"
                "================Section-wise Chunking initiated ================\n"
            )
            documents = self.splitter.split(documents)
            log.info("Documents are splitted and created it's chunks.")

            return documents
            
        except Exception as e:
            log.error(e)
            raise CustomException(e, sys)


    
