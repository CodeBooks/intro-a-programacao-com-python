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
# Arquivo: capitulo 08\08.04 - Reutilizacao da funcao epar em outra funcao.py
##############################################################################





def épar(x):
     return(x % 2 == 0)
def par_ou_ímpar(x):
     if épar(x):
         return "par"
     else:
         return "ímpar"
print(par_ou_ímpar(4))
print(par_ou_ímpar(5))
