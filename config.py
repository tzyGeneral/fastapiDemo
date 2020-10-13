

class Settings:
    ENVIRONMENT = "development"  # production or development or testing

    MYSQL_SERVER = '127.0.0.1'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB_NAME = 'api'
    MYSQL_PORT = '3306'

    REDIS_CONFIG = {
        'host': '127.0.0.1',
        'port': 6379,
        'db': 1,
        'password': '123',
        'aps_db': 3
    }
