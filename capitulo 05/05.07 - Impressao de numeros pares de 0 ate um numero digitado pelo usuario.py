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
# Arquivo: capitulo 05\05.07 - Impressao de numeros pares de 0 ate um numero digitado pelo usuario.py
##############################################################################





fim = int(input("Digite o último número a imprimir:"))
x = 0
while x <= fim:
     if x % 2 == 0:
         print(x)
     x = x + 1
