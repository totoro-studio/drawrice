__author__ = 'Tony'

from PyQt5 import QtCore, QtGui, QtWidgets

from UiProgressDialog import *
from DataCsvOpt import *
from DataBase import *
from DataTxtOpt import *

class ImportProgressThread(QtCore.QThread):
    trigger = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(ImportProgressThread, self).__init__(parent)

    def setup(self, filename, importtype):
        self.filename = filename
        self.importtype = importtype

    def run(self):
        n = 0
        db = DAllList()
        if self.importtype == 'alllist':
            for row in CsvOpt().csvread(self.filename)[1:]:
                self.trigger.emit('正在导入 ' + row['sid'] + ' ' + row['name'] + '  ...')
                if db.insertbaseinfo(row): n +=1
        else:
            for row in CheckinTxtOpt(self.filename).checkinread():
                self.trigger.emit('正在导入 ' + row['sid'] + '  ...')
                if db.insertcheckininfo(row): n += 1

        self.trigger.emit('导入完成！共计导入 ' + str(n) + ' 条记录。')

class BusiProgressDialog(QtWidgets.QDialog, Ui_ProgressDialog):
    def startimportthread(self, filename, imtype):
        self.pushButton.setDisabled(True)

        self.imthread = ImportProgressThread(self)
        self.imthread.setTerminationEnabled(True)
        self.imthread.setup(filename, imtype)
        self.imthread.trigger.connect(self.displayprogress)
        self.imthread.finished.connect(self.setbutton)
        self.imthread.start()

    def displayprogress(self,str):
        self.label.setText(str)

    def setbutton(self):
        self.pushButton.setDisabled(False)

    def exitimport(self):
        self.imthread.terminate()
        self.done(1)


