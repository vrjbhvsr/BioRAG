import json
import re

def reduce_normaliser(raw_output) -> str:
    """
    Normalizes raw LLM outputs for CellSense:
    - Removes problematic backslashes (\)
    - Ensures valid JSON
    - Enforces schema: analysis (str), key_metrics (list[dict])
    """

    
    if isinstance(raw_output, dict):
        data = raw_output

   
    elif isinstance(raw_output, str):
        raw_output = raw_output.strip()

        
        if (raw_output.startswith("'") and raw_output.endswith("'")) or \
           (raw_output.startswith('"') and raw_output.endswith('"')):
            raw_output = raw_output[1:-1]

       
        raw_output = raw_output.replace("\\", "")

        try:
            data = json.loads(raw_output)
        except json.JSONDecodeError:
            return json.dumps({
                "is_sufficient": False,
                "key_metrics": [],
                "analysis": "JSON parsing failed"
            })

    else:
        return json.dumps({
            "is_sufficient": False,
            "key_metrics": [],
            "analysis": "Unsupported output type"
        })

    
    if not isinstance(data.get("analysis"), str):
        data["analysis"] = str(data.get("analysis", ""))

    if not isinstance(data.get("key_metrics"), list):
        data["key_metrics"] = []

    
    data["key_metrics"] = [m for m in data["key_metrics"] if isinstance(m, dict)]

    return json.dumps(data, ensure_ascii=False)