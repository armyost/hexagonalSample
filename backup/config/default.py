from config.default import *

db = {
    'user'     : 'root',
    'password' : 'root',
    'host'     : 'hostname-mysql',
    'port'     : 3306,
    'database' : 'buzz'
}

redis = {
    'host'      : 'hostname-redis',
    'port'      : 6379
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"

REDIS_HOST = redis['host']
REDIS_PORT = 6379
REDIS_URL = f"redis://{redis['host']}:{redis['port']}"

RECOMM_AD_SERVER_URL = f"https://predict-ctr-pmj4td4sjq-du.a.run.app"

JWT_SECRET_KEY = 'SOME_SUPER_SECRET_KEY'
