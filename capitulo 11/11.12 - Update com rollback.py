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
# Arquivo: capitulo 11\11.12 - Update com rollback.py
##############################################################################


import sqlite3

conexão = sqlite3.connect("agenda.db")
cursor = conexão.cursor()
cursor.execute("""update agenda
	              set telefone = '12345-6789'
	              """)
print("Registros alterados: ", cursor.rowcount)
if cursor.rowcount == 1:
	conexão.commit()
	print("Alterações gravadas")
else:
	conexão.rollback()
	print("Alterações abortadas")
conexão.close()
