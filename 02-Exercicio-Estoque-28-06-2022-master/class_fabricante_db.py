import mysql.connector
from class_fabricante import *


class DBFabricante:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='q1w2e3',
            database='estoque'
        )
        self.meu_cursor = self.conexao.cursor()

    def salva_fabricante(self, cod, nome_fabricante):
        obj_contato = Fabricante(cod, nome_fabricante)
        comando_sql = f'insert into Fabricante(fabricante)value ("{obj_contato.nome_fabricante}")'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

    def lista_fabricante(self):
        comando_sql = f'select * from Fabricante'
        self.meu_cursor.execute(comando_sql)
        lista = self.meu_cursor.fetchall()
        for i in lista:
            print(i)

    def alterar_fabricante(self,atributo, valor, cod):
        comando_sql = f'update Fabricante set {atributo} = "{valor}" where id = {cod}'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

    def excluir_fabricante(self,cod):
        comando_sql = f'delete from Fabricante where id = "{cod}"'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()