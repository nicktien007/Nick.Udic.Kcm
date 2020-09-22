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


# num_lines = sum(1 for line in open("./input/"+'wiki2.json'))
# print(num_lines)

begin = time.time()
splitByLineCount("./output/"+'output_result.json',75000)
end = time.time()
print('time is %d seconds ' % (end - begin))
