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
# Arquivo: capitulo 06\06.53 - Exemplo de dicionario com estoque e operacoes de venda.py
##############################################################################





estoque={ "tomate": [ 1000, 2.30],
          "alface": [   500, 0.45],
          "batata": [ 2001, 1.20],
          "feijão": [   100, 1.50] }
venda = [ ["tomate", 5], ["batata", 10], ["alface",5]]
total = 0
print("Vendas:\n")
for operação in venda:
     produto, quantidade = operação
     preço = estoque[produto][1]
     custo = preço * quantidade
     print("%12s: %3d x %6.2f = %6.2f" %
         (produto, quantidade,preço,custo))
     estoque[produto][0] -= quantidade
     total += custo
print(" Custo total: %21.2f\n" % total)
print("Estoque:\n")
for chave, dados in estoque.items():
     print("Descrição: ", chave)
     print("Quantidade: ", dados[0])
     print("Preço: %6.2f\n" % dados[1])
