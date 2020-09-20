import codecs
import json
from collections import Counter


def get_wiki_json():
    # with open("wiki/Posseg_List9.json", mode="r") as file:
    with open("wiki/wiki.json", mode="r") as file:
        return json.load(file)

def calc_kcm(r):
    d = {}
    if len(r) > 0:
        print("現在匹配:" + r[0])
    for i in range(len(r)):
        # now = r[i]
        now = r[i][0:r[i].find("/")]
        # print("現在匹配:"+now+" , index:"+str(i))

        for n in r:
            if n == now:
                continue
            # print(n)
            # key = now + "&&" + n
            key = now + "&" + n[0:n.find("/")]
            if key not in d:
                d.setdefault(key, 1)
            else:
                d[key] += 1

    # for i in range(len(r)):
    #     # now = r[i][0:r[i].find("/")]
    #     now = r[i]
    #     # print("i=========" + str(i))
    #     print("匹配:"+now+" , index:"+str(i))
    #     for n in r:
    #         if n == now:
    #             continue
    #         # print(n)
    #         # key = now + "&" + n[0:n.find("/")]
    #         key = now + "&" + n
    #         # if key1 in d or key2 in d:
    #         if key in d:
    #             d[key] += 1
    #         else:
    #             d.setdefault(key, 1)
    #         # if key1 not in d or key2 not in d:
    #         #     d.setdefault(key1, 1)
    #         # else:
    #         #     d[key1] += 1
    return d


def saveJson(data ,fileName):
    with codecs.open("./output/"+ fileName +".json",mode="w" ,encoding = "utf-8") as f:
        json.dump(data,f, indent = 4, ensure_ascii = False, default = lambda x: x.__dict__)

jd = get_wiki_json()
l = []
result = []
for j in jd.values():
    # l += j
    r = list(filter(lambda x: "/n" in x, j))
    result.append(calc_kcm(r))

# print(l)
# r = list(filter(lambda x: "/n" in x, l))
# print(r)


# for item in r:
#     result.append(calc_kcm(item))

print("長度為:"+str(len(result)))
saveJson(result,"aa")
# print(result)

# d = calc_kcm(r)
# print(d)
# 關鍵字查找
# res = dict(filter(lambda item: "捷克" in item[0], d.items()))
# res = dict(filter(lambda item: "南蘆屋濱" in item[0], result[0].items()))
# print(result[0])
query_result= []
for d in result:
    res = dict(filter(lambda item: "迪士尼" in item[0], d.items()))
    # res = dict(filter(lambda item: "本線料" in item[0], d.items()))
    if res == {}:
        continue
    query_result.append(res)

print(query_result)

z = {}
for i in range(len(query_result)):
    z = dict(Counter(z) + Counter(query_result[i]))

print("=========================")
print("=========================")
print("=========================")
print("=========================")

# print(sorted(z.items(), key=lambda x:x[1], reverse=True)[:10])
print(z)
print(sorted(z.items(), key=lambda x:x[1], reverse=True)[:10])

