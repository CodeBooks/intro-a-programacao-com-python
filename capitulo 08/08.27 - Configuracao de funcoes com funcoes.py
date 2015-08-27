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
# Arquivo: capitulo 08\08.27 - Configuracao de funcoes com funcoes.py
##############################################################################





def imprime_lista(L, fimpressão, fcondição):
     for e in L:
         if fcondição(e):
               fimpressão(e)
def imprime_elemento(e):
     print("Valor: %d" % e)
def épar(x):
     return x % 2 == 0
def éimpar(x):
     return not épar(x)
L = [1,7,9,2,11,0]
imprime_lista(L, imprime_elemento, épar)
imprime_lista(L, imprime_elemento, éimpar)
