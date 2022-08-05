import os
from dotenv import load_dotenv

load_dotenv()


def print_environment_variables():
    print(os.environ.get('username'))
    print(os.environ.get('password'))


if __name__ == '__main__':
    print_environment_variables()
