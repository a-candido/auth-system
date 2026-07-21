# Auth System

A minimal authentication system built to demonstrate secure password handling in Python, from hashing to persistent storage.

## Why this project

Storing passwords is a common but easy-to-get-wrong task. This project shows the correct approach: passwords are never stored or logged in plain text, and verification never requires reconstructing the original password.

## Key design decisions

- **bcrypt over plain hashing (e.g. SHA-256):** bcrypt is intentionally slow and includes an automatic random salt per password, making brute-force and rainbow table attacks impractical. A fast hash function like SHA-256 alone is unsuitable for passwords.
- **Parameterized SQL queries:** all database queries use placeholders (`?`) instead of string concatenation, preventing SQL injection.
- **Password never leaves as plaintext:** even during login, the entered password is hashed and compared against the stored hash, it is never decrypted or reversed, because bcrypt hashes cannot be reversed.
- **SQLite for persistence:** lightweight, file-based storage with no external dependencies, suitable for a small-scale system like this one.

## Features

- User registration with duplicate-username check
- Login verification against stored hashes
- Persistent storage in a local SQLite database
- Interactive terminal menu

## Tech stack

Python · bcrypt · SQLite

## Requirements

- Python 3.10+
- bcrypt (`pip install bcrypt`)

## Usage

```bash
python auth.py
```

Follow the on-screen menu to register a new user, log in, or exit.

## Example

Stored hash example (bcrypt output, never the plaintext password):

`$2b$12$G6i/kgV5wMr6dIC.9e7AaOWmU2eoUCv.TlHLinvAWDikcBHulbKyW`

## Possible next steps

- Password strength validation on registration
- Rate limiting / lockout after repeated failed login attempts
- Session tokens for authenticated actions beyond login

