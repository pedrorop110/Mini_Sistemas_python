import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

# NOME - IDADE - CPF - SALDO
cursor.execute("""
    CREATE TABLE IF NOT EXISTS sistema_bancario(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    cpf TEXT NOT NULL UNIQUE,
    saldo REAL NOT NULL
)""")

# cursor.execute("""
#     INSERT INTO sistema_bancario ( nome, idade, cpf, saldo)
#     VALUES ( ?, ?, ?, ?)
# """, ("Pedro Lucas", 18, "123456789", 100))

# cursor.execute("""
#     INSERT INTO sistema_bancario ( nome, idade, cpf, saldo)
#     VALUES (?, ? ,? , ?)
# """, ("Vicente", 12, "987654321", 200))

# cursor.execute("SELECT nome, saldo FROM sistema_bancario WHERE nome = ?", ("Pedro Lucas",))
# informações = cursor.fetchall()
# print(informações)

# cursor.execute("SELECT nome, idade, saldo FROM sistema_bancario WHERE cpf = ?", ("123456789",))
# info = cursor.fetchone()
# print(info)

# cursor.execute("SELECT nome, idade, saldo FROM sistema_bancario WHERE cpf = ?", ("123456789",))
# info = cursor.fetchone()

# if info is None:
#     print("Conta nao encontrada!")
# else:
#     print(f"Conta encontrada! {info}")

def consultar_saldo(cpf):
    cursor.execute("SELECT nome, saldo FROM sistema_bancario WHERE cpf = ?",
                    (cpf,))

    info = cursor.fetchone()
    return info

def criar_conta(cpf, nome, idade, saldo):
    cursor.execute("""
        INSERT INTO sistema_bancario ( cpf, nome, idade, saldo)
        VALUES ( ? ,? ,? ,? )
       """, (cpf, nome, idade, saldo))
    
    conexao.commit()

def depositar(cpf, valor):
    cursor.execute("""
        UPDATE sistema_bancario
        SET saldo = saldo + ?
        WHERE cpf = ?
    """, (valor, cpf))

    linhas_atualizadas = cursor.rowcount
    conexao.commit()
    return linhas_atualizadas

def sacar(cpf, valor):
    cursor.execute("""
        UPDATE sistema_bancario
        SET saldo = saldo - ?
        WHERE cpf = ?
    """, (valor, cpf))
    
    linhas_atualizadas = cursor.rowcount
    conexao.commit()
    return linhas_atualizadas

conexao.commit()
# conexao.close()