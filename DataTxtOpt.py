__author__ = 'Tony'

import time, os

class TxtData:
    checkin = {'sid'    :   '',
               'checktime'    :  ''}

class TxtOpt():
    _f = None

    def __init__(self, filepath):
        self._f = open(filepath,'r')

    def __del_(self):
        self._f.close()

class CheckinTxtOpt(TxtOpt):
    def checkinread(self):
        ls = self._f.read().replace('\n',' ').split(' ')
        ls = list(set(ls))  #字符串数组去重，但会打乱数组的排序

        nls = []    #删除数组中不合要求的字符串(长度不为8)
        for l in ls:
            if len(l) == 8: nls.append(l)

        c = TxtData.checkin
        cis = []
        for l in nls:
            c = c.copy()
            c['sid'] = l
            c['checktime'] = time.strftime("%Y%m%d %H:%M:%S", time.gmtime())
            cis.append(c)
        return cis

class ListTxtOpt(TxtOpt):

    def __init__(self):
        if os.path.isdir('.\exportfile'):
            pass
        else:
            os.mkdir('.\exportfile')
        filename = '.\exportfile\\' + 'list' + time.strftime("%Y%m%d%H%M%S", time.gmtime()) + '.csv'
        self._f = open(filename,'w', encoding='UTF-8')

    def exportlist(self,rows):
        count = 0
        for row in rows:
            s = row['sid'] + ',' + row['name'] + ',' + row['class'] + ',' + str(row['checktime']) + ',' + str(row['wintype']) + '\n'
            self._f.writelines(s)
            count += 1
        return count

class WinListTxtOpt(TxtOpt):
    def __init__(self):
        if os.path.isdir('.\exportfile'):
            pass
        else:
            os.mkdir('.\exportfile')
        filename = '.\exportfile\\' + 'winlist' + time.strftime("%Y%m%d%H%M%S", time.gmtime()) + '.csv'
        self._f = open(filename,'w', encoding='UTF-8')

    def exportwinlist(self,rows):
        count = 0
        for row in rows:
            s = row['sid'] + ',' + row['name'] + ',' + row['class'] + ',' + str(row['wintype']) + '\n'
            self._f.writelines(s)
            count += 1
        return count

class FileOpt():
    def clearalltxtfile(self):
        return self.clearpathfile('.\exportfile') and self.clearpathfile('.\log')

    def clearpathfile(self, path):
        try:
            if os.path.isdir(path):
                for root, dirs, files in os.walk(path, topdown=False):
                    for name in files:
                        os.remove(os.path.join(root, name))
                    for name in dirs:
                        os.rmdir(os.path.join(root, name))
        except:
            return False
        else:
            return True

class SysLogOpt():
    def __init__(self):
        if os.path.isdir('.\log'):
            pass
        else:
            os.mkdir('.\log')
        filename = '.\log\\' + 'sys.log'
        self._f = open(filename,'a', encoding='UTF-8')

    def write(self,str):
        self._f.write('\n')
        self._f.writelines(time.strftime("%Y%m%d %H:%M:%S", time.gmtime()))
        self._f.write('\n')
        self._f.writelines(str)
        self._f.write('\n')
