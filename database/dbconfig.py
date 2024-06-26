

class Configuration(object):
    DATABASE = {
        'name': 'docusign_new',
        'engine': 'peewee.MySQLDatabase',
        'user': 'nsai_user',
        'password': 'RSj;KI4=6iR}',
        'host': 'localhost',
        'port': 3306,
    }
    DEBUG = True
    SECRET_KEY = 'shhhh'