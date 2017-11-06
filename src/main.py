# To change this template, choose Tools | Templates
# and open the template in the editor.

import sys, os, re
from PyQt4 import QtCore, QtGui
from _version import __version__
from backup_file import BackupFile
from backup_dir import BackupDir


# This is only needed for Python v2 but is harmless for Python v3.
import sip
sip.setapi('QString', 2)

try:
     _fromUtf8= QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


testFile=os.path.join("C:\\", "Users", "sledg_000", "Desktop", "whatsapp.txt")
testDir=os.path.join("C:\\", "Users", "sledg_000", "Desktop", "whatsapp")

sys.argv.append(testDir)

class RemoteObjBackup(QtGui.QDialog):
    def __init__(self, parent=None):
        """this is called first
        """
        QtGui.QDialog.__init__(self, parent) #this actually has no parent
        print("App started!")
        if len(sys.argv) >= 2:
            if os.path.isdir(sys.argv[1]):
                self.backupDirectory(sys.argv[1])
            elif os.path.isfile(sys.argv[1]):
                self.backupFile(sys.argv[1])
            else:
                pass




    def backupDirectory(self, directoryToBackup):
        BackupDir(directoryToBackup)

    def backupFile(self, fileToBackup):
        BackupFile(fileToBackup)


    def alert(self,text):
        QtGui.QMessageBox.warning(self,"Remote Object Backup", str(text))





if __name__ == "__main__":
    app=QtGui.QApplication(sys.argv)
    remoteBackup=RemoteObjBackup()
    remoteBackup.show()
    sys.exit(app.exec_())






