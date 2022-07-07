from class_estoque_db import *
from class_fabricante_db import *
from class_compras import *
from class_produto_db import *
from class_vendas import*

class Menu():
    def __init__(self):
        estoque = DBEstoque()
        produto = DBProduto()
        fabricante = DBFabricante()
        compra = DBCompras()
        venda = DBVendas()
        while True:
            entrada = input(('1 - Cadastrar Fabriante\n'
                             '2 - Listar Fabricante\n'
                             '3 - Cadastrar Produto\n'
                             '4 - Listar Produto\n'
                             '5 - Alterar Fabricante\n'
                             '6 - Alterar Prod.:\n'
                             '7 - Comprar:\n'
                             '8 - Vender\n'
                             '9 - Excluir Fabricante\n'
                             '10 - Excluir Produto\n'
                             '11 - Ver Compras\n'
                             '12 - Ver Vendas\n'
                             '0 - Sair\n: '))
            if entrada == '1':
                cod = None
                nome = input('Digite o nome: ')

                fabricante.salva_fabricante(cod, nome)

            elif entrada == '2':
                fabricante.lista_fabricante()

            #elif entrada == '3':
            #    cod = None
            #    fabricante.lista_fabricante()
            #    quantidade = int(input('Digite a quantidade:'))
            #    produto.salva_produto(cod,quantidade)

            elif entrada == '4':
                produto.lista_produto()

            elif entrada == '5':
                cod = int(input('Informe o código do Fabricante: '))
                valor= input('Entre com o novo nome: ')
                atributo = 'nome'
                fabricante.alterar_fabricante(atributo,valor,cod)

            elif entrada == '6':
                cod = int(input('Informe o código do Fabricante: '))
                valor= input('Entre com o novo nome: ')
                atributo = 'nome'
                produto.alterar_produto(atributo,valor,cod)

            elif entrada == '7':
                cod = None
                produto.lista_produto()
                cod = int(input('Informe o código do produto: '))
                quantidade = int(input('Quanto deseja comprar?'))

                compra.comprar(cod, quantidade)

            elif entrada == '8':

                produto.lista_produto()
                cod = int(input('Informe o código do produto: '))
                quantidade = int(input('Quanto deseja vender:'))

                venda.vendas(cod, quantidade)

            elif entrada == '9':
                cod = int(input('Informe o código do fabricante: '))
                fabricante.excluir_fabricante(cod)

            elif entrada == '10':
                cod = int(input('Informe o código do Produto: '))
                produto.excluir_produto(cod)

            elif entrada == '11':

                compra.compra_extrato()

            elif entrada == '12':

                venda.venda_extrato()
            elif entrada == '0':
                print('Obrigado por acessar. Volte Sempre.')
                break
            else:
                print('Opção Invalida!!!')
