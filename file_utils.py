import codecs
import json


def get_wiki_json(fileName):
    with open("wiki/" + fileName, mode="r") as file:
        # with open("wiki/wiki.json", mode="r") as file:
        return json.load(file)


# def saveJson(data, fileName):
#     with codecs.open("./output/" + fileName, mode="w", encoding="utf-8") as f:
#         json.dump(data, f, indent=4, ensure_ascii=False, default=lambda x: x.__dict__)

def saveJson_writeline(data, fileName):
    with codecs.open("./output/" + fileName, mode="a+", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, default=lambda x: x.__dict__)
        f.write("\n")


def get_output_json(file_name):
    with open("./output/" + file_name, mode="r") as file:
        return json.load(file)


def query_keyword_from(file_name, keyword):
    query_result = []
    with open("./output/" + file_name, mode="r") as file:
        for fLine in file:
            res = dict(filter(lambda item: keyword in item[0], json.loads(fLine).items()))
            if res == {}:
                continue
            # print(res)
            query_result.append(res)

        return query_result
