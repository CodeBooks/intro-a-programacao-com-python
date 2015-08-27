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
# Arquivo: capitulo 11\11.20 - Agrupando e contando estados por regiao.py
##############################################################################

import sqlite3
print("Região Número de Estados")
print("====== =================")
with sqlite3.connect("brasil.db") as conexão:
	for região in conexão.execute("""
		select região, count(*)
		from estados
		group by região"""):
		print("{0:6} {1:17}".format(*região))

