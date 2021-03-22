import json

file = 'eq_data_1_day_m1.json'
with open(file) as f:
    all_eq_data = json.load(f)

readable_file = 'readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent = 4)
