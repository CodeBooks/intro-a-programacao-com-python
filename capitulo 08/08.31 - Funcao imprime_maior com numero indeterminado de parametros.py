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
# Arquivo: capitulo 08\08.31 - Funcao imprime_maior com numero indeterminado de parametros.py
##############################################################################





def imprime_maior(mensagem, *numeros):
     maior = None
     for e in numeros:
         if maior == None or maior < e:
               maior = e
     print(mensagem, maior)
imprime_maior("Maior:",5,4,3,1)
imprime_maior("Max:", *[1,7,9])
