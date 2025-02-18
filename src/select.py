import sqlite3

db = sqlite3.connect('Python/Estoque/Estoque.db')
cursor = db.cursor()

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