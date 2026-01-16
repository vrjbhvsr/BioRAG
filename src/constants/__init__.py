#================================================================#   
#                  Loader Constants
#================================================================

OCR_LANGUAGES = "eng"
MODE = "elements"
STRATEGY = "hi_res"
INFER_TABLE_STRUCTURE = True
FILE_PATH = "/home/jovyan/work/BioRAG/Data/pdfs/cells-11-02650-v2.pdf"


#================================================================#   
#                  Table summariser Constants
#================================================================   

MODEL_NAME = "Qwen/Qwen2.5-7B-Instruct"
MAX_NEW_TOKENS = 512
DEVICE_MAP = "auto"
DTYPE = "auto"
DO_SAMPLE = False
SKIP_PROMPT = True


#================================================================#   
#                  Prompt Constants
#================================================================

TABLE_SUMMURISER_SYSTEM_MSG = """You are an expert biomedical research assistant who specializes in analyzing scientific tables.
            Your ONLY task is to generate a written summary of information contained in any table provided in 100 words.

            You must follow these strict rules:

                You must NOT generate, recreate, or display any table, in any format (including Markdown, text-based rows, bullet-formatted tables, or aligned columns).
    
                You must respond ONLY with a narrative summary, written in clear and concise sentences.
    
                Your summary must highlight key trends, important values, significant differences, and notable insights present in the original table.
    
                You must NOT list every value. Focus only on meaningful findings and overall patterns.
    
                Output must be free of table structures, headings, or column-like formatting."""
