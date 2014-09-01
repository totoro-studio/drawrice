__author__ = 'Tony'

import csv


class CsvData:
    list = {'sid': '',
            'name': '',
            'class': ''}


class CsvOpt():
    # __f = None
    #
    # def __init__(self, filepath):
    # self.__f = open(filepath,'r')
    #
    # def __del__(self):
    #     self.__f.close()

    def csvread(self, filepath):
        with open(filepath, 'r', newline='') as f:
            l = CsvData.list
            ls = []
            for row in csv.reader(f):
                l = l.copy()
                l['sid'] = row[0]
                l['name'] = row[1]
                l['class'] = row[2]
                ls.append(l)
        return ls

# co = CsvOpt().csvread('d:\\新生晚会学生名单380人.csv')
# print(co)

