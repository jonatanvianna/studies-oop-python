#!/usr/bin/env python
# coding: utf-8
import datetime
import argparse



class User:
    def __init__(self, username, id_perm, brand, domain):
        self.username = username
        self.id_perm = id_perm
        self.brand = brand
        self.domain = domain

    @property
    def email(self):
        return '{}@{}'.format(self.username, self.domain)

    @classmethod
    def validate_id_perm(cls, id_perm):
        # faz ssh no bridge pra validar o id_perm completo, brand e username
        ssh = id_perm
        return cls("ronnie_james_dio", "666777666#perm!terraus", "terraus", "terra.com")

    def __str__(self):
        return "User: {}\n" \
               "IDperm: {}\n" \
               "Brand: {}\n" \
               "Domain: {}\n" \
               "Email: {}".format(u.username, u.id_perm, u.brand, u.domain, u.email)


class Searcher:
    # Essa classe pode "juntar" user e logs
    def __init__(self, user, log):
        self.user = user
        self.log = log

    @staticmethod
    def calc_date_range_in_hours(init_date, final_date):
        # ADICIONAR VALIDAÇÃO PRA NÃO SETAR UMA DATA POSTERIOR A DATA DE EXECUÇÃO
        # ADICIONAR VALIDAÇÃO DE DATA NÃO NEGATIVA
        return int(((final_date - init_date).total_seconds() / 60) / 60)

    def id_perm_filter(self, log_files_list):
        try:
            with open("/tmp/"+str(self.user.username)+str(self.log.log_suffix), 'w') as f:
                for log_file in log_files_list:
                    try:
                        with open(log_file, 'r'):
                            for line in log_file:
                                if self.user.id_perm in line:
                                    f.write(line)
                    except IOError:
                        print("Arquivo não encontrado: " + log_file)
        except IOError:
            print("Arquivo não encontrado: " + log_file)


class FileLog:
    def __init__(self, log_path, date_range, log_suffix):
        self.log_path = log_path
        self.date_range = date_range
        self.log_suffix = log_suffix

    def build_date_for_log_file(self, final_date):

        d = final_date - datetime.timedelta(hours=self.date_range)

        list_log_to_search = []

        for i in range(0, self.date_range+1):
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

            d += datetime.timedelta(hours=1)

            list_log_to_search.append(
                self.log_path + str(d.year) + "-" + mes + "-" + dia + "T" + hora + ":00+00:00")

        return list_log_to_search


class MercuryFileLog(FileLog):
    MERCURY_PATH = "/gfs-log/mail-web-mia/mercury/mercury.log."
    LOG_SUFFIX = "_mercury.log"

    def __init__(self, date_range):
        super().__init__(MercuryFileLog.MERCURY_PATH, date_range, MercuryFileLog.LOG_SUFFIX)


class AtmailFileLog(FileLog):
    ATMAIL_PATH = "/gfs-log/mail-web-mia/atmail/atmail.log."
    LOG_SUFFIX = "_atmail.log"

    def __init__(self, date_range):
        super().__init__(AtmailFileLog.ATMAIL_PATH, date_range, AtmailFileLog.LOG_SUFFIX)


class Dovecot2FileLog(FileLog):
    DOVECOT2_PATH = "/gfs-log/mail-box-mia/docevot2/docevot2.log."
    LOG_SUFFIX = "_dovecot2.log"

    def __init__(self, date_range):
        super().__init__(Dovecot2FileLog.DOVECOT2_PATH, date_range, Dovecot2FileLog.LOG_SUFFIX)


if __name__ == '__main__':

    def valid_date(s):
        try:
            return datetime.datetime.strptime(s, "%Y-%m-%dT%H")
        except ValueError:
            msg = "Not a valid date: '{0}'.".format(s)
            raise argparse.ArgumentTypeError(msg)


    parser = argparse.ArgumentParser(description="Teste Entradade Data")
    parser.add_argument('-i', "--initialdate", help="The Initial Date - format YYYY-MM-DDTHH ", required=True, type=valid_date)
    parser.add_argument('-f', "--finaldate", help="The Final Date - format YYYY-MM-DDTHH ", required=True, type=valid_date)
    args = parser.parse_args()
    initial_date = args.initialdate
    final_date = args.finaldate

    u = User.validate_id_perm("666777666#perm!terraus")
    date_rng = Searcher.calc_date_range_in_hours(initial_date, final_date)

    m = MercuryFileLog(date_rng)
    a = AtmailFileLog(date_rng)
    d = Dovecot2FileLog(date_rng)

    sm = Searcher(u, m)
    sa = Searcher(u, a)
    sd = Searcher(u, d)

    lm = m.build_date_for_log_file(args.finaldate)
    la = a.build_date_for_log_file(args.finaldate)
    ld = d.build_date_for_log_file(args.finaldate)

    sm.id_perm_filter(lm)
    sa.id_perm_filter(la)
    sd.id_perm_filter(ld)


