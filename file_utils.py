import codecs
import json


def get_input_json(file_path):
    with open(file_path, mode="r") as file:
        return json.load(file)


def saveJson_writeline(data, file_path):
    with codecs.open(file_path, mode="a+", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, default=lambda x: x.__dict__)
        f.write("\n")


def query_keyword_from(file_path, keyword):
    query_result = []
    with open(file_path, mode="r") as file:
        for fLine in file:
            res = dict(filter(lambda item: keyword in item[0], json.loads(fLine).items()))
            if res == {}:
                continue
            # print(res)
            query_result.append(res)

        return query_result
