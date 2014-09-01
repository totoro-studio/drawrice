__author__ = 'Tony'

import sys, operator, time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

from DataCsvOpt import *
from DataBase import *
from SysConfig import *
from LotteryOpt import *

from UiMainForm import *
from UiSearchForm import *
from BusiProgressDialog import *
from BusiSearchFrame import *
from BusiCleanDialog import *
from DrawLotteryView import DrawLotteryView


class BusiMainFrame(QtWidgets.QFrame, Ui_MainForm):
    def initmainframe(self):
        '''初始化frame，包括各控件的初始化'''
        try:
            self.setFixedSize(504, 387)
            self.setWindowIcon(QtGui.QIcon('.\\res\drawrice.png'))
            self.initqueuetablewedgit()

            wt = SysConfig().getlotterytype()
            self.comboBox_WinType.addItems(wt)
            self.refreshwinnumber()

            self.currentlocal = 0   #指示当前的抽奖序列位置，已抽过的序列会被锁定
        except:
            return False

    def initqueuetablewedgit(self):
        '''初始化tableview'''
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(['奖项', '数量'])
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)  # 设置表格不可编辑
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)  # 设置表格行选择模式
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)  # 设置表格单选模式
        self.tableWidget.setColumnWidth(0, 101)
        self.tableWidget.setColumnWidth(1, 72)
        self.tableWidget.verticalHeader().setVisible(False)  # 侧边表头隐藏
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, 2)  # 固定表头宽度，第一列
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, 2)  # 固定表头宽度，第二列
        self.tableWidget.setHorizontalScrollBarPolicy(1)  # 关闭水平滚动
        self.tableWidget.setAlternatingRowColors(True)  # 设置表格颜色交替

    def addqueue(self):
        '''响应新增序列按钮，在全局抽奖序列lq中新增一个条目，同时刷新tableview'''
        lq = {'ltype': self.comboBox_WinType.currentText(),
              'number': self.comboBox_number.currentText()}

        # 当新增的中奖人数加上已增加的中奖人数之后小于参与抽奖的总人数，才充许继续增加
        if int(lq['number']) + self.getwincount() <= DAllList().getvalidnumber():
            i = self.tableWidget.rowCount()
            #当新加入的序列与上一个序列奖项一致时，则只增加该奖项的数量
            if i > 0 and self.getqueue(i - 1)['ltype'] == lq['ltype'] and i-1 >= self.currentlocal :
            # if i > 0 and self.getqueue(i - 1)['ltype'] == lq['ltype']:
                n = int(self.getqueue(i - 1)['number']) + int(lq['number'])
                item = QtWidgets.QTableWidgetItem(str(n))
                item.setTextAlignment(0x0004 | 0x0080)
                self.tableWidget.setItem(i - 1, 1, item)
            else:  #当新加入的序列与上一个序列不一致时，则直接在序列尾新增一项
                self.tableWidget.insertRow(i)
                item = QtWidgets.QTableWidgetItem(lq['ltype'])
                item.setTextAlignment(0x0004 | 0x0080)
                self.tableWidget.setItem(i, 0, item)

                item = QtWidgets.QTableWidgetItem(lq['number'])
                item.setTextAlignment(0x0004 | 0x0080)
                self.tableWidget.setItem(i, 1, item)
        else:
            QtWidgets.QMessageBox.information(self, '提示', '您打算新增的中奖人数已超过有效的参与抽奖总人数，请重新选择！')

        self.refreshalllabel()

    def getqueue(self, n):
        if n < 0:
            return None
        else:
            lq = {'ltype': self.tableWidget.item(n, 0).data(0),
                  'number': self.tableWidget.item(n, 1).data(0)}
            return lq

    def getcurrentqueue(self):
        if self.currentlocal < self.tableWidget.rowCount():
            self.lockqueuerow(self.currentlocal)
            lq = {'ltype': self.tableWidget.item(self.currentlocal, 0).data(0),
                  'number': self.tableWidget.item(self.currentlocal, 1).data(0)}
            self.currentlocal += 1
        else:
            lq = None
        return lq

    def getallqueues(self):
        '''获取抽奖序列列表，根据tablewidget中的列表进行重复项合并，并按数量从小到大进行排序'''

        '''获取tablewidget中所有的抽奖序列'''
        lqs = []
        for i in range(self.tableWidget.rowCount()):
            lq = {'ltype': self.tableWidget.item(i, 0).data(0),
                  'number': int(self.tableWidget.item(i, 1).data(0))}
            lqs.append(lq)
            lq = lq.copy()

        # nlqs = sorted(lqs, key=lambda x:x['number'])
        '''对抽奖序列进行重复合并,重新建立一个无重复项的抽奖序列nlqs'''
        if lqs != []:
            nlqs = []
            nlqs.append(lqs[0])
            for lq in lqs[1:]:
                i = 0
                n = len(nlqs)
                flag = True
                for i in range(n):
                    if nlqs[i]['ltype'] == lq['ltype']:
                        nlqs[i]['number'] = nlqs[i]['number'] + lq['number']
                        flag = False
                        break
                        # i += 1
                    else:
                        i += 1
                if flag:    nlqs.append(lq)

            '''对合并后的抽奖序列进行排序，按数量从小到大进行排列'''
            lqs = sorted(nlqs, key=operator.itemgetter('number'))
        return lqs

    def delqueue(self):
        '''响应删除单项序列按钮'''
        i = self.tableWidget.currentIndex().row()  # 获取选择行
        if i <= self.currentlocal-1:
            QtWidgets.QMessageBox.information(self, '提示', '该序列已被锁定，不允许删除！')
        else:
            if i >= 0:
                self.tableWidget.removeRow(i)
                # 检查删除行的下一行和上一行是否为同一抽奖类型，如果为相同抽奖类型，则合并条目
                if i > 0 and i <= self.tableWidget.rowCount() - 1:
                    if self.getqueue(i - 1)['ltype'] == self.getqueue(i)['ltype'] and i > self.currentlocal:
                        n = int(self.getqueue(i - 1)['number']) + int(self.getqueue(i)['number'])
                        item = QtWidgets.QTableWidgetItem(str(n))
                        item.setTextAlignment(0x0004 | 0x0080)
                        self.tableWidget.setItem(i - 1, 1, item)
                        self.tableWidget.removeRow(i)

            self.refreshalllabel()

    def clearqueue(self):
        '''响应清空序列按钮，清空tableview'''
        for i in range(self.tableWidget.rowCount()):
            self.tableWidget.removeRow(0)
        self.refreshalllabel()
        self.currentlocal = 0

    def refreshwinnumber(self):
        '''刷新数量combo控件的列表'''
        self.comboBox_number.clear()
        self.comboBox_number.addItems(self.getcurrentwinnumberlist())

    def getcurrentwinnumberlist(self):
        '''根据当前的奖项combo中的奖项类别，从xml中获取该奖项对应的最大数量，生成从1到最大数量的str列表'''
        s = []
        for i in range(int(SysConfig().getlotterymaxnumber(self.comboBox_WinType.currentText()))):
            s.append(str(i + 1))
        return s

    def importall(self):
        '''导入所有人员清单，CSV格式'''
        try:
            fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Select a CSV file', './importfile/', 'CSV Files(*.csv)')
            self.importthread(fileName[0], 'alllist')
        except:
            QtWidgets.QMessageBox.information(self, '提示', '输入文件格式不正确，或编码不正确！')

    def importcheckin(self):
        '''导入签到人员清单，TXT格式'''
        try:
            fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Select a Checkin file', './importfile/', 'txt Files(*.txt)')
            self.importthread(fileName[0], 'checkin')

            self.label_statistic1.setText('参与抽奖的总人数为：' + str(DAllList().getcheckinnumber()) + ' 人')
        except:
            QtWidgets.QMessageBox.information(self, '提示', '输入文件格式不正确，或编码不正确！')

    def importthread(self, filename, imtype):
        '''弹出导入窗口，同时支持导入所有人员清单和签到人员清单'''
        if filename != '':
            bpd = BusiProgressDialog()
            bpd.setupUi(bpd)
            bpd.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
            bpd.setFixedSize(300,70)
            bpd.startimportthread(filename, imtype)
            bpd.exec_()

    def clean(self):
        '''响应清除数据按钮'''
        bcd = BusiCleanDialog()
        bcd.setupUi(bcd)
        bcd.initcleandialog()
        bcd.exec_()

        if bcd.result != [None, None]:
            dbresult = {'None': '',
                        'True': '数据库清理成功！',
                        'False': '数据库清理失败，需要重新清理！'}.get(str(bcd.result[0]))
            fresult = {'None': '',
                       'True': '日志及导出文件清理成功！',
                       'False': '日志及导出文件清理失败，请手工清理！'}.get(str(bcd.result[1]))
            QtWidgets.QMessageBox.information(self, '提示', dbresult + '\n' + fresult)

        self.clearalllabel()

    def search(self):
        '''响应查找按钮'''
        self.sframe = BusiSearchFrame()
        self.sframe.setupUi(self.sframe)
        self.sframe.initframe()
        self.sframe.show()

    def clearalllabel(self):
        self.label_statistic1.setText('')
        self.label_statistic2.setText('')
        self.label_statistic3.setText('')
        self.label_statistic4.setText('')
        self.label_statistic5.setText('')
        self.label_statistic6.setText('')

    def getwincount(self):
        '''取得抽奖序列中中奖的总人数'''
        n = 0
        for i in range(self.tableWidget.rowCount()):
            n += int(self.tableWidget.item(i, 1).data(0))
        return n

    def refreshalllabel(self):
        '''刷新label列表的内容'''
        self.clearalllabel()

        # label1,显示参与抽奖的总人数
        totalsum = DAllList().getcheckinnumber()
        self.label_statistic1.setText('参与抽奖的总人数为：' + str(totalsum) + ' 人')

        #label2,显示将获奖的总人数
        lqs = self.getallqueues()
        if lqs != []:
            n = 0
            for lq in lqs:
                n += lq['number']
            rate = n * 100 / totalsum
            self.label_statistic2.setText('获奖总人数为：' + str(n) + ' 人，中奖比例为：%d%%' % rate)

            #label3~6,依次显示各奖项的获奖人数
            label = []
            label.append(self.label_statistic3)
            label.append(self.label_statistic4)
            label.append(self.label_statistic5)
            i = 0
            sum = 0
            for lq in lqs:
                if i <= 2:
                    label[i].setText('获得' + lq['ltype'] + '的人数为：' + str(lq['number']) + ' 人')
                else:
                    sum += lq['number']
                i += 1
            if sum > 0:
                self.label_statistic6.setText('获得剩余奖项的人数为：' + str(sum) + ' 人')

    def lockqueuerow(self, row):
        nitem = self.tableWidget.item(row, 0)
        nitem.setData(QtCore.Qt.TextColorRole, QColor(202, 202, 202))
        self.tableWidget.setItem(row, 0, nitem)
        nitem = self.tableWidget.item(row, 1)
        nitem.setData(QtCore.Qt.TextColorRole, QColor(202, 202, 202))
        self.tableWidget.setItem(row, 1, nitem)

    def drawlottery(self):
        '''响应抽奖按钮'''
        if self.tableWidget.rowCount() == 0 or self.currentlocal > self.tableWidget.rowCount()-1:
            QtWidgets.QMessageBox.information(self, '提示', '您的抽奖队列为空，请增加抽奖队列！')
        else:
            self.dlv = DrawLotteryView(self)
            self.dlv.show()

    def closeEvent(self, *args, **kwargs):
        if getattr(self, 'dlv', False) != False:
            self.dlv.web.close()
        if getattr(self,'sframe',False) != False:
            self.sframe.close()