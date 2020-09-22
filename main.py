from collections import Counter

from file_utils import get_wiki_json, saveJson_writeline, get_output_json, query_keyword_from
from kcm_services import calc_kcm

from datetime import datetime


def show_current_time():
    return datetime.now().strftime("%H:%M:%S")

wiki_json_data = get_wiki_json("Posseg_List18.json")

print("開始匹配：" + show_current_time())
for j in wiki_json_data.values():
    filter_list = list(filter(lambda x: "/n" in x, j))
    saveJson_writeline(calc_kcm(filter_list), "output_result.json")
print("結束匹配 =", show_current_time())

# print(result)

# 關鍵字查找
print("查詢開始..." + show_current_time())
query_result = query_keyword_from("output_result.json", "基隆市")
print("查詢結束..." + show_current_time())

z = {}
for i in range(len(query_result)):
    z = dict(Counter(z) + Counter(query_result[i]))

print("================================")
print("================================")
print("============統計如下==============")
print("================================")
print("================================")

# print(z)
print(sorted(z.items(), key=lambda x:x[1], reverse=True)[:10])
