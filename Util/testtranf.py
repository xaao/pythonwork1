import json
import jsonpath

json_data = json.load(open(r'C:\Users\11699\Desktop\333333\data-6538-10483.json', 'r', encoding='utf8'))
for i in [0, 2, 3, 4]:
    values_list = jsonpath.jsonpath(json_data, f'$.data.result[{i}].values')

    print(values_list[0])