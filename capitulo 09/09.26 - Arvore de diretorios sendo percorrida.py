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
# Arquivo: capitulo 09\09.26 - Arvore de diretorios sendo percorrida.py
##############################################################################





import os
import sys
for raiz, diretorios, arquivos in os.walk(sys.argv[1]):
     print("\nCaminho:", raiz)
     for d in diretorios:
         print("   %s/" % d)
     for f in arquivos:
         print("   %s" % f)
     print("%d diretório(s), %d arquivo(s)" % (len(diretorios), len(arquivos)))
