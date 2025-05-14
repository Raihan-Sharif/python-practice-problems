
data_list = [13, 24, 'Karim', {'name': 'guru'}, 45, 17]

cleaned_data = []   
for item in data_list:
    if isinstance(item, int):
        cleaned_data.append(item)  

print("Cleaned data: ", cleaned_data)
