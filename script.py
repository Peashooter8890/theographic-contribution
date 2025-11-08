import json
import os
from collections import OrderedDict
from typing import Any, Dict, List, Set

JSON_FOLDER = os.path.join(os.path.dirname(__file__), "json")
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "field_reports.txt")

TYPE_MAP = {
    str: "string",
    int: "integer",
    float: "float",
    bool: "boolean",
    list: "array",
    dict: "object",
    type(None): "null",
}

def detect_type(value: Any) -> str:
    t = type(value)
    # Distinguish int vs float even though int is subclass of numbers
    return TYPE_MAP.get(t, t.__name__)

def process_file(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        return f"### {os.path.basename(path)}\nError reading file: {e}\n"

    if not isinstance(data, list):
        return f"### {os.path.basename(path)}\nFile root is not a JSON array.\n"

    field_order: List[str] = []
    seen: Set[str] = set()
    type_accumulator: Dict[str, Set[str]] = {}
    sample_object = None
    max_field_count = -1

    for obj in data:
        if not isinstance(obj, dict):
            continue
        fields = obj.get("fields")
        if not isinstance(fields, dict):
            continue

        # Track order of first appearance
        for name in fields.keys():
            if name not in seen:
                seen.add(name)
                field_order.append(name)

        # Track types
        for name, value in fields.items():
            type_accumulator.setdefault(name, set()).add(detect_type(value))

        # Candidate for sample
        field_count = len(fields)
        if field_count > max_field_count:
            max_field_count = field_count
            sample_object = obj

    lines = [f"### {os.path.basename(path)}"]

    if not field_order:
        lines.append("No usable 'fields' objects found.")
        return "\n".join(lines) + "\n"

    lines.append("Field names (order of first appearance):")
    for name in field_order:
        lines.append(f"- {name}")

    lines.append("")
    lines.append("Field type summary:")
    for name in field_order:
        types = type_accumulator.get(name, set())
        if types:
            lines.append(f"{name}: {' | '.join(sorted(types))}")
        else:
            lines.append(f"{name}: (no values found)")

    lines.append("")
    lines.append("Sample object (with max fields):")
    if sample_object is not None:
        # Pretty-print sample object
        lines.append(json.dumps(sample_object, ensure_ascii=False, indent=2))
    else:
        lines.append("None found.")

    lines.append("")
    return "\n".join(lines)

def main():
    if not os.path.isdir(JSON_FOLDER):
        print(f"JSON folder not found: {JSON_FOLDER}")
        return

    report_sections = []
    for fname in sorted(os.listdir(JSON_FOLDER)):
        if not fname.lower().endswith(".json"):
            continue
        full = os.path.join(JSON_FOLDER, fname)
        report_sections.append(process_file(full))

    if not report_sections:
        print("No JSON files processed.")
        return

    with open(OUTPUT_PATH, "w", encoding="utf-8") as out:
        out.write("\n".join(report_sections))

    print(f"Report written to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()