from datetime import datetime
import time
from collections import Counter

from file_utils import query_keyword_from

def show_current_time():
    return datetime.now().strftime("%H:%M:%S")

def query_keyword_frompath(target_name, keyword):
    print("查詢開始..." + show_current_time())
    begin = time.time()
    query_result = query_keyword_from(target_name, keyword)
    print("查詢結束..." + show_current_time())

    z = {}
    for i in range(len(query_result)):
        z = dict(Counter(z) + Counter(query_result[i]))

    # print("================================")
    # print("============統計如下==============")
    # print("================================")

    # print(z)
    end = time.time()
    print('time is %d seconds ' % (end - begin))
    return sorted(z.items(), key= lambda x: x[1], reverse= True)[:10]