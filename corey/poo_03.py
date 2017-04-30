# unicode:utf-8
import datetime

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@ffvi.com'.format(self.first, self.last)

    # decorator property proporciona que se use o methodo como uma propriedade da classe
    @property
    def fullname(self):
        """Retorna o nome separado por espaço, Ex "Locke Cole"""
        return '{} {}'.format(self.first, self.last)

    # decorator <nome_da_property>.setter transforma o metodo em setter, mas tem que ter o mesmo nome da property
    # no caso fullname
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last


emp_01 = Employee("Terra", "Banford")
emp_01.fullname = "Celes Chere"
print(emp_01.email)
print(emp_01.fullname)
emp_01.first = "Tina"
print(emp_01.email)
print(emp_01.fullname)


d = datetime.datetime.now()
print(datetime.datetime.strftime(d, "%Y"))
print(d.strftime("%Y-%m-%dT%H"))


