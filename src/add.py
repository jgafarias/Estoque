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
    