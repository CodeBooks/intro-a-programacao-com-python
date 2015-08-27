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
# Arquivo: capitulo 09\09.21 - Obtencao de mais informacoes sobre o arquivo.py
##############################################################################





import os
import os.path
import time
import sys
nome = sys.argv[1]
print("Nome: %s" % nome)
print("Tamanho: %d" % os.path.getsize(nome))
print("Criado: %s" % time.ctime(os.path.getctime(nome)))
print("Modificado: %s" % time.ctime(os.path.getmtime(nome)))
print("Acessado: %s" % time.ctime(os.path.getatime(nome)))
