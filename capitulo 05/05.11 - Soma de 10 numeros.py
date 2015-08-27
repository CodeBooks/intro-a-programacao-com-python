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
# Arquivo: capitulo 05\05.11 - Soma de 10 numeros.py
##############################################################################





n = 1
soma = 0
while n <= 10:
     x = int(input("Digite o %d número:"%n))
     soma = soma + x
     n = n + 1
print("Soma: %d"%soma)
