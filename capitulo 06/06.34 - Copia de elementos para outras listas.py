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
# Arquivo: capitulo 06\06.34 - Copia de elementos para outras listas.py
##############################################################################





V = [9,8,7,12,0,13,21]
P = []
I = []
for e in V:
     if e % 2 == 0:
         P.append(e)
     else:
         I.append(e)
print("Pares: ", P)
print("Impares: ", I)
