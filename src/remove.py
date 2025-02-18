import sqlite3

db = sqlite3.connect('Python/Estoque/Estoque.db')
cursor = db.cursor()

def deletar_produto():
    nome = input('Digite o nome do produto para ser deletado: ')
    cursor.execute('DELETE FROM produtos WHERE name = ?', (nome,))
    db.commit()
    print(f'Produtos deletado com sucesso: {nome}')