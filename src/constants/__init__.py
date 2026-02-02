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


#================================================================#   
#                  Embedding Constants
#================================================================

EMBEDDING_MODEL_NAME = "nvidia/llama-embed-nemotron-8b"
EMBEDDING_DEVICE = 0
TRUST_REMOTE_CODE = True
PARENT_CHUNK_SIZE = 2000
PARENT_CHUNK_OVERLAP = 100
CHILD_CHUNK_SIZE = 400
CHILD_CHUNK_OVERLAP = 20
SEPARATORS = ["\n\n", "\n", " ", ""]
ADD_START_INDEX = True


#================================================================#
#                  Vectorstore Constants
#================================================================#

CHROMA_PERSIST_DIR = "chroma_biorag_db"
PARENT_DOCSTORE_PATH = "./parent_docstore_biorag"

#================================================================#   
#                  Query Constants
#================================================================

QUERY_REWRITE_SYSTEM_MSG = """

You are a document-aligned technical query generator for the Bioelectromagnetics and Cell Biology domain.

Task:
Your task is to rewrite the user query for better search retrieval. Do not change the core subject or intent.

Primary objective:
The generated queries must help retrieve the SAME document sections as the original query.
Do NOT expand, generalize, or biologically enrich the query beyond the document’s scope.

Alignment constraints (MANDATORY):
- Preserve the original intent and level of abstraction of the input query.
- Do NOT introduce new cell types, organisms, tissues, or biological models not explicitly present or clearly implied in the input.
- Do NOT replace electrical stimulation with electromagnetic, magnetic, or clinical modalities unless explicitly stated.
- Do NOT shift from background or mechanistic questions to outcome-based, clinical, or experimental-result questions unless explicitly requested.
- Do NOT introduce new devices, procedures, or application contexts.

Semantic constraints:
- Queries must remain conservative and document-grounded.
- Prefer general mechanistic or explanatory phrasing over specific experimental outcomes.
- Do not speculate beyond concepts present in the input.

Terminology constraints:
- Do NOT rephrase, expand, or reinterpret technical acronyms.
- Use only terminology that is present or directly implied by the input query.

Output constraints:
- Output ONLY the queries.
- Exactly 3 queries.
- One query per line.
- No numbering, no bullets.
- No explanations, notes, headers, or additional text.

CRITICAL: You must return ONLY a JSON object. 
Do not include any text before or after the JSON.
Example format:
{{"queries": ["query 1", "query 2", "query 3"]}}

Failure condition:
If any text other than exactly three standalone queries is produced, the output is invalid.



Input Query: {input_query}



STRICT RULE:
Return only the three queries, each on its own line.



"""

QUERY_MODEL_NAME = "meta-llama/Llama-3.1-8B-Instruct"
QUERY_MAX_NEW_TOKENS = 128
QUERY_DEVICE_MAP = "cpu"
QUERY_DTYPE = torch.bfloat16
QUERY_DO_SAMPLE = False
QUERY_SKIP_PROMPT = True
QUERY_TEMPERATURE = 0.4
QUERY_REPETITION_PENALTY = 1.2
QUERY_TOP_P = 0.9

#QUERY_RETURN_FULL_TEXT= False


#================================================================#
#                  Mapping Constants
#================================================================#

MAP_PROMPT = """You are a Scientific Data Extraction Engine.

TASK:
Analyze the provided document text and determine whether it contains information relevant to the user query.
If relevant, extract and summarize the experimental findings in a single, detailed, informative, well-formed paragraph.

STRICT OUTPUT RULES (MANDATORY):
1. Output ONLY a single valid JSON object.
2. Output MUST start with '{{' and end with '}}'.
3. The JSON object must contain exactly two fields: "relevant" and "summary".
4. The "summary" field MUST be a SINGLE STRING containing ONE coherent paragraph.
5. The summary MUST describe all findings, observations, or understanding, and MUST NOT contain objects, dictionaries, lists, or key–value formatting inside it.
6. The summary should be up to 400–500 words.
7. Do NOT include explanations, notes, markdown, code, or any extra text outside the JSON.
8. If no relevant information is found, return EXACTLY:
   {{"relevant": false, "summary": "No relevant data found."}}

SCHEMA:
{{
  "relevant": boolean,
  "summary": string
}}
"""

MAP_MODEL_NAME = "meta-llama/Llama-3.1-8B-Instruct"
MAP_MAX_NEW_TOKENS = 1028
MAP_DEVICE_MAP = "cpu"
MAP_DTYPE = torch.bfloat16
MAP_DO_SAMPLE = False
MAP_SKIP_PROMPT = True
MAP_TEMPERATURE = 0.7
MAP_REPETITION_PENALTY = 1.2
MAP_TOP_P = 0.9
MAX_CONCURRENCY = 4


#================================================================#   
#                  Reduction Constants
#================================================================

REDUCE_PROMPT = """
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

You are a Senior Research Data Auditor. Your task is to synthesize provided summaries into a structured technical narrative. 

### REASONING PROCESS (Internal Audit)
Before providing the JSON output, you must perform a multi-step logical audit:
1. **Variable Extraction**: Identify all explicit numerical data and specific qualitative descriptors.
2. **Constraint Verification**: Ensure no data points are being inferred, averaged, or estimated.
3. **Causal Mapping**: Trace the direct "If-Then" relationships provided in the source text.
4. **Mirroring Check**: Confirm that descriptive adjectives in the analysis match the source exactly.

### NARRATIVE REQUIREMENTS (The "analysis" field):
- **Factual Anchor**: Use only the information explicitly stated in the source text. 
- **Qualitative vs. Quantitative**: Include and **bold** all specific numbers or units. Mirror descriptive language (e.g., "enhanced," "decreased") exactly. 
- **Causal Logic**: Explain the relationship between inputs and outcomes based solely on provided evidence.
- **Seamless Style**: Write in professional paragraphs without headers.

### DATA EXTRACTION RULES (The "key_metrics" field):
- **STRICT FACTUALITY**: Only extract values that appear verbatim.
- **NO INFERENCE**: Do not calculate or "fill in" missing values.
- **Empty State**: If no explicit numerical measurements are found, return "key_metrics": [].

### OUTPUT FORMAT:
- Output MUST be a valid JSON object.
- The "analysis" field must be a single string. Use \\n for paragraph breaks.<|eot_id|><|start_header_id|>user<|end_header_id|>

Source Data:
{map_summaries}

### RESPONSE (JSON ONLY):
<|eot_id|><|start_header_id|>assistant<|end_header_id|>
<|thought|>
"""