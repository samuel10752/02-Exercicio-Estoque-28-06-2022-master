import mysql.connector
from class_historico import *
from class_produto import *

class Compra:

    def __init__(self):
        self.conexao = mysql.connector.connect(
            host= 'localhost',
            user= 'root',
            password= 'q1w2e3',
            database='estoque'
        )

        self.meu_cursor = self.conexao.cursor()
    
    def compra(self,cod,value,atributo):
        comando_sql = f'update Compra_venda set {atributo} = "{value}" where id = {cod} '
        comando_sql1 = f'update  Compra_venda set final = (select (estoque + compra) where id = {cod}) where id = {cod};'
        comando_sql2 = f'update  Compra_venda set estoque = (select final where id = {cod}) where cod = {cod};'
        comando_sql3 = f'update  Produtos set quantidade = (select final from Compra_venda where id = {cod}) where id = {cod};'
        self.meu_cursor.execute(comando_sql) 
        self.conexao.commit()
        self.meu_cursor.execute(comando_sql1) 
        self.conexao.commit()
        self.meu_cursor.execute(comando_sql2) 
        self.conexao.commit()
        self.meu_cursor.execute(comando_sql3) 
        self.conexao.commit()