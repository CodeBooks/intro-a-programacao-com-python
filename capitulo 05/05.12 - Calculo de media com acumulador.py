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
# Arquivo: capitulo 05\05.12 - Calculo de media com acumulador.py
##############################################################################





x = 1
soma = 0
while x <= 5:
     n = int(input("%d Digite o número:" % x))
     soma = soma + n
     x = x + 1
print("Média: %5.2f" % (soma/5))
