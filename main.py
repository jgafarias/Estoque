import sqlite3

db = sqlite3.connect('Python/Estoque/Estoque.db')
cursor = db.cursor()

cursor.execute('''
                    CREATE TABLE IF NOT EXISTS produtos (
                        id INTEGER PRIMARY KEY NOT NULL,
                        name VARCHAR(500) NOT NULL,
                        quantity INTEGER NOT NULL
                    )
               ''')

def add_produto():
    nome = input('Digite o nome do produto: ')
    quantidade = int(input('Digite a quantidade do produto: '))
    
    cursor.execute('''INSERT INTO produtos(name, quantity)
                      VALUES(?, ?)''', (nome, quantidade))

    db.commit()
    print(f'Produto adicionado: {nome}, quantidade: {quantidade}!')
    
def consultar_produtos():
    nome = input('Digite o nome do produto: ')
    cursor.execute('SELECT * FROM produtos WHERE name = ?', (nome,))
    produtos = cursor.fetchall()
    
    print('Produtos no estoque:')
    print('----------------------')
    for produto in produtos:
        print(f'Nome: {produto[1]}, Quantidade: {produto[2]}')

def todos_produtos():
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()
    
    print('Produtos no estoque:')
    print('----------------------')
    for produto in produtos:
        print(f'Nome: {produto[1]}, Quantidade: {produto[2]}')
        
def deletar_produto():
    nome = input('Digite o nome do produto para ser deletado: ')
    cursor.execute('DELETE FROM produtos WHERE name = ?', (nome,))
    db.commit()
    print(f'Produtos deletado com sucesso: {nome}')        

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

db.close()