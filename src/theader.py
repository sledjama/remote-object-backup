__author__ = 'sledg_000'


from PyQt4 import QtCore
class Threader(QtCore.QThread):
    def __init__(self,fileToUpload, uploaderFactory):
        QtCore.QThread.__init__(self)
        self.uploaderFactory=uploaderFactory

    def __del__(self):
        self.wait()

    def run(self):
        pass
