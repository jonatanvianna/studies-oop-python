#!/usr/bin/env python
# coding: utf-8
import datetime


class FileLog:
    def __init__(self, log_path):
        self.log_path = log_path

    def build_date(self, rng):
        d = datetime.datetime.now() - datetime.timedelta(hours=rng)
        list_log_to_search = []

        for i in range(0, rng):
            if d.day < 10:
                dia = "0" + str(d.day)
            else:
                dia = str(d.day)

            if d.hour < 10:
                hora = "0" + str(d.hour)
            else:
                hora = str(d.hour)

            if d.month < 10:
                mes = "0" + str(d.month)
            else:
                mes = str(d.month)

            d = d + datetime.timedelta(hours=1)

            list_log_to_search.append(
                self.log_path + str(d.year) + "-" + mes + "-" + dia + "T" + hora + ":00+00:00")

        return list_log_to_search


class MercuryFileLog(FileLog):
    MERCURY_PATH = "/gfs-log/mail-web-mia/mercury/mercury.log."

    def __init__(self):
        super().__init__(MercuryFileLog.MERCURY_PATH)


class AtmailFileLog(FileLog):
    ATMAIL_PATH = "/gfs-log/mail-web-mia/atmail/atmail.log."

    def __init__(self):
        super().__init__(AtmailFileLog.ATMAIL_PATH)

m = MercuryFileLog()
a = AtmailFileLog()

l = a.build_date(5)
l2 = m.build_date(6)

for i in l:
    print(i)

