# To change this template, choose Tools | Templates
# and open the template in the editor.
version="0.1"
import sys, os, re
from PyQt4 import QtCore, QtGui



# This is only needed for Python v2 but is harmless for Python v3.
import sip
sip.setapi('QString', 2)

try:
     _fromUtf8= QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
    


class RemoteObjBackup(QtGui.QMainWindow):
    def __init__(self, parent=None):
        """this is called first
        """
        print("App started!")




    def alert(self,text):
        QtGui.QMessageBox.warning(self,"Remote Object Backup", str(text))





if __name__ == "__main__":

    RemoteObjBackup()



