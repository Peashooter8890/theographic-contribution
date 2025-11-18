import json
from typing import List, Dict, Any

def extract_suffix_int(s: str) -> int | None:
    """
    Extract the integer after the final '.' in the string.
    Returns None if not found or not an int.
    """
    if not isinstance(s, str):
        return None
    if '.' not in s:
        return None
    last_segment = s.rsplit('.', 1)[-1]
    # Allow stripping trailing non-digit chars if needed (customize here)
    # For now, require pure digits
    if not last_segment.isdigit():
        return None
    return int(last_segment)

def find_anomalies(objects: List[Dict[str, Any]]) -> List[Any]:
    """
    For each object, checks if def_id suffix == termID suffix + 1.
    Returns list of dictLookup values of anomalous objects.
    """
    anomalies = []
    for obj in objects:
        # Extract fields from the nested structure
        fields = obj.get("fields", {})
        term_id = fields.get("termID")
        def_id = fields.get("def_id")
        dict_lookup = fields.get("dictLookup")

        term_suffix = extract_suffix_int(term_id)
        def_suffix = extract_suffix_int(def_id)

        # If either suffix can't be parsed, treat as anomaly (can change logic)
        if term_suffix is None or def_suffix is None:
            anomalies.append(dict_lookup)
            continue

        if def_suffix != term_suffix + 1:
            anomalies.append(dict_lookup)

    return anomalies

def main():
    # Load data from easton.json
    json_path = "json/easton.json"
    
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            objects = json.load(f)
    except FileNotFoundError:
        print(f"Error: Could not find {json_path}")
        return
    except json.JSONDecodeError as e:
        print(f"Error: Could not parse JSON file: {e}")
        return

    anomalies = find_anomalies(objects)
    print("Anomalies (dictLookup values):")
    print(anomalies)
    print(f"\nTotal anomalies found: {len(anomalies)}")

if __name__ == "__main__":
    main()