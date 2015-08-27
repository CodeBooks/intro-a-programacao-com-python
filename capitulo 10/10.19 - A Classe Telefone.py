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
# Arquivo: capitulo 10\10.19 - A Classe Telefone.py
##############################################################################


class Telefone:
    def __init__(self, número, tipo=None):
        self.número = número
        self.tipo = tipo

    def __str__(self):
        if self.tipo!=None:
           tipo = self.tipo
        else:
            tipo = ""
        return "{0} {1}".format(self.número, tipo)

    def __eq__(self, outro):
        return self.número == outro.número and (
               (self.tipo == outro.tipo) or (
                self.tipo == None or outro.tipo == None))

    @property
    def número(self):
        return self.__número

    @número.setter
    def número(self, valor):
        if  valor == None or not valor.strip():
            raise ValueError("Número não pode ser None ou em branco")
        self.__número = valor
