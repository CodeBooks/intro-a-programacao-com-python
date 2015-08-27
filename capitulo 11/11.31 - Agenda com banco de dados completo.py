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
# Arquivo: capitulo 11\11.31 - Agenda com banco de dados completo.py
##############################################################################

import sys
import sqlite3
import os.path
from functools import total_ordering

BANCO = """
create table tipos(id integer primary key autoincrement,
                   descrição text);
create table nomes(id integer primary key autoincrement,
                   nome text);
create table telefones(id integer primary key autoincrement,
                   id_nome integer,
                   número text,
                   id_tipo integer);
insert into tipos(descrição) values ("Celular");
insert into tipos(descrição) values ("Fixo");
insert into tipos(descrição) values ("Fax");
insert into tipos(descrição) values ("Casa");
insert into tipos(descrição) values ("Trabalho");
"""


def nulo_ou_vazio(texto):
    return texto == None or not texto.strip()

def valida_faixa_inteiro(pergunta, inicio, fim, padrão = None):
    while True:
        try:
            entrada = input(pergunta)
            if nulo_ou_vazio(entrada) and padrão != None:
                entrada = padrão
            valor = int(entrada)
            if inicio <= valor <= fim:
                return(valor)
        except ValueError:
            print("Valor inválido, favor digitar entre %d e %d" %
                 (inicio, fim))


def valida_faixa_inteiro_ou_branco(pergunta, inicio, fim):
    while True:
        try:
            entrada = input(pergunta)
            if nulo_ou_vazio(entrada):
                return None
            valor = int(entrada)
            if inicio <= valor <= fim:
                return(valor)
        except ValueError:
            print("Valor inválido, favor digitar entre %d e %d" %
                 (inicio, fim))

class ListaÚnica:
    def __init__(self, elem_class):
        self.lista = []
        self.elem_class = elem_class

    def __len__(self):
        return len(self.lista)

    def __iter__(self):
        return iter(self.lista)

    def __getitem__(self, p):
        return self.lista[p]

    def indiceVálido(self, i):
        return i>=0 and i<len(self.lista)

    def adiciona(self, elem):
        if self.pesquisa(elem) == -1:
            self.lista.append(elem)

    def remove(self, elem):
        self.lista.remove(elem)

    def pesquisa(self, elem):
        self.verifica_tipo(elem)
        try:
            return self.lista.index(elem)
        except ValueError:
            return -1

    def verifica_tipo(self, elem):
        if type(elem)!=self.elem_class:
            raise TypeError("Tipo inválido")

    def ordena(self, chave = None):
        self.lista.sort(key= chave)

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


@total_ordering
class Nome:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

    def __repr__(self):
        return "<Classe {3} em 0x{0:x} Nome: {1} Chave: {2}>".format(
                id(self), self.__nome, self.__chave,
                type(self).__name__)

    def __eq__(self, outro):
        return self.nome == outro.nome

    def __lt__(self, outro):
        return self.nome < outro.nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if nulo_ou_vazio(valor):
            raise ValueError("Nome não pode ser nulo nem em branco")
        self.__nome = valor
        self.__chave = Nome.CriaChave(valor)

    @property
    def chave(self):
        return self.__chave

    @staticmethod
    def CriaChave(nome):
        return nome.strip().lower()

class DBNome(Nome):
    def __init__(self, nome, id_=None):
        super().__init__(nome)
        self.id = id_

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

class DBTipoTelefone(TipoTelefone):
    def __init__(self, id_, tipo):
        super().__init__(tipo)
        self.id = id_


class Telefone:
    def __init__(self, número, tipo=None):
        self.número = número
        self.tipo = tipo

    def __str__(self):
        if self.tipo!=None:
           tipo = self.tipo
        else:
            tipo = ""
        return "{0} {1}".format(self.número, tipo)

    def __eq__(self, outro):
        return self.número == outro.número and (
               (self.tipo == outro.tipo) or (
                self.tipo == None or outro.tipo == None))

    @property
    def número(self):
        return self.__número

    @número.setter
    def número(self, valor):
        if  nulo_ou_vazio(valor):
            raise ValueError("Número não pode ser None ou em branco")
        self.__número = valor

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

