import csv

f = open('../../crawl/cnki/csv/article.csv', encoding='utf-8')
reader = csv.reader(f)
header_row = next(reader)
for row in reader:
    # row为每一行元素
    if len(row) == 9:
        # print(row)
        name = row[0]
        classNo = row[8]
        print('title:{},classNo:{}'.format(name, classNo))
