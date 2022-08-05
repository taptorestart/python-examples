# pyjwt
- [pyjwt github page](https://github.com/jpadilla/pyjwt)

## Environments
- python: v3.8.2
- pyjwt: v2.4.0

## Install
```shell
$ pip install -r requirements.txt
```

## Run
```shell
$ python pyjwt.py
```

Result like below

```shell
 % python pyjwt.py
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzaWQiOiJqb2huZG9lIiwic3RhcnRfYXQiOjE2NTk3MDEwOTcsImV4cCI6MTY1OTcwMzA5N30.9pYikqL2ZkYV6Jtc8rmlv6VF-EHDfYixKfTaSLqeydY
{'sid': 'johndoe', 'start_at': 1659701097, 'exp': 1659703097}
Traceback (most recent call last):
  File "pyjwt.py", line 29, in <module>
    decoded_text = decode_jwt(encoded_text, public_key, algorithm)
  File "pyjwt.py", line 11, in decode_jwt
    decoded = jwt.decode(jwt_text, public_key, algorithm)
    ....
jwt.exceptions.InvalidSignatureError: Signature verification failed
```

The error 'Signature verification failed' was raised due to the wrong public key.
