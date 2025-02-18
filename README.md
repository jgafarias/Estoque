# Sistema de Gerenciamento de Estoque

Este é um sistema simples de gerenciamento de estoque desenvolvido em Python usando o banco de dados SQLite. O sistema permite adicionar, consultar, listar e remover produtos do estoque.

## Funcionalidades

1. **Adicionar Produtos**: Permite ao usuário adicionar novos produtos ao estoque.
2. **Consultar Produtos**: Permite ao usuário consultar a quantidade de um produto específico no estoque.
3. **Consultar Todo o Estoque**: Permite ao usuário listar todos os produtos presentes no estoque.
4. **Remover Produtos**: Permite ao usuário remover produtos do estoque.

## Estrutura do Banco de Dados

A tabela `produtos` tem os seguintes campos:
- `id`: Identificador único do produto (chave primária).
- `name`: Nome do produto.
- `quantity`: Quantidade do produto em estoque.

## Uso

### Inicializar o Banco de Dados

```python
import sqlite3

db = sqlite3.connect('Python/Estoque/Estoque.db')
cursor = db.cursor()
```

## Requisitos
- Python 3.x

## Contato

Para mais informações, entre em contato com o autor:

- **Nome:** João Gabriel
- **GitHub:** [jgafarias](https://github.com/jgafarias)