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
# Arquivo: capitulo 06\06.35 - Controle da utilizacao de salas de um cinema.py
##############################################################################





lugares_vagos = [10,2,1,3,0]
while True:
     sala = int(input("Sala (0 sai): "))
     if sala == 0:
         print("Fim")
         break
     if sala > len(lugares_vagos) or sala < 1:
         print("Sala inválida")
     elif lugares_vagos[sala-1] == 0:
         print("Desculpe, sala lotada!")
     else:
         lugares = int(input("Quantos lugares você deseja (%d vagos):" % lugares_vagos[sala-1]))
         if lugares > lugares_vagos[sala-1]:
               print("Esse número de lugares não está disponível.")
         elif lugares < 0:
               print("Número inválido")
         else:
               lugares_vagos[sala-1] -= lugares
               print("%d lugares vendidos" % lugares)
print("Utilização das salas")
for x,l in enumerate(lugares_vagos):
     print("Sala %d - %d lugar(es) vazio(s)" % (x+1, l))
