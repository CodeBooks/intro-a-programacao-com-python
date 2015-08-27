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
# Arquivo: capitulo 06\06.15 - Adicao de elementos a lista.py
##############################################################################





L = []
while True:
     n = int(input("Digite um número (0 sai):"))
     if n == 0:
         break
     L.append(n)
x = 0
while x < len(L):
     print(L[x])
     x = x + 1
