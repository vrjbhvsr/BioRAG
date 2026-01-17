from uuid import uuid4
import re
from typing import List
from langchain_core.documents import Document
from ingestion.splitting.base import BaseSplitter
from ingestion.enrichment.table_summary import Table_Image_Summary
from config.exception import CustomException
import sys
from config.logging import log  

logger = log()
log = logger.get_logger(__name__)   


class SectionBasedSplitter(BaseSplitter):
    """
    A splitter that splits documents based on sections.
    """
    def __init__(self):
        self.table_summarizer = Table_Image_Summary()


    def split(self, documents: List[Document]) -> List[Document]:
        """
        Section-wise split the Documents.

        Args:
            documents: Raw Cleaned documents

        Returns:
            Section-wise splitted documents
        """
        new_docs = []
        new_content = ""
        section_header = ""
        subsection_header = ""
        Paper_title = "Pulsed Electrical Stimulation Affects Osteoblast Adhesion and Calcium Ion Signaling"
        metadata = {}
        current_chunk_page = None
        section_pattern = r"^(\d+\.)+\s*(.+)$"
        subsection_pattern = r"`\s*\d+(?:\.\d+)*\s+[^\n]+`"
        try:
            for doc in documents:
                metadata_copy = doc.metadata.copy()
                content = doc.page_content
                current_page = metadata_copy.get('page_number', None)
                doc_category = doc.metadata.get('category', '')
                is_section_header = (doc_category == 'Title')

                if is_section_header:
                    if new_content:
                        chunk_metadata = doc.metadata.copy()
                        chunk_metadata['section_header'] = section_header
                        
                        if current_chunk_page is not None:
                            chunk_metadata['start_page'] = current_chunk_page
                        chunk_metadata['end_page'] = current_page
                        chunk_metadata['paper_title'] = Paper_title
                        document_id = str(uuid4())
                        chunk_metadata['document_id'] = document_id
                        new_docs.append(Document(page_content=new_content.strip(), metadata=chunk_metadata))

                    if content.strip() != Paper_title:
                        section_header = content.strip()
                        new_content = ""
                        metadata = metadata_copy
                        current_chunk_page = current_page
                    continue

                # Now we will add the category wise content, unless it is a section header
                if doc_category in ['NarrativeText', 'FigureCaption']:
                    current_page = doc.metadata.get('page_number', None)
                    chunk_metadata = doc.metadata.copy()
                    chunk_metadata['section_header'] = section_header
                    chunk_metadata['subsection_header'] = subsection_header
                    if re.match(section_pattern, content.strip()):
                        subsection_header = content.strip()
                    new_content += "\n" + content.strip()+ "\n"

                if (doc_category == "NarrativeText" and content.startswith("Table")) or (doc_category == "FigureCaption" and content.startswith("Table")):
                        caption = content.strip()

                if doc_category == "Table" and metadata_copy.get('text_as_html'):
                        txt_html = metadata_copy.get('text_as_html')
                        summary = self.table_summarizer.summarize(txt_html, caption)
                        new_content += "\n Table Summary: \n"+ txt_html + summary.replace("Assistant: ", "") + "\n"
                        
                metadata.update(chunk_metadata)

            # After processing all documents, check if there's remaining content to be added
            if new_content:
                chunk_metadata = metadata.copy()
                chunk_metadata['section_header'] = section_header
                if current_chunk_page is not None:
                    chunk_metadata['start_page'] = current_chunk_page
                chunk_metadata['end_page'] = current_page
                chunk_metadata['paper_title'] = Paper_title
                document_id = str(uuid4())
                chunk_metadata['document_id'] = document_id
                new_docs.append(Document(page_content=new_content.strip(), metadata=chunk_metadata))
            return new_docs
        except Exception as e:
            log.error("Error during section-based splitting.")
            raise CustomException(e, sys)