class DBAgenda:
    def __init__(self, banco):
        self.tiposTelefone = DBTiposTelefone()
        self.banco = banco
        novo = not os.path.isfile(banco)
        self.conexão = sqlite3.connect(banco)
        self.conexão.row_factory = sqlite3.Row
        if novo:
            self.cria_banco()
        self.carregaTipos()

    def carregaTipos(self):
        for tipo in self.conexão.execute("select * from tipos"):
            id_ = tipo["id"]
            descrição = tipo["descrição"]
            self.tiposTelefone.adiciona(DBTipoTelefone(id_, descrição))

    def cria_banco(self):
        self.conexão.executescript(BANCO)

    def pesquisaNome(self, nome):
        if not isinstance(nome, DBNome):
            raise TypeError("nome deve ser do tipo DBNome")
        achado = self.conexão.execute("""select count(*)
                                         from nomes where nome = ?""",
                                         (nome.nome,)).fetchone()
        if(achado[0]>0):
            return self.carrega_por_nome(nome)
        else:
            return None

    def carrega_por_id(self, id):
        consulta = self.conexão.execute(
                "select * from nomes where id = ?", (id,))
        return carrega(consulta.fetchone())

    def carrega_por_nome(self, nome):
        consulta = self.conexão.execute(
                "select * from nomes where nome = ?", (nome.nome,))
        return self.carrega(consulta.fetchone())

    def carrega(self, consulta):
        if consulta is None:
            return None
        novo = DBDadoAgenda(DBNome(consulta["nome"], consulta["id"]))
        for telefone in self.conexão.execute(
            "select * from telefones where id_nome = ?",
            (novo.nome.id,)):
            ntel = DBTelefone(telefone["número"], None,
                              telefone["id"], telefone["id_nome"])
            for tipo in self.tiposTelefone:
                if tipo.id == telefone["id_tipo"]:
                    ntel.tipo = tipo
                    break
            novo.telefones.adiciona(ntel)
        return novo

    def lista(self):
        consulta = self.conexão.execute(
                "select * from nomes order by nome")
        for registro in consulta:
            yield self.carrega(registro)

    def novo(self, registro):
        try:
            cur = self.conexão.cursor()
            cur.execute("insert into nomes(nome) values (?)",
                         (str(registro.nome),))
            registro.nome.id = cur.lastrowid
            for telefone in registro.telefones:
                cur.execute("""insert into telefones(número,
                               id_tipo, id_nome) values (?,?,?)""",
                            (telefone.número, telefone.tipo.id,
                             registro.nome.id))
                telefone.id = cur.lastrowid
            self.conexão.commit()
        except:
            self.conexão.rollback()
            raise
        finally:
            cur.close()

    def atualiza(self, registro):
        try:
            cur = self.conexão.cursor()
            cur.execute("update nomes set nome=? where id = ?",
                (str(registro.nome), registro.nome.id))
            for telefone in registro.telefones:
                if telefone.id is None:
                    cur.execute("""insert into telefones(número,
                                   id_tipo, id_nome)
                                   values (?,?,?)""",
                            (telefone.número, telefone.tipo.id,
                            registro.nome.id))
                    telefone.id = cur.lastrowid
                else:
                    cur.execute("""update telefones set número=?,
                                          id_tipo=?, id_nome=?
                                          where id = ?""",
                            (telefone.número, telefone.tipo.id,
                            registro.nome.id, telefone.id))
            for apagado in registro.telefones.apagados:
                cur.execute("delete from telefones where id = ?",
                            (apagado,))
            self.conexão.commit()
            registro.telefones.limpa()
        except:
            self.conexão.rollback()
            raise
        finally:
            cur.close()

    def apaga(self, registro):
        try:
            cur = self.conexão.cursor()
            cur.execute("delete from telefones where id_nome = ?",
                            (registro.nome.id,))
            cur.execute("delete from nomes where id = ?",
                         (registro.nome.id,))
            self.conexão.commit()
        except:
            self.conexão.rollback()
            raise
        finally:
            cur.close()

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

