import jwt
import time


def encode_jwt(jwt_payload, key, algorithm):
    encoded = jwt.encode(jwt_payload, key, algorithm)
    return encoded


def decode_jwt(jwt_text, public_key, algorithm):
    decoded = jwt.decode(jwt_text, public_key, algorithm)
    return decoded


if __name__ == "__main__":
    key = "very_secret"
    algorithm = "HS256"
    now = int(time.time())
    exp = now + 2000
    jwt_payload = {"sid": "johndoe", "start_at": now, "exp": exp}
    encoded_text = encode_jwt(jwt_payload, key, algorithm)
    print(encoded_text)

    public_key = "very_secret"
    decoded_text = decode_jwt(encoded_text, public_key, algorithm)
    print(decoded_text)

    public_key = "wrong_key"
    decoded_text = decode_jwt(encoded_text, public_key, algorithm)
    print(decoded_text)
