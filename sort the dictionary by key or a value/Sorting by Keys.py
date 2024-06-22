my_dict = {'car': 2, 'bike': 20, 'flight': 10, 'train': 3}

sorted_dict_by_key = dict(sorted(my_dict.items()))

print("Dictionary sorted by keys:")
for key, value in sorted_dict_by_key.items():
    print(key, ':', value)
