from collections import Counter

from file_utils import query_keyword_from
from multithread import ThreadWithReturnValue
import time

def foo(i):
    # print('hello {0}'.format(bar))
    return query_keyword_from("output_result_"+str((i+1))+".json", "基隆市")

# # 建立 5 個子執行緒
# threads = []
# for i in range(5):
#     threads.append(ThreadWithReturnValue(target=foo, args=(i,)))
#     threads[i].start()
#
# # 主執行緒繼續執行自己的工作
# # ...
#
# # 等待所有子執行緒結束
# r = []
# for i in range(5):
#     r.append(threads[i].join())
#
# print(*r)


# 建立 5 個子執行緒
threads = []
begin = time.time()

for i in range(4):
    threads.append(ThreadWithReturnValue(target=foo, args=(i,)))
    threads[i].start()

# 主執行緒繼續執行自己的工作
# ...

# 等待所有子執行緒結束
r = []
for i in range(4):
    r.append(threads[i].join())

print(*r)
end = time.time()
print('time is %d seconds ' % (end - begin))