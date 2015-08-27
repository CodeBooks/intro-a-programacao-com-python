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
# Arquivo: capitulo 06\06.21 - Simulacao de uma fila de banco.py
##############################################################################





último = 10
fila = list(range(1,último+1))
while True:
     print("\nExistem %d clientes na fila" % len(fila))
     print("Fila atual:", fila)
     print("Digite F para adicionar um cliente ao fim da fila,")
     print("ou A para realizar o atendimento. S para sair.")
     operação = input("Operação (F, A ou S):")
     if operação == "A":
         if(len(fila))>0:
               atendido = fila.pop(0)
               print("Cliente %d atendido" % atendido)
         else:
               print("Fila vazia! Ninguém para atender.")
     elif operação == "F":
         último += 1 # Increnta o ticket do novo cliente
         fila.append(último)
     elif operação == "S":
         break
     else:
         print("Operação inválida! Digite apenas F, A ou S!")
