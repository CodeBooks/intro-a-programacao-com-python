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
# Arquivo: capitulo 08\08.16 - Validacao de inteiro usando funcao.py
##############################################################################





def faixa_int(pergunta, mínimo, máximo):
     while True:
         v = int(input(pergunta))
         if v < mínimo or v > máximo:
               print("Valor inválido. Digite um valor entre %d e %d" % (mínimo,máximo))
         else:
              return v
