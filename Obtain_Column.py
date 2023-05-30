#==========获取csv的列数===========
import csv
import glob

path=''
for file in glob.glob(path + '/*.csv'):
    input_csv = csv.reader(open(file, 'r'))
    row_num = ""
    for row in input_csv:
        row_num = row
    print(len(row_num))
    print("=====================")