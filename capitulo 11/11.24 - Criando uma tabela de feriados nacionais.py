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
# Arquivo: capitulo 11\11.24 - Criando uma tabela de feriados nacionais.py
##############################################################################

import sqlite3

feriados = [["2014-01-01", "Confraternização Universal"], ["2014-04-21", "Tiradentes"], ["2014-05-01", "Dia do trabalhador"], ["2014-09-07", "Independência"], ["2014-10-12", "Padroeira do Brasil"], ["2014-11-02", "Finados"], ["2014-11-15", "Proclamação da República"], ["2014-12-25", "Natal"] ]
with sqlite3.connect("brasil.db") as conexão:
	conexão.execute("create table feriados(id integer primary key autoincrement, data date, descrição text)")
	conexão.executemany("insert into feriados(data,descrição) values (?,?)", feriados)



