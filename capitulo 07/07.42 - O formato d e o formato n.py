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
# Arquivo: capitulo 07\07.42 - O formato d e o formato n.py
##############################################################################





"{:d}".format(5678)
"{:n}".format(5678)
import locale
# Mac OS x e Linux, descomente a linha abaixo:
#locale.setlocale(locale.LC_ALL,"pt_BR.utf-8")
# Windows, descomente a linha abaixo:
#locale.setlocale(locale.LC_ALL,"Portuguese_Brazil")
"{:n}".format(5678)
