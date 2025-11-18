import json
import os
from pathlib import Path

def truncate_arrays(obj):
    """Recursively truncate all arrays with size > 1 to contain only the first element."""
    if isinstance(obj, dict):
        return {key: truncate_arrays(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        if len(obj) > 1:
            return [truncate_arrays(obj[0])]
        elif len(obj) == 1:
            return [truncate_arrays(obj[0])]
        else:
            return obj
    else:
        return obj

def process_json_files():
    """Process all JSON files in .json folder and output to cpjsons folder."""
    # Define paths
    input_folder = Path("json")
    output_folder = Path("cpjsons")
    
    # Create output folder if it doesn't exist
    output_folder.mkdir(exist_ok=True)
    
    # Check if input folder exists
    if not input_folder.exists():
        print(f"Error: {input_folder} folder does not exist")
        return
    
    # Process each JSON file
    json_files = list(input_folder.glob("*.json"))
    
    if not json_files:
        print(f"No JSON files found in {input_folder}")
        return
    
    for json_file in json_files:
        try:
            # Read the JSON file
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Process each entity in the JSON
            if isinstance(data, list):
                for entity in data:
                    if isinstance(entity, dict) and "fields" in entity:
                        entity["fields"] = truncate_arrays(entity["fields"])
            elif isinstance(data, dict) and "fields" in data:
                data["fields"] = truncate_arrays(data["fields"])
            
            # Write to output folder
            output_file = output_folder / json_file.name
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            print(f"Processed: {json_file.name}")
            
        except Exception as e:
            print(f"Error processing {json_file.name}: {e}")
    
    print(f"\nProcessing complete. Output files saved to {output_folder}")

if __name__ == "__main__":
    process_json_files()