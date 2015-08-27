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
# Arquivo: capitulo 08\08.12 - Funcao modificada para facilitar o rastreamento.py
##############################################################################





def fatorial(n):
     print("Calculando o fatorial de %d" % n)
     if n==0 or n == 1:
         print("Fatorial de %d = 1" % n)
         return 1
     else:
         fat = n * fatorial(n-1)
         print(" fatorial de %d = %d" % (n, fat) )
     return fat
fatorial(4)
