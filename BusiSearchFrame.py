__author__ = 'Tony'

from PyQt5 import QtCore, QtGui, QtWidgets

from DataBase import *
from UiSearchForm import *
from DataTxtOpt import *

class BusiSearchFrame(QtWidgets.QFrame, Ui_SearchForm):
    __searchds =[]

    def initframe(self):
        self.setFixedSize(559, 336)
        self.setWindowIcon(QtGui.QIcon('.\\res\drawrice.png'))
        self.setWindowFlags(QtCore.Qt.Dialog)
        self.inittablewidget()

    def inittablewidget(self):
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['学号','姓名','班级','签到','奖项'])
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.tableWidget.setColumnWidth(0,70)
        self.tableWidget.setColumnWidth(1,70)
        self.tableWidget.setColumnWidth(2,70)
        self.tableWidget.setColumnWidth(3,120)
        self.tableWidget.setColumnWidth(4,70)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)  #设置表格单选模式
        self.tableWidget.horizontalHeader().setSectionResizeMode(0,2)   #固定表头宽度，第一列
        self.tableWidget.horizontalHeader().setSectionResizeMode(1,2)   #固定表头宽度，第二列
        self.tableWidget.horizontalHeader().setSectionResizeMode(2,2)   #固定表头宽度，第一列
        self.tableWidget.horizontalHeader().setSectionResizeMode(3,2)   #固定表头宽度，第二列
        self.tableWidget.horizontalHeader().setSectionResizeMode(4,2)   #固定表头宽度，第一列
        self.tableWidget.setAlternatingRowColors(True)

    def checkclick(self):
        if self.checkBox_ischeckin.isChecked() or self.checkBox_isnotcheckin.isChecked():
            self.checkBox_iswin.setChecked(False)
        self.listcheck()

    def iswinclick(self):
        if self.checkBox_iswin.isChecked():
            self.checkBox_ischeckin.setChecked(False)
            self.checkBox_isnotcheckin.setChecked(False)
        self.listcheck()

    def listcheck(self):
        bls = []
        bls.append(str(int(self.checkBox_ischeckin.isChecked())))
        bls.append(str(int(self.checkBox_isnotcheckin.isChecked())))
        bls.append(str(int(self.checkBox_iswin.isChecked())))
        self.filltablewidget(''.join(bls))

    def filltablewidget(self, searchtype):
        self.cleartablewidget() #更新表格前，先把表格清空

        dl = DAllList()
        self.__searchds = {'000': self.__nullfunc,
                           '100': dl.getcheckinlist,
                           '010': dl.getnotcheckinlist,
                           '110': dl.getalllist,
                           '001': dl.getwinlist}.get(searchtype)()

        for row in self.__searchds:
            self.tableWidget.insertRow(0)
            newitem = QtWidgets.QTableWidgetItem(row['sid'])
            self.tableWidget.setItem(0,0,newitem)

            newitem = QtWidgets.QTableWidgetItem(row['name'])
            self.tableWidget.setItem(0,1,newitem)

            newitem = QtWidgets.QTableWidgetItem(row['class'])
            self.tableWidget.setItem(0,2,newitem)

            newitem = QtWidgets.QTableWidgetItem(row['checktime'])
            self.tableWidget.setItem(0,3,newitem)

            newitem = QtWidgets.QTableWidgetItem(row['wintype'])
            self.tableWidget.setItem(0,4,newitem)

        self.label_sum.setText('共计：' + str(len(self.__searchds)) + ' 人')

    def cleartablewidget(self):
        for row in range(self.tableWidget.rowCount()):
            self.tableWidget.removeRow(0)

    def exportlist(self):
        if len(self.__searchds) == 0:
            QtWidgets.QMessageBox.information(self,'提示','没有需要导出的记录。')
        else:
            if self.checkBox_iswin.isChecked():
                n = WinListTxtOpt().exportwinlist(self.__searchds)
            else:
                n = ListTxtOpt().exportlist(self.__searchds)
            QtWidgets.QMessageBox.information(self, '提示', '成功导出 '+ str(n) + ' 条记录, 导出文件在 “\exportfile” 目录下。')

    def __nullfunc(self):
        return []