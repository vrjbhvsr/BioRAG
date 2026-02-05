import json
import re
from typing import Any, Dict

def extract_first_json_object(text: str) -> str:
    """
    Extract the first JSON object {...} from a larger string.
    Works even if the model adds text before/after the JSON.
    """
    match = re.search(r"\{.*\}", text, flags=re.DOTALL)
    if not match:
        raise ValueError("No JSON object found in LLM output.")
    return match.group(0)


def reduce_normaliser(raw_output: Any) -> str:
    """
    Normalizes raw LLM outputs:
    - Extracts JSON from messy text (if needed)
    - Parses JSON safely
    - Ensures schema fields exist:
        - analysis: str
        - key_metrics: list[dict]
    - Returns a JSON string (ready for Pydantic parsing)
    """
    # 1) Convert to dict
    if isinstance(raw_output, dict):
        data: Dict[str, Any] = raw_output

    elif isinstance(raw_output, str):
        text = raw_output.strip()

        # If it's wrapped in quotes, unwrap once
        if (text.startswith("'") and text.endswith("'")) or (text.startswith('"') and text.endswith('"')):
            text = text[1:-1].strip()

        # Try direct parse first
        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            # Extract JSON object from messy output (prefix/suffix text)
            try:
                json_str = extract_first_json_object(text)
                data = json.loads(json_str)
            except Exception:
                # Fallback: return minimal valid JSON
                return json.dumps({
                    "key_metrics": [],
                    "analysis": "JSON parsing failed"
                }, ensure_ascii=False)

    else:
        return json.dumps({
            "key_metrics": [],
            "analysis": "Unsupported output type"
        }, ensure_ascii=False)

    # 2) Normalize schema
    analysis = data.get("analysis", "")
    if not isinstance(analysis, str):
        data["analysis"] = str(analysis)

    key_metrics = data.get("key_metrics", [])
    if not isinstance(key_metrics, list):
        key_metrics = []
    # Keep only dict metrics (drop strings/nulls)
    key_metrics = [m for m in key_metrics if isinstance(m, dict)]
    data["key_metrics"] = key_metrics

    # 3) Return clean JSON string
    return json.dumps(data, ensure_ascii=False)
