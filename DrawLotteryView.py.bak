__author__ = 'Tony'

#coding:utf-8

import sys
from os.path import dirname, join

from PyQt5.Qt import Qt
from PyQt5.QtCore import QUrl, QObject, pyqtSignal, pyqtSlot, QStateMachine, QState, QDir
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebKitWidgets import QWebView
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtWidgets import QTableWidget
from SysConfig import SysConfig
from DataBase import DAllList

class DrawLotteryView(QObject):
    def __init__(self, parent):
        super(DrawLotteryView, self).__init__()
        self.pwindow = parent   #获取父窗口指针

        self.states = QStateMachine()

        sinitinfo = QState()
        sltypeinfo = QState()
        sprizeinfo = QState()
        svnumberwindow = QState()
        sdrawlottery = QState()
        sfinal = QState()

        sinitinfo.addTransition(self.on_nextstep_event, sltypeinfo)
        sltypeinfo.addTransition(self.on_nextstep_event, sprizeinfo)
        sprizeinfo.addTransition(self.on_nextstep_event, svnumberwindow)
        svnumberwindow.addTransition(self.on_nextstep_event, sdrawlottery)
        sdrawlottery.addTransition(self.on_nextstep_event, sfinal)
        sfinal.addTransition(self.on_final_event, sinitinfo)

        sinitinfo.entered.connect(self.initinfo)
        sltypeinfo.entered.connect(self.viewltypeinfo)
        sprizeinfo.entered.connect(self.viewprizeinfo)
        svnumberwindow.entered.connect(self.viewnumberwindow)
        sdrawlottery.entered.connect(self.drawlottery)
        sfinal.entered.connect(self.final)

        self.states.addState(sinitinfo)
        self.states.addState(sltypeinfo)
        self.states.addState(sprizeinfo)
        self.states.addState(svnumberwindow)
        self.states.addState(sdrawlottery)
        self.states.addState(sfinal)
        self.states.setInitialState(sinitinfo)

        self.states.start()

    def show(self):
        #It is IMPERATIVE that all forward slashes are scrubbed out, otherwise QTWebKit seems to be
        # easily confused
        # kickOffHTML = 'file:///' + join(dirname(__file__).replace('\\', '/'), "www/test02.html").replace('\\', '/')
        # kickOffHTML = 'file:///' + join(dirname(__file__).replace('\\', '/'), "www/test02.html").replace('\\', '/')
        kickOffHTML = 'file:///' + QDir().absolutePath() + SysConfig().getlotterywindowspath() + 'test02.html'
        # kickOffHTML = 'http://get.webgl.org/'
        # kickOffHTML = 'http://www.airtightinteractive.com/demos/js/nebula/'

        #This is basically a browser instance
        # self.gweb = QGraphicsWebView()
        self.web = QWebView()
        self.web.setMinimumSize(1024,680)
        self.web.setWindowFlags(Qt.FramelessWindowHint) #无边框
        self.web.setContextMenuPolicy(0)    #关闭右键

        #Unlikely to matter but prefer to be waiting for callback then try to catch
        # it in time.
        self.web.loadFinished.connect(self.onLoad)
        self.web.load(QUrl(kickOffHTML))
        self.web.show()
        # self.scene = QGraphicsScene()
        # self.scene.addItem(self.gweb)
        # self.view = QGraphicsView()
        # self.view.setScene(self.scene)
        # self.view.show()

    def onLoad(self):
        #如果mywebinterface未初始化，则初始化mywebinterface
        # if getattr(self, "mywebinterface", False) == False:
        #     self.mywebinterface = WebInterface()

        #This is the body of a web browser tab
        self.myPage = self.web.page()
        self.myPage.settings().setAttribute(QWebSettings.DeveloperExtrasEnabled, True)
        self.myPage.settings().setAttribute(QWebSettings.JavascriptEnabled, True)
        self.myPage.settings().setAttribute(QWebSettings.WebGLEnabled, True)
        self.myPage.settings().setAttribute(QWebSettings.AcceleratedCompositingEnabled, True)

        #This is the actual context/frame a webpage is running in.
        # Other frames could include iframes or such.
        self.myFrame = self.myPage.mainFrame()
        # ATTENTION here's the magic that sets a bridge between Python to HTML
        self.myFrame.addToJavaScriptWindowObject("mywebinterface", self)
        #Tell the HTML side, we are open for business
        self.myFrame.evaluateJavaScript("ApplicationIsReady()")

    def initinfo(self):
        # print('initinfo')
        cltypes = self.pwindow.getcurrentqueue()
        if cltypes == None:
            self.isfinished = True
        else:
            self.isfinished = False
            self.currentltype = cltypes['ltype']
            self.currentnumber = cltypes['number'] #当前奖项需要抽取的数量
            self.drawcount = int(self.currentnumber)  #当前抽奖序列的人数，需要重复抽奖的次数
            self.isdrawing = False    #当前是否为抽奖状态

    @pyqtSlot()
    def nextstep(self):
        if self.isfinished:
            # print('close this window')
            self.on_message_event.emit('当前抽奖序列已抽取完毕！<br>按退出按钮退出！')
        else:
            if self.isdrawing and self.drawcount > 0:
                self.drawlottery()
            else:
                # print('nextstep')
                self.on_nextstep_event.emit()

    @pyqtSlot()
    def exitwindow(self):
        # print('exit window')
        self.web.close()

    def viewltypeinfo(self):
        # print('viewltypeinfo')
        self.on_viewltypeinfo_event.emit(self.currentltype, int(self.currentnumber))

    def viewprizeinfo(self):
        # print('return prizeinfo')
        ls = SysConfig().getprizeitempicandnote(self.currentltype)
        icon = ls[0]
        notes = ls[1]
        self.on_viewprizeinfo_event.emit(icon, notes)

    def viewnumberwindow(self):
        # print('return viewnumberwindow')
        self.on_viewnumberwindow_event.emit()

    def drawlottery(self):
        # print('return drawlottery')
        progress = str(int(self.currentnumber)-self.drawcount+1) + '/' + self.currentnumber
        self.on_viewprogress_event.emit(progress)
        try:
            dl = DAllList().getwininfo()
            sid = dl[0][2] + dl[0][5] + dl[0][6] + dl[0][7]
            name = dl[1]
            DAllList().setwininfo(self.currentltype,dl[0])
        except:
            sid = '0000'
            name = 'error, retry'
            self.drawcount = 0
            self.isdrawing = False
            self.on_drawlottery_event.emit(sid, name)
            pass
        self.on_drawlottery_event.emit(sid, name)
        self.drawcount -= 1
        if self.drawcount == 0:
            self.isdrawing = False
        else:
            self.isdrawing = True

    def final(self):
        print('final')
        self.on_final_event.emit()

    @pyqtSlot()
    def changesize(self):
        # print('changesize')
        if self.web.isFullScreen():
            self.web.showNormal()
        else:
            self.web.showFullScreen()

    on_nextstep_event = pyqtSignal()
    on_viewltypeinfo_event = pyqtSignal(str, int)
    on_viewprizeinfo_event = pyqtSignal(str, str)
    on_viewluckguyinfo_event = pyqtSignal(str, str)
    on_viewnumberwindow_event = pyqtSignal()
    on_drawlottery_event = pyqtSignal(str, str)
    on_final_event = pyqtSignal()
    on_message_event = pyqtSignal(str)
    on_viewprogress_event = pyqtSignal(str)


# app = QApplication(sys.argv)
#
# myWebApp = DrawLotteryView()
# myWebApp.show()
#
# exit(app.exec_())