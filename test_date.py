#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import argparse


def valid_date(s):
    try:
        #datetime.datetime.strftime()
        return datetime.datetime.strptime(s, "%Y-%m-%d")
        print("b", type(s))
    except ValueError:
        print("a", type(s))
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)


parser = argparse.ArgumentParser(description="Teste Entradade Data")
parser.add_argument('-s', "--startdate", help="The Start Date - format YYYY-MM-DD ", required=True, type=valid_date)
args = parser.parse_args()

print(args.startdate)


d = datetime.datetime(2006, 12, 17, 10, 36, 0)

log_path = "/gfs-log/mail-box-mia/dovecot2/"


# pesquisa dos ultimos 7 dias
def pesquisa_sete_dias():
    d = datetime.datetime.now()
    for i in range(1, 168):
        d = d - datetime.timedelta(hours=1)

        if d.day < 10:
            dia = "0"+str(d.day)
        else:
            dia = str(d.day)

        if d.hour < 10:
            hora = "0"+str(d.hour)
        else:
            hora = str(d.hour)

        if d.month < 10:
            mes = "0" + str(d.month)
        else:
            mes = str(d.month)

        log = ""
        try:
            with open(log_path+"dovecot2.log."+str(d.year)+"-"+mes+"-"+dia+"T"+hora+":00+00:00", 'r') as log:
                print(log)
        except IOError:
            print("Aqui eu podia gerar uma linha de log\n não tem o arquivo:" + str(log))

pesquisa_sete_dias()
