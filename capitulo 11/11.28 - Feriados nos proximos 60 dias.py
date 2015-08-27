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
# Arquivo: capitulo 11\11.28 - Feriados nos proximos 60 dias.py
##############################################################################

import sqlite3
import datetime

hoje = datetime.date.today()
hoje60dias = hoje + datetime.timedelta(days=60)

with sqlite3.connect("brasil.db",detect_types=sqlite3.PARSE_DECLTYPES) as conexão:
	conexão.row_factory = sqlite3.Row
	for feriado in conexão.execute("select * from feriados where data >= ? and data <= ?", (hoje, hoje60dias)):
		print("{0} {1}".format(feriado["data"].strftime("%d/%m"), feriado["descrição"]))


