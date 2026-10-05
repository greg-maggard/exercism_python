def transform(legacy_data):
    data = {}
    for point_value, letters in legacy_data.items():
        for letter in letters:
            data[letter.lower()] = point_value
    return data
            
            
