import os
import sys
from config.logging import logging
from config.exception import CustomException
from ingestion.preprocess.base import BaseCleaner
from constants import *
from langchain_core.document import Document
from typing import List


class cleaner(BaseCleaner):
    def __init__(self, documents: List[Document]):
        self.documents = documents

    def