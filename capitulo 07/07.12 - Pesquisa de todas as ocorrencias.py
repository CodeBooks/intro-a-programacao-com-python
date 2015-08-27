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
# Arquivo: capitulo 07\07.12 - Pesquisa de todas as ocorrencias.py
##############################################################################





s = "um tigre, dois tigres, três tigres"
p = 0
while(p>-1):
     p = s.find("tigre", p)
     if p >= 0:
         print("Posição: %d" % p)
         p += 1
