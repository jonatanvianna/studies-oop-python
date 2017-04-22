# unicode:utf-8


class Employee:
    """Classe Base para todos os tipos de employees do sistema"""
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

    # Metodo de instancia, SEMPRE recebe o objeto no parametro 'self' como padrão isso não muda.
    # dentro do metodo, pode usar atributos de classe por meio do 'self.'
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    # sobrescreve o raise_amt de Employee, se eu usar o Developer.apply_raise() ele aumenta 10% ao inves de 4%
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    # Não passamos parametros mutaveis como listas ou dicionarios no caso de employees passamos None.
    # Corey tem mais videos sobre isso.
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.full_name())

# Instancias de Developer, que herdam de Employee
dev_1 = Developer('Jonatan', 'Kopichenko', 60000, 'Python')
dev_2 = Developer('Ale', 'Kopichenko', 80000, 'Java')
dev_3 = Developer('Cyan', 'Garamond', 80000, 'C')
mgr_01 = Manager('Celes', 'Chere', 100000, [dev_2])


def uso_de_subclasse_01():
    print(mgr_01.email)
    mgr_01.add_emp(dev_1)
    mgr_01.add_emp(dev_3)
    mgr_01.print_emps()


def uso_de_subclasse_02():
    print(dev_1.email)
    print(dev_1.prog_lang)
    print(dev_1.pay)
    dev_1.apply_raise()
    print(dev_1.pay)


def uso_metodo_help():
    # Metodo help imprime informações sobre a classe que precisamos.
    # Nela tem  ordem de resolução de métodos que é a ordem em que o python ve os metodos da classe em questão.
    print(help(Developer))
    print(help(Employee))
    print(help(Manager))


def uso_de_built_in_methods():
    # isinstance verifica se
    print(isinstance(mgr_01, Employee))
    print(issubclass(Developer, Manager))


# uso_metodo_help()
# uso_de_subclasse_01()
# uso_de_subclasse_01()
# uso_de_built_in_methods()
