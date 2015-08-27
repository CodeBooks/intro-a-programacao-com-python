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
# Arquivo: capitulo 10\10.10 - Criando os objetos.py
##############################################################################





from clientes import Cliente
from bancos import Banco
from contas import Conta
joão = Cliente("João da Silva", "3241-5599")
maria = Cliente("Maria Silva", "7231-9955")
josé = Cliente("José Vargas","9721-3040")
contaJM = Conta( [joão, maria], 100)
contaJ = Conta( [josé], 10)
tatu = Banco("Tatú")
tatu.abre_conta(contaJM)
tatu.abre_conta(contaJ)
tatu.lista_contas()
