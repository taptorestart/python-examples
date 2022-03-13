from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: int
    name: str = None
    email: EmailStr = None


if __name__ == "__main__":
    data = {
        'id': '1',
        'name': 'taptorestart',
        'email': 'taptorestart@gmail.com',
    }
    user = User(**data)
    print(user)
    data_with_incorrect_email = {
        'id': '2',
        'name': 'taptorestart',
        'email': 'test.gmail.com',
    }
    user = User(**data_with_incorrect_email)
    print(user)

"""
# Result
id=1 name='taptorestart' email='taptorestart@gmail.com'
Traceback (most recent call last):
  File "user.py", line 23, in <module>
    user = User(**data_with_incorrect_email)
  File "pydantic/main.py", line 331, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for User
email
  value is not a valid email address (type=value_error.email)

"""