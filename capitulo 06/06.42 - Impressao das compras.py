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
# Arquivo: capitulo 06\06.42 - Impressao das compras.py
##############################################################################





produto1 = [ "maçã", 10, 0.30]
produto2 = [ "pêra",   5, 0.75]
produto3 = [ "kiwi",   4, 0.98]
compras = [ produto1, produto2, produto3]
for e in compras:
     print("Produto: %s" % e[0])
     print("Quantidade: %d" % e[1])
     print("Preço: %5.2f" % e[2])
