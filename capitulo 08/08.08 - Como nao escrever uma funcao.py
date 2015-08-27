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
# Arquivo: capitulo 08\08.08 - Como nao escrever uma funcao.py
##############################################################################





def soma(L):
     total = 0
     x = 0
     while x < 5:
         total += L[x]
         x+=1
     return total
L = [1,7,2,9,15]
print(soma(L))
print(soma([7,9,12,3,100,20,4]))
