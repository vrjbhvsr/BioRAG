from ingestion.loader.pdfloader import PDFLoader
from ingestion.preprocess.cleaner import DocumentCleaner
from ingestion.splitting.SectionBased_splitter import SectionBasedSplitter
from retrieval.parent_retriever import retriever
from ingestion.pipeline import IngestionPipeline
from config.logging import log
from config.exception import CustomException
from constants import *
import sys


logger = log()
log = logger.get_logger(__name__)


loader = PDFLoader(FILE_PATH)
cleaner = DocumentCleaner()
splitter = SectionBasedSplitter()
retriever = retriever()
try:
    log.info(
    "\n"
    "=====================================================\n"
    "        🚀 DATA INGESTION PIPELINE STARTED\n"
    "====================================================="
)

    pipeline = IngestionPipeline(loader = loader,
                                cleaner = cleaner,
                                splitter = splitter,
                                retriever = retriever
                                )
    pipeline.run()
    

    log.info(
    "\n"
    "=====================================================\n"
    "         DATA INGESTION PIPELINE Finished 🚀\n"
    "====================================================="
)
    
except Exception as e:
    log.error(e)
    raise CustomException(e, sys)
