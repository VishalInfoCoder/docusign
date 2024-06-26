

class Configuration(object):
    DATABASE = {
        'name': 'docusign',
        'engine': 'peewee.MySQLDatabase',
        'user': 'nsai_user',
        'password': 'helloworld',
        'host': 'localhost',
        'port': 3306,
    }
    DEBUG = True
    SECRET_KEY = 'shhhh'