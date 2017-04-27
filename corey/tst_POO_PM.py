#!/usr/bin/env python
# coding: utf-8


class FileLog:

    def __init__(self, path, filename):
        self.path = path
        self.filename = filename

    @property
    def full_logfile_path(self):
        return "{}{}".format(self.path, self.filename)

    def filtro_id_perm(self, id_perm):
        pass


class MercuryFileLog(FileLog):
    MERCURY_PATH = "/gfs-log/mail-web-mia/atmail/"

    def __init__(self, path, filename):
        super().__init__(path, filename)


f = MercuryFileLog(MercuryFileLog.MERCURY_PATH, "joe.txt")
print(f.full_logfile_path)
