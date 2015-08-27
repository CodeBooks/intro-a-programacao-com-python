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
# Arquivo: capitulo 06\06.22 - Pilha de pratos.py
##############################################################################





prato = 5
pilha = list(range(1,prato+1))
while True:
       print("\nExistem %d pratos na pilha" % len(pilha))
       print("Pilha atual:", pilha)
       print("Digite E para empilhar um novo prato,")
       print("ou D para desempilhar. S para sair.")
       operação = input("Operação (E, D ou S):")
       if operação == "D":
               if(len(pilha)) > 0:
                       lavado = pilha.pop(-1)
                       print("Prato %d lavado" % lavado)
               else:
                       print("Pilha vazia! Nada para lavar.")
       elif operação == "E":
               prato += 1 # Novo prato
               pilha.append(prato)
       elif operação == "S":
               break
       else:
               print("Operação inválida! Digite apenas E, D ou S!")
