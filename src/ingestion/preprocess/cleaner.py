import os
import sys
import re
from config.logging import log
from config.exception import CustomException
from ingestion.preprocess.base import BaseCleaner
from constants import *
from langchain_core.documents import Document
from typing import List, Set

logger = log()

log = logger.get_logger(__name__)
class DocumentCleaner(BaseCleaner):
    def _get_categories(self, documents: List[Document]) -> Set[str]:
        """ This function gets the present categories in the documents. This function is needed to determine the necessary categories to work with."""
        try:
            cats = set()
            for doc in documents:
                cats.add(doc.metadata.get('category'))
    
            log.info("The available categories are %s", cats)
            return cats
        except Exception as e:
            log.error(e)
            raise CustomException(e,sys)

    
    def _filter_documents(self, documents: List[Document]) -> List[Document]:
        """This function will only keep the document with only four categories: Title, NarrativeText, Table, FigureCaption"""
        categories = self._get_categories(documents)
        try:
            filterd_docs = [doc for doc in documents if doc.metadata.get('category') not in ['Image', 'Header', 'ListItem', 'UncategorizedText']]
            log.info("The number of documents after filtering with necessary categoreis %d", len(filterd_docs))
    
            return filterd_docs
        except Exception as e:
            log.error(e)
            raise CustomException(e,sys)

    def _remove_boilerplate(self, documents: List[Document]) -> list[Document]:

        """This function removes boiler plates present in the document content."""
        BOILERPLATE_PATTERN = r"""\b\d+\s*of\s*\d+\b | # Matches '18 of 22'
        \b[A-Za-z]+\s+\d{4},\s*\d+,\s*\d+\b # Matches 'Cells 2022, 11, 2650'
        """
        Docs = self._filter_documents(documents)
        try:
            boilerplate_regex = re.compile(BOILERPLATE_PATTERN, re.VERBOSE)
            for doc in Docs:
                if (doc.metadata.get('category') == 'NarrativeText'):
                    if boilerplate_regex.fullmatch(doc.page_content.strip()):
                        Docs.remove(doc)
            log.info("Boiler plates removed from the filtered documents.")
            return Docs

        except Exception as e:
            log.error(e)
            raise CustomException(e,sys)
        
    # Remove unnnecessary narattivetext like citation publisher info

    def _clean_narrative_text(self, documents: List[Document]) -> list[Document]:
        text_start_with = ['Cells 2022, 11, 2650', 'Article', 'Academic Editor','Received:', 'Citation',
                           'Accepted:' , 'Published:',"Publisher’s Note:", "G check for updates", "Susanne Staehlke 1",
                           "Institutional Review Board Statement: Not applic",'Informed Consent Statement: Not applicable',
                           'Conﬂicts of Interest:', 'https:', 'Copyright: © ', 'Acknowledgments:', 'Funding:','Data Availability,     Statement','References']
        Docs = self._remove_boilerplate(documents)
        try:
            docs = [doc for doc in Docs if not any(doc.page_content.strip().startswith(text) for text in text_start_with)]
            log.info("All the Documents cleaned successfully...")
            return docs
        except Exception as e:
            log.error(e)
            raise CustomException(e,sys)

    def clean(self, documents: List[Document]) -> List[Document]:
        """This function filters documetns bsed on required document category.
        - It also removes boiler plates.
        - It also cleans the narrative text.
        """
        documents = documents.copy()
        return self._clean_narrative_text(documents)
            
                