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
# Arquivo: capitulo 04\04.08 - Categoria x preco usando elif.py
##############################################################################





categoria = int(input("Digite a categoria do produto:"))
if categoria == 1:
     preço = 10
elif categoria == 2:
     preço = 18
elif categoria == 3:
     preço = 23
elif categoria == 4:
     preço = 26
elif categoria == 5:
     preço = 31
else:
     print("Categoria inválida, digite um valor entre 1 e 5!")
     preço = 0
print("O preço do produto é: R$%6.2f" % preço)
