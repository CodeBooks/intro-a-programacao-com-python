##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2014
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Primeira reimpressão - Outubro/2011
# Segunda reimpressão - Novembro/1012
# Terceira reimpressão - Agosto/2013
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Site: http://python.nilo.pro.br/
# 
# Arquivo: capitulo 10\10.15 - Usando anotacoes.py
##############################################################################


from functools import total_ordering

@total_ordering
class Nome:
    def __init__(self, nome):
        if nome == None or not nome.strip():
            raise ValueError("Nome não pode ser nulo nem em branco")
        self.nome = nome
        self.chave = Nome.CriaChave(nome)

    def __str__(self):
        return self.nome

    def __repr__(self):
        return "<Classe {3} em 0x{0:x} Nome: {1} Chave: {2}>".format(id(self), self.nome, self.chave, type(self).__name__)

    def __eq__(self, outro):
        print("eq Chamado")
        return self.nome == outro.nome

    def __lt__(self, outro):
        print("lt Chamado")
        return self.nome < outro.nome

    @staticmethod
    def CriaChave(nome):
        return nome.strip().lower()


