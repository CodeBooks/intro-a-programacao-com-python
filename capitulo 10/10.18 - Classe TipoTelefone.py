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
# Arquivo: capitulo 10\10.18 - Classe TipoTelefone.py
##############################################################################


from functools import total_ordering

@total_ordering
class TipoTelefone:
    def __init__(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return "({0})".format(self.tipo)

    def __eq__(self, outro):
        if outro is None:
            return False
        return self.tipo == outro.tipo

    def __lt__(self, outro):
        return self.tipo < outro.tipo
