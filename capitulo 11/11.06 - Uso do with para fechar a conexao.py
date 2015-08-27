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
# Arquivo: capitulo 11\11.06 - Uso do with para fechar a conexao.py
##############################################################################


import sqlite3
from contextlib import closing #<1>

with sqlite3.connect("agenda.db") as conexao:
	with closing(conexao.cursor()) as cursor:
		cursor.execute("select * from agenda")
		while True:
			resultado=cursor.fetchone() #<2>
			if resultado == None:
				break
			print("Nome: %s\nTelefone: %s" % (resultado))
