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