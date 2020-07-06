class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'olá {self.nome} sua idade é {self.idade} anos'


if __name__ == '__main__':

    nome = input("Insira seu nome: ")
    idade = input("insira sua idade: ")

    p = Pessoa(nome,idade)
    print(p.cumprimentar())

