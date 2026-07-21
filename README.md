# Auth System

A Python authentication system that never stores or reconstructs passwords in plain text not even during login.

## Why this project

Storing passwords is a common task, but an easy one to get wrong. This project implements the correct approach: passwords are never saved or logged in plain text, and verification never requires reconstructing the original password.

## Technical decisions

- **bcrypt over simple hashing (e.g. SHA-256):** bcrypt is intentionally slow and generates an automatic random salt per password, making brute-force and rainbow table attacks impractical. A fast hash like SHA-256 alone is not suitable for passwords.
- **Parameterized SQL queries:** all database queries use placeholders (`?`) instead of string concatenation, preventing SQL injection.
- **Password never leaves as plain text:** even during login, the entered password is hashed and compared against the stored hash where it is never decrypted or reversed, because bcrypt hashes are not reversible.
- **SQLite for persistence:** lightweight, file-based storage with no external dependencies suitable for a system of this scale.

## Features

- User registration with duplicate check
- Login verification against stored hash
- Persistent storage in a local SQLite database
- Interactive terminal menu

## Stack

Python · bcrypt · SQLite

## Requirements

- Python 3.10+
- bcrypt (`pip install bcrypt`)

## Usage

```bash
python auth.py
```

Follow the on-screen menu to register a new user, log in, or exit.

## Usage example

Registering a new user:
```
--- Sistema de Autenticação ---
1. Registrar
2. Login
2. Sair
Escolha uma opção: 1
Novo usuário: ana
Nova senha: ********
Usuário registrado com sucesso!
```
Login attempt with wrong password:
```
Escolha uma opção: 2
Usuário: ana
Senha: ********
Usuário ou senha incorretos.
```
Successful login:
```
Escolha uma opção: 2
Usuário: ana
Senha: ********
Login bem-sucedido!
```
Stored hash (bcrypt output, never the plaintext password):

`$2b$12$G6i/kgV5wMr6dIC.9e7AaOWmU2eoUCv.TlHLinvAWDikcBHulbKyW`

## Ideas to evolve

- Password strength validation on registration
- Rate limiting / lockout after repeated failed login attempts
- Session tokens for authenticated actions beyond login

---

Ana Laura Cândido Silveira
[LinkedIn](https://www.linkedin.com/in/analauracandido)