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
# Arquivo: capitulo 11\11.30 - Listagem parcial - classe DBAgenda.py
##############################################################################

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
