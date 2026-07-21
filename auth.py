import bcrypt
import sqlite3


def conectar_banco():
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            usuario TEXT PRIMARY KEY,
            senha_hash BLOB NOT NULL
        )
    """)
    conexao.commit()
    return conexao


def registrar_usuario(conexao, usuario: str, senha: str) -> bool:
    cursor = conexao.cursor()

    cursor.execute("SELECT usuario FROM usuarios WHERE usuario = ?", (usuario,))
    if cursor.fetchone() is not None:
        return False  # usuário já existe

    senha_bytes = senha.encode("utf-8")
    hash_senha = bcrypt.hashpw(senha_bytes, bcrypt.gensalt())

    cursor.execute(
        "INSERT INTO usuarios (usuario, senha_hash) VALUES (?, ?)",
        (usuario, hash_senha)
    )
    conexao.commit()
    return True

def verificar_login(conexao, usuario: str, senha: str) -> bool:
    cursor = conexao.cursor()

    cursor.execute("SELECT senha_hash FROM usuarios WHERE usuario = ?", (usuario,))
    resultado = cursor.fetchone()

    if resultado is None:
        return False  # usuário não existe

    hash_guardado = resultado[0]
    senha_bytes = senha.encode("utf-8")

    return bcrypt.checkpw(senha_bytes, hash_guardado)

def menu():
    conexao = conectar_banco()

    while True:
        print("\n--- Sistema de Autenticação ---")
        print("1. Registrar")
        print("2. Login")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            usuario = input("Novo usuário: ")
            senha = input("Nova senha: ")
            if registrar_usuario(conexao, usuario, senha):
                print("Usuário registrado com sucesso!")
            else:
                print("Esse usuário já existe.")

        elif opcao == "2":
            usuario = input("Usuário: ")
            senha = input("Senha: ")
            if verificar_login(conexao, usuario, senha):
                print("Login bem-sucedido!")
            else:
                print("Usuário ou senha incorretos.")

        elif opcao == "3":
            print("Saindo...")
            conexao.close()
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()