from collections import Counter

from file_utils import query_keyword_from
from multithread import ThreadWithReturnValue
import time


from service.query_service import query_keyword_from_path


def foo(i):
    # print('hello {0}'.format(bar))
    # return query_keyword_from_path("./output/output_result_" + str((i + 1)) + ".txt", "司法")
    return query_keyword_from_path("./output/output_result_" + str(i) + ".txt", "法院")


# 建立 5 個子執行緒
threads = []
begin = time.time()

for i in range(8):
    threads.append(ThreadWithReturnValue(target=foo, args=(i,)))
    threads[i].start()

# 主執行緒繼續執行自己的工作
# ...

# 等待所有子執行緒結束
r = []
for i in range(8):
    r.append(threads[i].join())

z = {}
for i in range(len(r)):
    z = dict(Counter(z) + Counter(r[i]))

res = sorted(z.items(), key=lambda x: x[1], reverse=True)[:int(10)]
print(res)
end = time.time()
print('last time is %d seconds ' % (end - begin))
