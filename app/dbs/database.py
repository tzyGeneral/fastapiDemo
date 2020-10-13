import redis
from config import Settings

DATABASE_URL = "mysql://{}:{}@{}:{}/{}?charset=utf8".format(
    Settings.MYSQL_USER,
    Settings.MYSQL_PASSWORD,
    Settings.MYSQL_SERVER,
    Settings.MYSQL_PORT,
    Settings.MYSQL_DB_NAME
)

# 数据库迁移配置
TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": ["aerich.models", "app.models.model"],
            # 须添加“aerich.models”
            "default_connection": "default",
        },
    },
}

pool = redis.ConnectionPool(host=Settings.REDIS_CONFIG['host'],
                            port=Settings.REDIS_CONFIG['port'],
                            # password=Settings.REDIS_CONFIG['password'],
                            db=Settings.REDIS_CONFIG['db'],
                            decode_responses=True)
redis_client = redis.StrictRedis(connection_pool=pool)
