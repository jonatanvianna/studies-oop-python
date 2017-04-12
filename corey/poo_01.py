# unicode:utf-8


class Employee:
    """ metodo construtor, usamos o self como primeiro parametro para receber a
        propria instancia do objeto, também podem ser passados outros parametros """
    # Variavel de Classe
    # disponivel não somente para instancias, mas pode ser usada usando Employee.raise_amount
    # E como uma variavel static no Java
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def full_name(self):
        """
            metodo de instancia, SEMPRE recebe o objeto no parametro 'self' como padrão isso não muda.
            dentro do metodo, pode usar atributos de classe por meio do 'self.'
        """
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_01 = Employee("Jonatan", "Vianna", 5000)
emp_02 = Employee("Ale", "Kopi", 5000)

# print(emp_01.full_name()) # passa automaticamente a instancia da classe
# print(Employee.full_name(emp_02)) se usarmos o caminho 'absoluto da classe' temos que passar a instacia explicitamente


def uso_da_variavel_de_classe_01():
    # imprime o salario
    print(emp_02.pay)

    # usa o metodo que aumenta o salario
    emp_02.apply_raise()

    # aqui já com o aumento
    print(emp_02.pay)

    # imprime o valor atual da variavel da classe
    print(Employee.raise_amount)

    # imprime o namespace da instancia emp02, a qual não tem a variavel raise_amount
    print(emp_02.__dict__)

    # seta na instancia a variavel raise_amount com o valor 1.06
    emp_02.raise_amount = 1.06

    # imprime o namespace da instancia emp02, que agora tem a sua variavel de instancia raise_amount
    print(emp_02.__dict__)

    # imprime o namespace da classe Employee com a variavel de classe raise_amount
    print(Employee.__dict__)

uso_da_variavel_de_classe_01()



