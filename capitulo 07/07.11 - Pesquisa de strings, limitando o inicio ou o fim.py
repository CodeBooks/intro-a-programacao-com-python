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
# Arquivo: capitulo 07\07.11 - Pesquisa de strings, limitando o inicio ou o fim.py
##############################################################################





s = "um tigre, dois tigres, três tigres"
s.find("tigres")
s.rfind("tigres")
s.find("tigres",7) #início=7
s.find("tigres",30) #início=30
s.find("tigres",0,10) #início=0 fim=10
