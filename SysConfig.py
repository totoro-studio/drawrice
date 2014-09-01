__author__ = 'Tony'

import xml.etree.ElementTree as ET

configfile = 'config.xml'

class SysConfig():

    __root = None

    def __init__(self):
        tree = ET.parse(configfile)
        self.__root = tree.getroot()

    def getdatabasefiename(self):
        try:
            for dbase in self.__root.findall('database'):
                return dbase.find('filename').text
        except:
            return None

    def getlotterytype(self):
        ltype = []
        try:
            lt = self.__root.find('lotterytype')
            for t in lt.findall('type'):
                ltype.append(t.get('name'))
            return ltype
        except:
            return None

    def getlotterymaxnumber(self,ltype):
        try:
            lt = self.__root.find('lotterytype')
            for t in lt.findall('type'):
                if t.get('name') == ltype:
                    return(t.find('maxnumber').text)
        except:
            return None

    def getlotterywindowspath(self):
        try:
            for dbase in self.__root.findall('lotterywindows'):
                return dbase.find('filepath').text
        except:
            return None

    def getprizeitempicandnote(self, ltype):
        try:
            pn = []
            lt = self.__root.find('lotterytype')
            for t in lt.findall('type'):
                if t.get('name') == ltype:
                    pn.append(t.find('pic').text)
                    pn.append(t.find('note').text)
            return(pn)
        except:
            return None

    def getfeasttitle(self):
        try:
            return self.__root.find('feasttitle').text
        except:
            return None

# sc = SysConfig()
# print(sc.getfeasttitle())