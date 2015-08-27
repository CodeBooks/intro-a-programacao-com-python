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
# Arquivo: capitulo 11\11.17 - Consulta dos estados brasileiros ordenados por nome.py
##############################################################################


import sqlite3

conexão = sqlite3.connect("brasil.db")
conexão.row_factory = sqlite3.Row
print("%3s %-20s %12s" % ("Id","Estado","População"))
print("="*37)
for estado in conexão.execute("select * from estados order by nome"):
	print("%3d %-20s %12d" %
		  (estado["id"],
		   estado["nome"],
		   estado["população"]))
conexão.close()
