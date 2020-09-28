import time
import arg_parser_factory

from service import kcm_service
from service.query_service import query_keyword_from_path
from time_utils import show_current_time

if __name__ == '__main__':
    # begin = time.time()
    # file_utils.savedb()
    # end = time.time()
    # print('time is %d seconds ' % (end - begin))
    args = arg_parser_factory.build()

    # KCM轉換
    if args.subcmd == 'kcm':
        print("進行KCM, 解析檔案：" + args.path + ", 輸出檔案：" + args.output)
        print("開始解析：" + show_current_time())
        begin = time.time()
        kcm_service.convert_kcm(args.path, args.output)
        end = time.time()
        print("結束解析：" + show_current_time())
        print('time is %d seconds ' % (end - begin))

    # 關鍵字查找
    if args.subcmd == 'query':
        print("查詢關鍵字, 查詢目標：" + args.path + ", 查詢關鍵字：" + args.keyword + ", 篩選筆數：" + str(args.limit))
        r = query_keyword_from_path(args.path, args.keyword, args.limit)
        print(r)
