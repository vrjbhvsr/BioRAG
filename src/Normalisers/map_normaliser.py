import json
from config.logging import log
from config.exception import CustomException
import sys

logger = log()
log = logger.get_logger(__name__)

def map_normaliser(raw: str) -> str:
    """
    Extracts the FIRST valid JSON object from LLM output
    and returns it as a JSON STRING (LangChain-safe).
    """
    try:
        log.info("Normalizing LLM output...")
        if not raw or not isinstance(raw, str):
            raise ValueError("LLM output is empty or not a string")

        text = raw.strip()
        text = text.replace("```json", "").replace("```", "")

        start = None
        brace_count = 0

        for i, ch in enumerate(text):
            if ch == "{":
                if start is None:
                    start = i
                brace_count += 1
            elif ch == "}":
                brace_count -= 1
                if brace_count == 0 and start is not None:
                    json_text = text[start:i+1]
                    break
        else:
            raise ValueError("No JSON object found in LLM output")

        try:
            data = json.loads(json_text)
        except json.JSONDecodeError as e:
            raise ValueError(f"JSON parsing failed: {e}\nExtracted:\n{json_text}")

        # Schema hardening
        data.setdefault("relevant", False)
        data.setdefault("summary", "")

        if isinstance(data["summary"], dict):
            data["summary"] = " ".join(f"{k}: {v}" for k, v in data["summary"].items())

        data["relevant"] = bool(data["relevant"])
        data["summary"] = str(data["summary"])

        log.info("LLM output normalized successfully.")

        return json.dumps(data, ensure_ascii=False)

    except Exception as e:
        log.error("Error normalizing LLM output.")
        raise CustomException(e, sys)


