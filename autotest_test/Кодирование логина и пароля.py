"""
Шифрование логина и пароля с помощью cryptography.fernet.
Сгенерируйте свой ключ и сохраните в переменную окружения ENCRYPTION_KEY.
"""
import os
from cryptography.fernet import Fernet


def get_or_create_key():
    """Получает ключ из переменной окружения или генерирует новый"""
    key = os.environ.get("ENCRYPTION_KEY")
    if key:
        return key.encode()
    # Если переменная не задана — генерируем новый ключ (для примера)
    new_key = Fernet.generate_key()
    print(f"⚠️  ENCRYPTION_KEY не задан. Сгенерирован новый ключ:\n{new_key.decode()}")
    print("Сохраните его в переменную окружения ENCRYPTION_KEY для расшифровки.")
    return new_key


def main():
    key = get_or_create_key()
    cipher = Fernet(key)

    # Здесь укажите свои логин и пароль
    username = b"Agent5"
    password = b"Agent5"

    encrypted_username = cipher.encrypt(username).decode()
    encrypted_password = cipher.encrypt(password).decode()

    print("Зашифрованный логин:", encrypted_username)
    print("Зашифрованный пароль:", encrypted_password)


if __name__ == "__main__":
    main()
