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
# Arquivo: capitulo 10\10.21 - Listagem parcial do programa agenda.py
##############################################################################


class TiposTelefone(ListaÚnica):
    def __init__(self):
        super().__init__(TipoTelefone)

class Agenda(ListaÚnica):
    def __init__(self):
        super().__init__(DadoAgenda)
        self.tiposTelefone = TiposTelefone()

    def adicionaTipo(self, tipo):
        self.tiposTelefone.adiciona(TipoTelefone(tipo))

    def pesquisaNome(self, nome):
        if type(nome) == str:
            nome = Nome(nome)
        for dados in self.lista:
            if dados.nome == nome:
                return dados
        else:
            return None

    def ordena(self):
        super().ordena(lambda dado: str(dado.nome))
