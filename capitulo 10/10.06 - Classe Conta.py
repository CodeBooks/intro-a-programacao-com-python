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
# Arquivo: capitulo 10\10.06 - Classe Conta.py
##############################################################################





class Conta:
     def __init__(self, clientes, número, saldo = 0):
         self.saldo = saldo
         self.clientes = clientes
         self.número = número
     def resumo(self):
         print("CC Número: %s Saldo: %10.2f" %
               (self.número, self.saldo))
     def saque(self, valor):
         if self.saldo >= valor:
               self.saldo -= valor
     def deposito(self, valor):
         self.saldo += valor
