import torch
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

MODEL_NAME = "meta-llama/Llama-3.1-8B-Instruct"
MAX_NEW_TOKENS = 512
DEVICE_MAP = "auto"
DTYPE = torch.bfloat16
DO_SAMPLE = False
SKIP_PROMPT = True
TEMPERATURE = 0
REPETITION_PENALTY = 1.2
RETURN_FULL_TEXT= False


#================================================================#   
#                  Prompt Constants
#================================================================

TABLE_SUMMURISER_SYSTEM_MSG = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>

You are an expert biomedical research assistant specializing in analyzing scientific tables. 
Your ONLY task is to generate a written summary of the provided table in exactly one paragraph of approximately 100 words.

**Strict Directives:**
1. **Focus on Comparisons:** Describe the relationship between the experimental groups (e.g., 1V vs 5V) and the control. 
2. **Handle Footnotes Safely:** Do not use math formulas (like E=U/d) to calculate new values. Mention that theoretical and measured values were compared if applicable, but focus on the resulting data.
3. **Data Precision:** For mean ± s.e.m. data (e.g., 319 ± 5.1), report only the mean (319) to maintain narrative flow.
4. **Professional Tone:** Use high-level scientific terminology (e.g., "osteoblastic proliferation," "amplitude-dependent response," "temporal increase").
5. **No Filler:** Start immediately with the summary. Do not use headers, bolding, or introductory phrases.

**Constraint:** If the summary is under 80 words, expand on the temporal trends (how data changed over time) or the impact of voltage/frequency variations.<|eot_id|><|start_header_id|>user<|end_header_id|>

Table Caption: [INSERT_CAPTION_HERE]
HTML Table: [INSERT_HTML_HERE]<|eot_id|><|start_header_id|>assistant<|end_header_id|>"""
