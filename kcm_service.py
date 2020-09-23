from file_utils import get_input_json, saveJson_writeline
from time_utils import show_current_time
import time



def calc_kcm(filter_list):
    d = {}
    # print("現在匹配:" + filter_list[0])
    for i in range(len(filter_list)):
        # now = r[i]
        now_sp = filter_list[i][0:filter_list[i].find("/")]

        for n in filter_list:
            n_sp = n[0:n.find("/")]
            if n_sp == now_sp:
                continue

            key1 = now_sp + "&" + n_sp  # 鱉&煎蛋
            key2 = n_sp + "&" + now_sp  # 煎蛋&鱉

            if key1 not in d and key2 not in d:
                d[key1] = 1
            elif key1 in d:
                d[key1] += 1
            elif key2 in d:
                d[key2] += 1
    return d


def convert_kcm(input_path, output_path):
    input_json_data = get_input_json(input_path)

    for j in input_json_data.values():
        exclude = ['/ns','nr','nz','nt','nw']
        filter_list = list(filter(lambda x: "/n" in x and not any(y in x for y in exclude), j))
        # 空字典檢查
        query_dic = calc_kcm(filter_list)
        if query_dic == {}:
            continue
        saveJson_writeline(query_dic, output_path)