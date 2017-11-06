__author__ = 'sledg_000'
from backup_file import BackupFile

class BackupDir(BackupFile):
    dirToBackup=""
    def __init__(self, dirToBackup):
        self.dirToBackup=dirToBackup

    def checkDirOk(self):
        pass

