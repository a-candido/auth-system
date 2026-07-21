import sqlite3

conexao = sqlite3.connect("usuarios.db")
cursor = conexao.cursor()
cursor.execute("SELECT usuario, senha_hash FROM usuarios")

for usuario, hash_senha in cursor.fetchall():
    print(f"Usuário: {usuario}")
    print(f"Hash guardado: {hash_senha}")
    print("---")

conexao.close()