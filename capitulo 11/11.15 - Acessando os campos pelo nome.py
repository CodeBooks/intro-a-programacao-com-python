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
# Arquivo: capitulo 11\11.15 - Acessando os campos pelo nome.py
##############################################################################


import sqlite3

conexão = sqlite3.connect("agenda.db")
conexão.row_factory = sqlite3.Row
cursor = conexão.cursor()
for registro in cursor.execute("select * from agenda"):
	print("Nome: %s\nTelefone: %s" % (registro["nome"], registro["telefone"]))
cursor.close()
conexão.close()
