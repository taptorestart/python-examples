import os
from hashlib import blake2b


def get_hash(text, text_size):
    salt = os.urandom(blake2b.SALT_SIZE)
    h1 = blake2b(salt=salt)
    h1.update(bytes(text, 'UTF-8'))
    return h1.hexdigest()[:text_size]


if __name__ == "__main__":
    text = "hello world"
    text_size = 30
    hashed_text = get_hash(text, text_size)
    print(hashed_text)
