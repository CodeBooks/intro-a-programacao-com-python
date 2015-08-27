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
# Arquivo: capitulo 10\10.22 - Listagem parcial da agenda - classe menu.py
##############################################################################


class Menu:
    def __init__(self):
        self.opções = [ ["Sair", None] ]

    def adicionaopção(self, nome, função):
        self.opções.append([nome, função])

    def exibe(self):
        print("====")
        print("Menu")
        print("====\n")
        for i, opção in enumerate(self.opções):
            print("[{0}] - {1}".format(i, opção[0]))
        print()

    def execute(self):
        while True:
            self.exibe()
            escolha = valida_faixa_inteiro("Escolha uma opção: ",
                         0, len(self.opções)-1)
            if escolha == 0:
                break
            self.opções[escolha][1]()
