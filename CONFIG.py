import os

databasename = os.environ.get('databasename', 'tlgbot')
config = {
    'user': os.environ.get('user', 'root'),
    'password': os.environ.get('password', '123456'),
    'host': os.environ.get('host', 'localhost'),
    'database': databasename
}
