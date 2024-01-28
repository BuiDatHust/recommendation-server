from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    """ App base configuration """

    DEBUG = False
    MILVUS_HOST=getenv('MILVUS_HOST', 'localhost')
    MILVUS_PORT=getenv('MILVUS_PORT', '19530')
    MILVUS_USER=getenv('MILVUS_USER', '')
    MILVUS_PASS=getenv('MILVUS_PASS', '')
    DELAY_TIME_BACKOF_RETRY=int(getenv('DELAY_TIME_BACKOF_RETRY', '2'))
    TOTAL_RETRY_BACKOF=int(getenv('TOTAL_RETRY_BACKOF', '3'))
    GRPC_PORT=getenv('GRPC_PORT','50051')

class DevelopmentConfig(Config):
    """ App Development configuration """

    PORT = getenv('APP_PORT', '5000')
    DEBUG = True

class ProductionConfig(Config):
    """ App Production configuration """

    PORT = getenv('APP_PORT', '5000')
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

AppConfig = config.get(
    getenv('FLASK_DEBUG'), 'development')