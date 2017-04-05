# coding: utf-8

class Exemplo():
    # Variavel de Classe, este atributo é compartilhado entre todas as instancias da classe Exemplo.
    lista_de_exemplos = ["jonatan", "vianna", "da", "Silva"]

    # exemplo de metodo de instancia
    # ele tem acesso as variaveis de instancia
    def metodo_instancia_exemplo(self):
        print(self.teste_exemplo)

    # exemplo de metodo de Classe
    @classmethod
    def metodo_de_classe_exemplo(cls):
        cls.lista_de_exemplos.append("Kopichenko")

    # metodo estatico não recebe nenhum parametro default como self ou cls
    @staticmethod
    def metodo_esatico_exemplo():
        pass

    # metodo construtor para criação de instancias
    # esse metodo __init__ é executado toda a vez que uma instancia de Exemplo é criada.
    ## TODO
    def __init__(self, teste_exemplo):
        self.teste_exemplo = teste_exemplo

        # construtor vazio
        # para o construtor vazio precisa declarar o construtor vazio ou é default?
        # def __init__(self):
        # pass


e1 = Exemplo("Ale")
Exemplo.metodo_de_classe_exemplo()
print(e1.lista_de_exemplos)