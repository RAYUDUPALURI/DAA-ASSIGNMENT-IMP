my_dict = {'ios': 8, 'os': 2, 'web': 10, 'app': 3}

sorted_dict_by_value = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print("Dictionary sorted by values:")
for key, value in sorted_dict_by_value.items():
    print(key, ':', value)
