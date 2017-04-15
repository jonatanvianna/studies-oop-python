# unicode:utf-8


class Employee:

    # Variavel de Classe
    # disponivel para uso de classes Ex: Employee.raise_amt
    # pode ser usar em instancias, bu is silly
    # É como uma variavel static no Java
    raise_amt = 1.04

    # metodo construtor, usamos o self como primeiro parametro para receber a
    # propria instancia do objeto, também podem ser passados outros parametros
    # somente um método __init__ pode ser usado na classe
    # como alternativa para outros contrutores podemos usar métodos de classe.
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def full_name(self):
        """ metodo de instancia, SEMPRE recebe o objeto no parametro 'self' como padrão isso não muda.
            dentro do metodo, pode usar atributos de classe por meio do 'self.'"""
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # metodo de classe, sempre recebe como primeiro parametro a classe ao inves da instancia
    # a variavel classe é por convenção a palavra 'cls'
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    # metodo de classe usado como construtor alternativo.
    # É como uma conveção, como não podemos usar mais de um metodo ___init___ temos a opção de usar
    # metodos de classe para diferentes assinaturas de metodo.
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # metodos estáticos não recebem nem classe nem instancia na assinatura do método.
    # podemos definir qualquer argumento
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# usando full_name()
def uso_do_instance_method_01():
    emp_01 = Employee("Jonatan", "Vianna", 5000)
    emp_02 = Employee("Ale", "Kopi", 5000)

    # passa automaticamente a instancia da classe
    print(emp_01.full_name())
    # se usarmos o caminho 'absoluto da classe' temos que passar a instacia explicitamente
    print(Employee.full_name(emp_02))


# usando raise_amt
def uso_da_variavel_de_classe_01():
    emp_01 = Employee("Jonatan", "Vianna", 5000)
    emp_02 = Employee("Ale", "Kopi", 5000)

    # imprime o salario
    print(emp_02.pay)

    # usa o metodo que aumenta o salario
    emp_02.apply_raise()

    # aqui já com o aumento
    print(emp_02.pay)

    # imprime o valor atual da variavel da classe
    print(Employee.raise_amt)

    # imprime o namespace da instancia emp02, a qual não tem a variavel raise_amt
    print(emp_02.__dict__)

    # seta na instancia a variavel raise_amt com o valor 1.06
    emp_02.raise_amt = 1.06

    # imprime o namespace da instancia emp02, que agora tem a sua variavel de instancia raise_amt
    print(emp_02.__dict__)

    # imprime o namespace da classe Employee com a variavel de classe raise_amt
    print(Employee.__dict__)


# usando set_raise_amt()
def uso_do_class_method_01():

    # instancia Employee
    emp_01 = Employee("Jonatan", "Vianna", 5000)
    # instancia Employee
    emp_02 = Employee("Ale", "Kopi", 5000)

    # imprime a variavel de classe raise_amt, da classe Employee
    print(Employee.raise_amt)

    # imprime a variavel de classe raise_amt, da classe Employee atraves da instancia
    print(emp_01.raise_amt)

    # imprime a variavel de classe raise_amt, da classe Employee atraves da instancia
    print(emp_02.raise_amt)

    # usa o metodo de classe set_raise_amt(), para mudar o valor da variavel de classe raise_amt
    # passa automaticamente a classe na chamada do método, é o 'cls'
    Employee.set_raise_amt(1.06)

    # imprime a variavel de classe raise_amt, da classe Employee
    print(Employee.raise_amt)

    # imprime a variavel de classe raise_amt, da classe Employee atraves da instancia
    print(emp_01.raise_amt)

    # imprime a variavel de classe raise_amt, da classe Employee atraves da instancia
    print(emp_02.raise_amt)


# usando from_string
def uso_do_class_method_02():
    # Tres strings com first,last e pay
    emp_str01 = 'Vicks-Vicky-5000'
    emp_str02 = 'Wedge-Edgy-6000'
    emp_str03 = 'Bicks-Back-7000'

    # usa o metodo de classe para criar novas instancias de Employee a partir de uma string previamente formatada.
    new_emp_01 = Employee.from_string(emp_str01)
    new_emp_02 = Employee.from_string(emp_str02)
    new_emp_03 = Employee.from_string(emp_str03)

    # imprime os atributos das tres instancias exemplo
    print('{} {}, {} : {}'.format(new_emp_01.first, new_emp_01.last, new_emp_01.pay, new_emp_01.email))
    print('{} {}, {}'.format(new_emp_02.first, new_emp_02.last, new_emp_02.pay))
    print('{} {}, {}'.format(new_emp_03.first, new_emp_03.last, new_emp_03.pay))


# usando is_workday()
def uso_do_satic_method_01():
    import datetime
    # seta a data na variavel
    my_date = datetime.date(2017, 7, 20)
    # imprime o retorno no metodo estatico is_workday() usando a data atual recebida atraves do metodo now()
    print(Employee.is_workday(datetime.datetime.now()))
    # imprime o retorno no metodo estatico is_workday() usando a variavel my_date setada anteriormente
    print(Employee.is_workday(my_date))



# uso_do_instance_method_01()
# uso_da_variavel_de_classe_01()
# uso_do_class_method_01()
# uso_do_class_method_02()


