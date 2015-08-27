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
# Arquivo: capitulo 11\11.01 - Exemplo de uso do SQLIte em Python.py
##############################################################################


import sqlite3

conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()
cursor.execute('''
        create table agenda(
            nome text,
            telefone text)
        ''')
cursor.execute('''
        insert into agenda (nome, telefone)
            values(?, ?)
            ''', ("Nilo", "7788-1432"))
conexao.commit()
cursor.close()
conexao.close()
