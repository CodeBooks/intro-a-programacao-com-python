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
# Arquivo: capitulo 08\08.30 - Funcao soma com numero indeterminado de parametros.py
##############################################################################





def soma(*args):
     s = 0
     for x in args:
         s += x
     return s
soma(1,2)
soma(2)
soma(5,6,7,8)
soma(9,10,20,30,40)
