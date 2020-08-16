from json import loads, dump

with open(r'./training.json', encoding='utf-8') as fh:
    json_txt = fh.read()
    json_txt = str(json_txt).replace('True', 'true').replace('False', 'false')
    data = loads(json_txt)

with open(r'./test.json', encoding='utf-8') as fh:
    json_txt = fh.read()
    json_txt = str(json_txt).replace('True', 'true').replace('False', 'false')
    test_data = loads(json_txt)

empty_dict = {}
for data in test_data.items():
    if len(data[1][1]) <= 60:
        empty_dict[data[0]] = [data[1][0], data[1][1]]
        with open(r'./test.json', mode='w', encoding='utf-8') as f:
            dump(empty_dict, f, ensure_ascii=False, indent=1, sort_keys=True, separators=(',', ': '))