# unicode:utf-8


class Employee:

    # metodo construtor, usamos o self como primeiro parametro para receber a
    # propria instancia do objeto
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    # metodo de instancia, recebe o objeto recebido no parametro self,
    # como padrão isso não muda.
    # usa os atributos do objeto para funções.
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

emp_01 = Employee("Jonatan", "Vianna", 5000)
emp_02 = Employee("Ale", "Kopi", 5000)


print(emp_01.email)
print(emp_01.full_name())

