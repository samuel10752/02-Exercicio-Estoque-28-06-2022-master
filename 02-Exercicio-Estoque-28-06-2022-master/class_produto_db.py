import mysql.connector
from class_produto import *

class DBProduto:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='q1w2e3',
            database='estoque'
        )
        self.meu_cursor = self.conexao.cursor()

    def salva_produtos(self, cod, nome, fabricante, quantidade):
        obj_contato = Produto(cod,nome, fabricante, quantidade)
        comando_sql = f'insert into Produtos(nome, fabricante, quantidade)value ("{obj_contato.nome}", "{obj_contato.fabricante}", "{obj_contato.quantidade}")'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

    def lista_produtos(self):
        comando_sql = f'select * from Produtos'
        self.meu_cursor.execute(comando_sql)
        lista = self.meu_cursor.fetchall()
        for i in lista:
            print(i)

    def alterar_produtos(self,atributo, valor, cod):
        comando_sql = f'update Produtos set {atributo} = "{valor}" where id = {cod}'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

    def excluir_produto(self,cod):
        comando_sql = f'delete from Produtos where id = "{cod}"'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()