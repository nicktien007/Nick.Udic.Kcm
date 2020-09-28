import time
from collections import Counter

from file_utils import query_keyword_from
from time_utils import show_current_time


def query_keyword_from_path(target_path, keyword, limit=10):
    print(target_path+" 查詢開始..." + show_current_time())
    begin = time.time()
    query_result = query_keyword_from(target_path, keyword)
    # print("查詢結束..." + show_current_time())
    print(target_path+" 查詢結束..." + show_current_time())

    print("開始統計..." + show_current_time())
    z = {}
    for i in range(len(query_result)):
        z = dict(Counter(z) + Counter(query_result[i]))

    print("結束統計..." + show_current_time())
    end = time.time()
    print(target_path+' time is %d seconds ' % (end - begin))
    return sorted(z.items(), key=lambda x: x[1], reverse=True)[:int(limit)]
