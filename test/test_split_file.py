import os
import time


def mkSubFile(lines, head, srcName, sub):
    [des_filename, extname] = os.path.splitext(srcName)
    filename = des_filename + '_' + str(sub) + extname
    print('make file: %s' % filename)
    with open(filename, 'w') as fout:
        try:
            fout.writelines([head])
            fout.writelines(lines)
            return sub + 1
        finally:
            fout.close()


def splitByLineCount(filename, count):
    with open(filename, 'r') as fin:
        try:
            head = fin.readline()
            buf = []
            sub = 1
            for line in fin:
                buf.append(line)
                if len(buf) == count:
                    sub = mkSubFile(buf, head, filename, sub)
                    buf = []
            if len(buf) != 0:
                sub = mkSubFile(buf, head, filename, sub)
        finally:
            fin.close()


def getfilesize(filename):
    with open(filename, "rb") as fr:
        fr.seek(0, 2)  # move to end of the file
        size = fr.tell()
        print("getfilesize: size: %s" % size)
        return fr.tell()


def split_file_by_KB(t, size):
    fp = open(t, 'rb')
    i = 0
    dir_put = 'split_dir/'
    if os.path.isdir(dir_put):  # os.path.isdir	判斷路徑是否為目錄
        pass
    else:
        os.mkdir(dir_put)  # 創建dir_put文件夾
    filename_front = os.path.splitext(t)[0]  # 取到除去擴展名的文件名	os.path.splitext	分割路徑，返回路徑名和文件擴展名的元組
    temp = open(dir_put + filename_front + '_' + str(i) + '.txt', 'wb')
    buf = fp.readline()

    while 1:
        temp.write(buf)
        buf = fp.readline()
        try:
            if buf[0] == "":
                continue
        except IndexError:
            print(filename_front + '_' + str(i) + '.txt')
            temp.close()
            fp.close()
            return
        if getfilesize(dir_put + filename_front + '_' + str(i) + '.txt') >= size:
            print(filename_front + '_' + str(i) + '.txt')
            i += 1
            temp.close()
            temp = open(dir_put + filename_front + '_' + str(i) + '.txt', 'wb')
    fp.close()


begin = time.time()
split_file_by_KB('output_result.txt', 500000000)
end = time.time()
print('time is %d seconds ' % (end - begin))
