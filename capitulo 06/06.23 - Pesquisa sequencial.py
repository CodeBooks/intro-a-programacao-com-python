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
# Arquivo: capitulo 06\06.23 - Pesquisa sequencial.py
##############################################################################





L = [15,7,27,39]
p = int(input("Digite o valor a procurar:"))
achou = False
x = 0
while x < len(L):
     if L[x] == p:
         achou = True
         break
     x += 1
if achou:
     print("%d achado na posição %d" % (p,x))
else:
     print("%d não encontrado" % p)
