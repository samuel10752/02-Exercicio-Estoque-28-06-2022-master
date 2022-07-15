from class_estoque import*
from class_historico import*

class Compras:
    def __init__(self):
<<<<<<< HEAD
        self.entrada = Estoque()
        self.historico = Historico()
    def comprar(self):
        entrada = input('Cod do Produto:  ')
        for i in range(len(self.entrada.listaProdutos)):
            if entrada == self.entrada.listaProdutos[i].cod:
                x=int(input('Quantidade comprada:  '))
                self.entrada.listaProdutos[i].quantidade += int(x)
                self.historico.transacoes.append(f'Compra de {x} unidades do produto: {self.entrada.listaProdutos[i].nome}')
                break
    def extrato(self):
        print(self.historico.compras_vendas()) 
=======
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
        comando_sql2 = f'update  Compra_venda set estoque = (select final where id = {cod}) where id = {cod};'
        comando_sql3 = f'update  Produtos set quantidade = (select final from Compra_venda where id = {cod}) where id = {cod};'
        self.meu_cursor.execute(comando_sql) 
        self.conexao.commit()
        self.meu_cursor.execute(comando_sql1) 
        self.conexao.commit()
        self.meu_cursor.execute(comando_sql2) 
        self.conexao.commit()
        self.meu_cursor.execute(comando_sql3) 
        self.conexao.commit()
>>>>>>> 32385a3ca798767ecbf36497e3a2825dfb52b362
