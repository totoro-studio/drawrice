from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from UiMainForm import *
from BusiMainFrame import *
from SysConfig import *

app = QtWidgets.QApplication(sys.argv)
mw = BusiMainFrame()
mw.setupUi(mw)
mw.setWindowFlags(QtCore.Qt.Dialog)
mw.show()
if mw.initmainframe() == False:
    QtWidgets.QMessageBox.critical(None, '出错提示','配置文件sysconfig.xml读取出错!')
    mw.close()
else:
    sys.exit(app.exec_())