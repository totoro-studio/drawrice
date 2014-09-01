__author__ = 'Tony'

from PyQt5 import QtCore, QtGui, QtWidgets

from UiCleanDialog import *
from DataBase import *
from DataTxtOpt import *

class BusiCleanDialog(QtWidgets.QDialog, Ui_CleanDialog):
    result = []

    def initcleandialog(self):
        self.setFixedSize(205,179)
        self.setWindowIcon(QtGui.QIcon('.\\res\drawrice.png'))

    def beginclean(self):
        cs = self.getcheckstate()
        da = DAllList()
        result = []
        self.result = []
        result.append({'000': self.__nullfunc,
                       '100': da.delalllist,
                       '010': da.cleancheckinlabel,
                       '001': da.cleanwintypelabel}.get(cs[0:3])())
        result.append({'0':self.__nullfunc,
                       '1':FileOpt().clearalltxtfile}.get(cs[3])())

        self.result = result
        self.done(0)

    def setbutton(self):
        if self.getcheckstate() != '0000':
            self.pushButton_clean.setText('开始清理')
        else:
            self.pushButton_clean.setText('退出')

    def getcheckstate(self):
        css = []
        css.append(str(int(self.checkBox_cleanall.isChecked())))
        css.append(str(int(self.checkBox_cleancheckin.isChecked())))
        css.append(str(int(self.checkBox_cleanwin.isChecked())))
        css.append(str(int(self.checkBox_directory.isChecked())))
        return ''.join(css)

    def closeEvent(self, QCloseEvent):
        self.result = []
        self.result.append(None)
        self.result.append(None)
        self.done(0)

    def __nullfunc(self):
        pass
