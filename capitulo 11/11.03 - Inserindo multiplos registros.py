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
# Arquivo: capitulo 11\11.03 - Inserindo multiplos registros.py
##############################################################################


import sqlite3

dados =  [ ("João",  "98901-0109"),
           ("André", "98902-8900"),
           ("Maria", "97891-3321")]

conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()
cursor.executemany('''
	   insert into agenda (nome, telefone)
       values(?, ?)
            ''', dados)

conexao.commit()
cursor.close()
conexao.close()
