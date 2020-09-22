from file_utils import get_input_json, saveJson_writeline


def calc_kcm(filter_list):
    d = {}
    # if len(filter_list) > 0:
    # print("現在匹配:" + filter_list[0])
    for i in range(len(filter_list)):
        # now = r[i]
        now_sp = filter_list[i][0:filter_list[i].find("/")]
        # print("現在匹配:"+now+" , index:"+str(i))
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


def convert_kcm(input_name, output_name):
    input_json_data = get_input_json(input_name)

    # print("開始匹配：" + show_current_time())
    for j in input_json_data.values():
        filter_list = list(filter(lambda x: "/n" in x, j))
        saveJson_writeline(calc_kcm(filter_list), output_name)
    # print("結束匹配 =", show_current_time())
