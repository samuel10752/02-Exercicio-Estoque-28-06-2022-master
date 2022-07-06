from class_estoque_db import *
from class_fabricante_db import *
from class_produto_db import *


class Menu():
    def __init__(self):
        estoque = DBEstoque()
        produto = DBProduto()
        fabricante = DBFabricante()
        while True:
            entrada = input(('1 - Cadastrar Fabriante\n'
                             '2 - Listar Fabricante\n'
                             '3 - Cadastrar Produto\n'
                             '4 - Listar Produto\n'
                             '5 - Alterar Fabricante\n'
                             '6 - Alterar Prod.:\n'
                             '7 - Comprar:\n'
                             '8 - Vender\n'
                             '9 - Excluir Fabricante'
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

            # elif entrada == '3':
            #    estoque.salvar_produtos()
            # elif entrada == '4':
            #    estoque.listar_produtos()
            # elif entrada == '5':
            #    estoque.alterar_fabricantes()
            # elif entrada == '6':
            #    estoque.alterar_produtos()
            # elif entrada == '7':
            #    compra.comprar()
            # elif entrada == '8':
            #    venda.vender()
            # elif entrada == '9':
            #    estoque.excluir_fabricantes()
            # elif entrada == '10':
            #    estoque.excluir_produtos()
            # elif entrada == '11':
            #    compra.extrato()
            # elif entrada == '12':
            #    venda.extrato()
            elif entrada == '0':
                print('Obrigado por acessar. Volte Sempre.')
                break
            else:
                print('Opção Invalida!!!')
