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
# Arquivo: capitulo 08\08.24 - Chamadando a funcao retangulo nomeando os argumentos.py
##############################################################################





def retângulo(largura, altura, caractere = "*"):
     linha = caractere * largura
     for i in range(altura):
         print(linha)

retângulo(3,4)
retângulo(largura=3, altura=4)
retângulo(altura=4, largura=3)
retângulo(caractere="-", altura=4, largura=3)
