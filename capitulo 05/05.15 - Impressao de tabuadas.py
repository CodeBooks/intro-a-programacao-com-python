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
# Arquivo: capitulo 05\05.15 - Impressao de tabuadas.py
##############################################################################





tabuada = 1
while tabuada <= 10:
     número = 1
     while número <= 10:
         print("%d x %d = %d" % (tabuada, número, tabuada * número))
         número += 1
     tabuada += 1
