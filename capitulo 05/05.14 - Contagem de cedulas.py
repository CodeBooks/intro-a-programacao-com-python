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
# Arquivo: capitulo 05\05.14 - Contagem de cedulas.py
##############################################################################





valor = int(input("Digite o valor a pagar:"))
cédulas = 0
atual = 50
apagar = valor
while True:
     if atual <= apagar:
         apagar -= atual
         cédulas += 1
     else:
         print("%d cédula(s) de R$%d" % (cédulas, atual))
         if apagar == 0:
               break
         if atual == 50:
               atual = 20
         elif atual == 20:
               atual = 10
         elif atual == 10:
               atual = 5
         elif atual == 5:
               atual = 1
         cédulas = 0
