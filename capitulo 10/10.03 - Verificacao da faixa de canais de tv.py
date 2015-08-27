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
# Arquivo: capitulo 10\10.03 - Verificacao da faixa de canais de tv.py
##############################################################################





class Televisão:
     def __init__(self, min, max):
         self.ligada = False
         self.canal = 2
         self.cmin = min
         self.cmax = max
     def muda_canal_para_baixo(self):
         if(self.canal-1 >= self.cmin):
               self.canal -= 1
     def muda_canal_para_cima(self):
         if(self.canal+1 <= self.cmax):
               self.canal += 1
tv=Televisão(1,99)
for x in range(0,120):
     tv.muda_canal_para_cima()
print(tv.canal)
for x in range(0,120):
     tv.muda_canal_para_baixo()
print(tv.canal)
