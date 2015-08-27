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
# Arquivo: capitulo 10\10.02 - Adicao de metodos para mudar o canal.py
##############################################################################





class Televisão:
     def __init__(self):
           self.ligada = False
           self.canal = 2
     def muda_canal_para_baixo(self):
           self.canal -= 1
     def muda_canal_para_cima(self):
           self.canal += 1

tv = Televisão()
tv.muda_canal_para_cima()
tv.muda_canal_para_cima()
tv.canal
tv.muda_canal_para_baixo()
tv.canal
