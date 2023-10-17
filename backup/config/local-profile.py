from config.default import *

db = {
    'user'     : 'root',
    'password' : 'password',
    'host'     : '222.239.193.15',
    'port'     : 30010,
    'database' : 'iotdb'
}

redis = {
    'host'      : 'redis01.armyost.com',
    'port'      : 6379
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"

REDIS_HOST = redis['host']
REDIS_PORT = 6379
REDIS_URL = f"redis://{redis['host']}:{redis['port']}"

RECOMM_AD_SERVER_URL = f"https://predict-ctr-pmj4td4sjq-du.a.run.app"

JWT_SECRET_KEY = 'SOME_SUPER_SECRET_KEY'