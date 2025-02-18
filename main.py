from src.add import add_produto
from src.select import *
from src.remove import deletar_produto

print('''
      1 - Adicionar Produtos
      2 - Consultar Produtos
      3 - Consultar Todo o Estoque
      4 - Remover Produtos
      ''')    
opcao = input('Digite o número correspondente ao que deseja: ')

if opcao == '1':
    print('Opção escolhida: Adicionar produtos.')
    add_produto()
if opcao == '2':
    print('Opção escolhida: Consultar Produtos.')
    consultar_produtos()
if opcao == '3':
    print('Opção escolhida: Todos os Produtos no estoque.')
    todos_produtos()
if opcao == '4':
    print('Opção escolhida: Deletar Produto.')
    deletar_produto()