from class_estoque_db import*
from class_historico import*
import mysql.connector

#class Compras:
#    def __init__(self):
#        self.entrada = DBEstoque()
#        self.historico = Historico()
#    def comprar(self):
#        entrada = input('Cod do Produto:  ')
#        for i in range(len(self.entrada.listaProdutos)):
#            if entrada == self.entrada.listaProdutos[i].cod:
#                x=int(input('Quantidade comprada:  '))
#                self.entrada.listaProdutos[i].quantidade += int(x)
#                self.historico.transacoes.append(f'Compra de {x} unidades do produto:', self.entrada.listaProdutos[i].nome)
#    def extrato(self):
#        print(self.historico.compras_vendas())



class Compras(): 

    def __init__(self, cod, quantidade):
        self.cod = cod
        self.quantidade = quantidade

class DBCompras:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='q1w2e3',
            database='estoque'
        )
        self.meu_cursor = self.conexao.cursor()

    def comprar(self, cod ,quantidade):
        obj_compra = Compras(cod, quantidade)
        comando_sql = f'insert into Compras (quantidade) value ("{obj_compra.quantidade}")'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()     

    def compra_extrato(self):       
        comando_sql = f'select * from Compras'
        self.meu_cursor.execute(comando_sql)
        lista = self.meu_cursor.fetchall()
        for quantidade in lista:
            print("Seu extrato foi de ",quantidade, 'Reais')
