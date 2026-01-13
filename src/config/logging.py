import logging
import os
from pathlib import Path
import inspect
from logging.handlers import RotatingFileHandler
from typing import Optional

class log:
    def __init__(self):
        self.LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
        self.LOG_FORMAT = os.getenv("LOG_FORMAT",
                                   "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
                                   )
        self.LOG_DIR = os.getenv("LOG_DIR", "logs")
        self.LOG_FILE = os.getenv("LOG_FILE", "BioRAG.log")

    def _check_log_dir() -> None:
        "Create a log directory if not exist."
        os.makedirs(self.LOG_DIR, exist_ok = True)

    def get_logger(name: Optional[str]: None, 
        level: str = self.LOG_LEVEL,) -> logging.Logger:

        """
        Returns a configured logger instance.
        """

        logger = logging.getLogger(name)
        logger.setLevel(level)

        # Avoiding adding handlers multiple times
        if logger.handlers:
            return logger

        self._check_log_dir()
        formatter = logging.Formatter(self.LOG_FORMAT)     # Setting how the logg message will look like

        console_handler = logging.StreamHandler()          # setting the log message got to terminal
        console_handler.setFormatter(formatter)
        console_handler.setLevel(level)

        # File handler (rotating)
        file_handler = RotatingFileHandler(                 # Rotating File Handler limits log file size           
        filename=os.path.join(self.LOG_DIR, self.LOG_FILE), # by rotating, meaning archiving old logs, and 
            maxBytes=5 * 1024 * 1024,  # 5 MB               # creating new ones. So, the BioRAG.log will grow 
            backupCount=5,                                  # till 5MB then creates new BioRAG.log.1 and  
        )                                                   # archives the old. it does It does this upto 25                                                                MB(backup count 5) and deletes the archived                                                                    older one.

        
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level)
    
        logger.addHandler(console_handler)  # the log message go to terminal
        logger.addHandler(file_handler)     # the log message go to file
    
        # Prevent logs from being duplicated by root logger
        logger.propagate = False
    
        return logger        