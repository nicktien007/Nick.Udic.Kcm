import codecs
import json
import sqlite3


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

def savedb():
    db = sqlite3.connect('./DB/TEST.db')
    cursor = db.cursor()
    with open("./output/output_result.txt", mode="r") as file:
        for fLine in file:
            j = json.loads(fLine)
            for key, value in j.items():
                # print('''INSERT INTO KCM2 (KEY,VALUE) VALUES ({key}, {value})'''.format(key=str(key), value=str(value)))
                cursor.execute('INSERT INTO KCM (KEY,VALUE) VALUES ("{key}", "{value}")'.format(key=str(key), value=str(value)))
                # print('INSERT INTO KCM (KEY,VALUE) VALUES ("{key}", "{value}")'.format(key=str(key), value=str(value)))
            db.commit()

    db.close()

