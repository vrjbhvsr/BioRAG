from ingestion.loader.pdfloader import PDFLoader
from ingestion.preprocess.cleaner import DocumentCleaner
from ingestion.splitting.SectionBased_splitter import SectionBasedSplitter
from retrieval.parent_retriever import retirever
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
retriever = retirever()
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
    retriever = pipeline.run()
    query = "Compare the simulated electric field outcomes with the measured electric current."
    relevent_docs = retriever.invoke(query)
    print(len(relevent_docs))
    for i in relevent_docs:
        print(i.metadata.get('section_header'))
    

    log.info(
    "\n"
    "=====================================================\n"
    "         DATA INGESTION PIPELINE Finished 🚀\n"
    "====================================================="
)
    
except Exception as e:
    log.error(e)
    raise CustomException(e, sys)
