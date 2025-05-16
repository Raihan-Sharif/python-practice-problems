

# Implementation of flattening a nested JSON
def flatten_json(nested_json, parent_key='', sep='.'):
    items = []
    for k, v in nested_json.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_json(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

# Example usage
nested_json = {"a": {"b": 1}}
flattened_json = flatten_json(nested_json)
print(flattened_json)  