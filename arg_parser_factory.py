from argparse import ArgumentParser, RawTextHelpFormatter


def build():
    parser = ArgumentParser(
        description='輸入 kcm 以進行KCM解析 => 範例：python3 main.py kcm ./Posseg_List9.json -output ./output_result.txt\n'
                    '輸入 query 以進行關鍵字查詢 => 範例：python3 main.py query filepath -k 政府 -limit 15'
        , formatter_class=RawTextHelpFormatter)

    subcmd = parser.add_subparsers(
        dest='subcmd', help='subcommands', metavar='SUBCOMMAND')
    subcmd.required = True

    # 進行KCM解析
    kcm_parser = subcmd.add_parser('kcm',
                                   help='進行KCM解析')
    kcm_parser.add_argument('path',
                            help='進行【KCM解析】的檔案路徑')
    kcm_parser.add_argument('-output',
                            dest='output',
                            help='輸出檔案路徑')

    # 進行KCM解析
    query_parser = subcmd.add_parser('query',
                                     help='進行關鍵字查詢')
    query_parser.add_argument('path',
                              help='進行【查詢】的檔案路徑')
    query_parser.add_argument('-keyword', "-k",
                              dest='keyword',
                              help='關鍵字',
                              default="")
    query_parser.add_argument('-limit', "-l",
                              dest='limit',
                              help='篩選筆數(default:10)',
                              default=10)

    return parser.parse_args()
