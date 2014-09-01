__author__ = 'Tony'

import sqlite3, random
from SysConfig import SysConfig
from DataTxtOpt import SysLogOpt

class DbData:
    sinfo = {'sid': '',
             'name': '',
             'class': '',
             'checktime': '',
             'wintype': ''}

class DBase():
    _c = None
    _conn = None

    def __init__(self):
        sc = SysConfig()
        self._conn = sqlite3.connect(sc.getdatabasefiename())
        self._c = self._conn.cursor()

    def __del__(self):
        self._conn.close()

class DAllList(DBase):
    def insertbaseinfo(self, row):
        try:
            self._c.execute('INSERT INTO alllist VALUES (\'' + row['sid'] + '\',\'' + row['name'] + '\',\''+ row['class'] +'\', Null, Null)')
            self._conn.commit()
        except Exception as err:
            slog = SysLogOpt()
            serr = row['sid'] + ' ' + row['name'] + '写入失败！\n'
            sreason = '失败原因：' + str(err)
            slog.write(serr+sreason)
            return False
        else:
            return True

    def insertcheckininfo(self, row):
        try:
            self._c.execute('SELECT COUNT(sid) FROM alllist WHERE sid = \'' + row['sid'] + '\'')
            if self._c.fetchone()[0] > 0:
                self._c.execute('UPDATE alllist SET checktime = \'' + row['checktime'] + '\' WHERE sid = \'' + row['sid'] + '\'')
                self._conn.commit()
            else:
                return False
        except:
            return False
        else:
            return True

    def getalllist(self):
        self._c.execute('SELECT * FROM alllist')
        results = self._c.fetchall()
        return(self.__filldataset(results))

    def getcheckinlist(self):
        try:
            self._c.execute('SELECT * FROM alllist WHERE checktime is NOT NULL ')
            results = self._c.fetchall()
            return(self.__filldataset(results))
        except:
            return None

    def getcheckinnumber(self):
        try:
            self._c.execute('SELECT COUNT(sid) FROM alllist WHERE checktime is NOT NULL ')
            results = self._c.fetchall()
            return(results[0][0])
        except:
            return 0

    def getvalidnumber(self):
        try:
            self._c.execute('SELECT COUNT(sid) FROM alllist WHERE checktime is NOT NULL and wintype is null ')
            results = self._c.fetchall()
            return(results[0][0])
        except:
            return 0

    def getnotcheckinlist(self):
        self._c.execute('SELECT * FROM alllist WHERE checktime is NULL')
        results = self._c.fetchall()
        return(self.__filldataset(results))

    def getwinlist(self):
        self._c.execute('SELECT * FROM alllist WHERE wintype is NOT NULL ')
        results = self._c.fetchall()
        return(self.__filldataset(results))

    def delalllist(self):
        try:
            self._c.execute('DELETE FROM alllist')
            self._conn.commit()
        except:
            return False
        else:
            return True

    def cleancheckinlabel(self):
        try:
            self._c.execute('UPDATE alllist SET checktime = NULL ')
            self._conn.commit()
        except:
            return False
        else:
            return True

    def cleanwintypelabel(self):
        try:
            self._c.execute('UPDATE alllist SET wintype = NULL ')
            self._conn.commit()
        except:
            return False
        else:
            return True

    def __filldataset(self, results):
        dd = DbData.sinfo
        dds = []
        for row in results:
            dd = dd.copy()
            dd['sid'] = row[0]
            dd['name'] = row[1]
            dd['class'] = row[2]
            dd['checktime'] = row[3]
            dd['wintype'] = row[4]
            dds.append(dd)
        return(dds)

    def getwininfo(self):
        try:
            self._c.execute('SELECT * FROM alllist WHERE checktime is NOT NULL and wintype is null')
            results = self._c.fetchall()
            dds = self.__filldataset(results)
        except:
            return None
        else:
            i = random.randint(0,len(dds)-1)
            wininfo = []
            wininfo.append(dds[i]['sid'])
            wininfo.append(dds[i]['name'])
            wininfo.append(dds[i]['class'])
            return(wininfo)

    def setwininfo(self, ltype, sid):
        try:
            self._c.execute('SELECT COUNT(sid) FROM alllist WHERE sid = \'' + sid + '\'')
            if self._c.fetchone()[0] > 0:
                self._c.execute('UPDATE alllist SET wintype = \'' + ltype + '\' WHERE sid = \'' + sid + '\'')
                self._conn.commit()
            else:
                return False
        except:
            return False
        else:
            return True

# db = DAllList()
# row = {'sid':'21420018',
#        'checktime':'20140820'}
# db.setwininfo('二等奖','21420042')
# cl = db.getwininfo()
# print(cl)