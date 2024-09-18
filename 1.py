from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

# Генерация ключа и инициализационного вектора
key = os.urandom(16)  # Ключ длиной 16 байт (128 бит)
iv = os.urandom(16)   # Инициализационный вектор длиной 16 байт

# Создание объекта шифрования
cipher = AES.new(key, AES.MODE_CBC, iv)

# Исходные данные для шифрования
data = b'Привет, мир!'

# Шифрование данных
ciphertext = cipher.encrypt(pad(data, AES.block_size))

# Расшифровка
cipher_dec = AES.new(key, AES.MODE_CBC, iv)
plaintext = unpad(cipher_dec.decrypt(ciphertext), AES.block_size)

# Вывод результатов
print("Исходные данные:", data)
print("Зашифрованные данные:", ciphertext)
print("Расшифрованные данные:", plaintext)
