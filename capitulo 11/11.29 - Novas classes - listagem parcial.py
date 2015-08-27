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
# Arquivo: capitulo 11\11.29 - Novas classes - listagem parcial.py
##############################################################################

class DBListaÚnica(ListaÚnica):
    def __init__(self, elem_class):
        super().__init__(elem_class)
        self.apagados = []

    def remove(self, elem):
        if elem.id is not None:
            self.apagados.append(elem.id)
        super().remove(elem)

    def limpa(self):
        self.apagados = []

class DBNome(Nome):
    def __init__(self, nome, id_=None):
        super().__init__(nome)
        self.id = id_

class DBTipoTelefone(TipoTelefone):
    def __init__(self, id_, tipo):
        super().__init__(tipo)
        self.id = id_

class DBTelefone(Telefone):
    def __init__(self, número, tipo=None, id_=None, id_nome=None):
        super().__init__(número, tipo)
        self.id = id_
        self.id_nome = id_nome

class DBTelefones(DBListaÚnica):
    def __init__(self):
        super().__init__(DBTelefone)

class DBTiposTelefone(ListaÚnica):
    def __init__(self):
        super().__init__(DBTipoTelefone)

class DBDadoAgenda:
    def __init__(self, nome):
        self.nome = nome
        self.telefones = DBTelefones()

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if type(valor)!=DBNome:
            raise TypeError("nome deve ser uma instância da classe DBNome")
        self.__nome = valor

    def pesquisaTelefone(self, telefone):
        posição = self.telefones.pesquisa(DBTelefone(telefone))
        if posição == -1:
            return None
        else:
            return self.telefones[posição]