class AppAgenda:

    @staticmethod
    def pede_nome():
         return(input("Nome: "))

    @staticmethod
    def pede_telefone():
         return(input("Telefone: "))

    @staticmethod
    def mostra_dados(dados):
        print("Nome: %s" % dados.nome)
        for telefone in dados.telefones:
            print("Telefone: %s" % telefone)
        print()

    @staticmethod
    def mostra_dados_telefone(dados):
        print("Nome: %s" % dados.nome)
        for i, telefone in enumerate(dados.telefones):
           print("{0} - Telefone: {1}".format(i, telefone))
        print()

    def __init__(self, banco):
        self.agenda = DBAgenda(banco)
        self.menu = Menu()
        self.menu.adicionaopção("Novo", self.novo)
        self.menu.adicionaopção("Altera", self.altera)
        self.menu.adicionaopção("Apaga", self.apaga)
        self.menu.adicionaopção("Lista", self.lista)
        self.ultimo_nome = None

    def pede_tipo_telefone(self, padrão = None):
        for i,tipo in enumerate(self.agenda.tiposTelefone):
            print(" {0} - {1} ".format(i,tipo),end=None)
        t = valida_faixa_inteiro("Tipo: ",0,
            len(self.agenda.tiposTelefone)-1, padrão)
        return self.agenda.tiposTelefone[t]

    def pesquisa(self, nome):
        if type(nome)==str:
            nome = DBNome(nome)
        dado = self.agenda.pesquisaNome(nome)
        return dado

    def novo(self):
        novo = AppAgenda.pede_nome()
        if nulo_ou_vazio(novo):
            return
        nome = DBNome(novo)
        if self.pesquisa(nome) != None:
            print("Nome já existe!")
            return
        registro = DBDadoAgenda(nome)
        self.menu_telefones(registro)
        self.agenda.novo(registro)

    def apaga(self):
        nome = AppAgenda.pede_nome()
        if(nulo_ou_vazio(nome)):
           return
        p = self.pesquisa(nome)
        if p != None:
            self.agenda.apaga(p)
        else:
            print("Nome não encontrado.")

    def altera(self):
        nome = AppAgenda.pede_nome()
        if(nulo_ou_vazio(nome)):
           return
        p = self.pesquisa(nome)
        if p != None:
            print("\nEncontrado:\n")
            AppAgenda.mostra_dados(p)
            print("Digite enter caso não queira alterar o nome")
            novo = AppAgenda.pede_nome()
            if not nulo_ou_vazio(novo):
                p.nome.nome = novo
            self.menu_telefones(p)
            self.agenda.atualiza(p)
        else:
            print("Nome não encontrado!")

    def menu_telefones(self, dados):
        while True:
            print("\nEditando telefones\n")
            AppAgenda.mostra_dados_telefone(dados)
            if(len(dados.telefones)>0):
                print("\n[A] - alterar\n[D] - apagar\n", end="")
            print("[N] - novo\n[S] - sair\n")
            operação = input("Escolha uma operação: ")
            operação = operação.lower()
            if operação not in ["a","d","n", "s"]:
                print("Operação inválida. Digite A, D, N ou S")
                continue
            if operação == 'a' and len(dados.telefones)>0:
                self.altera_telefones(dados)
            elif operação == 'd' and len(dados.telefones)>0:
                self.apaga_telefone(dados)
            elif operação == 'n':
                self.novo_telefone(dados)
            elif operação == "s":
                break

    def novo_telefone(self, dados):
        telefone = AppAgenda.pede_telefone()
        if nulo_ou_vazio(telefone):
            return
        if dados.pesquisaTelefone(telefone) != None:
            print("Telefone já existe")
        tipo = self.pede_tipo_telefone()
        dados.telefones.adiciona(DBTelefone(telefone, tipo))

    def apaga_telefone(self, dados):
        t = valida_faixa_inteiro_ou_branco(
            "Digite a poisção do número a apagar, enter para sair: ",
            0, len(dados.telefones)-1)
        if t == None:
            return
        dados.telefones.remove(dados.telefones[t])

    def altera_telefones(self,dados):
        t = valida_faixa_inteiro_ou_branco(
            "Digite a poisção do número a alterar, enter para sair: ",
            0, len(dados.telefones)-1)
        if t == None:
            return
        telefone = dados.telefones[t]
        print("Telefone: %s" % telefone)
        print("Digite enter caso não queira alterar o número")
        novotelefone = AppAgenda.pede_telefone()
        if not nulo_ou_vazio(novotelefone):
            telefone.número = novotelefone
        print("Digite enter caso não queira alterar o tipo")
        telefone.tipo = self.pede_tipo_telefone(
            self.agenda.tiposTelefone.pesquisa(telefone.tipo))

    def lista(self):
        print("\nAgenda")
        print("-"*60)
        for e in self.agenda.lista():
            AppAgenda.mostra_dados(e)
        print("-"*60)

    def execute(self):
        self.menu.execute()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        app = AppAgenda(sys.argv[1])
        app.execute()
    else:
        print("Erro: nome do banco de dados não informado")
        print("      agenda.py nome_do_banco")

