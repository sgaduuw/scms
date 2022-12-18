from environs import Env

env = Env()
env.read_env()


class MongoSettings:
    MONGODB_DB = env.str('MONGODB_DB')
    MONGODB_HOST = env.str('MONGODB_HOST')
    MONGODB_USERNAME = env.str('MONGODB_USERNAME')
    MONGODB_PASSWORD = env.str('MONGODB_PASSWORD')


class DTBSettings:
    DEBUG_TB_ENABLED = True
    DEBUG_TB_PROFILER_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = True


class CacheSettings:
    CACHE_TYPE = env.str('CACHE_TYPE')
    CACHE_DEFAULT_TIMEOUT = env.int("CACHE_DEFAULT_TIMEOUT")


class Config(CacheSettings, DTBSettings, MongoSettings):
    FLASK_DEBUG = env.bool("FLASK_DEBUG")
    DEBUG = env.bool("FLASK_DEBUG")
    SECRET_KEY = env.str("SECRET_KEY")
    SEND_FILE_MAX_AGE_DEFAULT = env.int("SEND_FILE_MAX_AGE_DEFAULT")
    BCRYPT_LOG_ROUNDS = env.int("BCRYPT_LOG_ROUNDS", default=13)
