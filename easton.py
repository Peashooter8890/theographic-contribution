import json

# Load the JSON file
with open('json/easton.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Track if any mismatches are found
mismatches_found = False

# Iterate through each object in the JSON
for obj in data:
    term_label = obj.get('termLabel', '')
    item_num = obj.get('itemNum', 0)
    dict_lookup = obj.get('dictLookup', '')
    
    # Calculate expected dictLookup based on the formula
    if item_num == 0:
        expected_dict_lookup = term_label
    else:
        expected_dict_lookup = f"{term_label} {item_num}"
    
    # Check if actual matches expected
    if dict_lookup != expected_dict_lookup:
        mismatches_found = True
        print(f"Mismatch found:")
        print(f"  termLabel: {term_label}")
        print(f"  itemNum: {item_num}")
        print(f"  Expected dictLookup: '{expected_dict_lookup}'")
        print(f"  Actual dictLookup: '{dict_lookup}'")
        print()

# If no mismatches were found, print success message
if not mismatches_found:
    print("Everything matches.")