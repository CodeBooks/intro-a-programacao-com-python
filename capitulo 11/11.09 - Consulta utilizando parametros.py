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
# Arquivo: capitulo 11\11.09 - Consulta utilizando parametros.py
##############################################################################


import sqlite3

nome=input("Nome a selecionar: ")
conexão = sqlite3.connect("agenda.db")
cursor = conexão.cursor()
cursor.execute('select * from agenda where nome = ?', (nome,))
x=0
while True:
    resultado=cursor.fetchone()
    if resultado == None:
    	if x == 0:
    		print("Nada encontrado.")
    	break
    print("Nome: %s\nTelefone: %s" % (resultado))
    x+=1
cursor.close()
conexão.close()
