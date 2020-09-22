import kcm_service
from query_service import query_keyword_frompath

# 進行轉換
# kcm_service.convert_kcm("example.json", "output_example.txt")

# 關鍵字查找
r = query_keyword_frompath("output_result_2.json", "捷克")
print(r)
