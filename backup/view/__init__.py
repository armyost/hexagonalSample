from datetime import datetime, timedelta
import json
import logging
import redis
import jwt

from flask      import request, jsonify, current_app, Response, g
from flask.json import JSONEncoder
from functools  import wraps

# def valid_check_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         rd = redis.StrictRedis(host=current_app.config['REDIS_HOST'], port=current_app.config['REDIS_PORT'], db=0)
#         accessToken = request.headers.get('Authorization')
#         submitInfo = request.json
#         requestUrl = request.url
#         if accessToken is not None and submitInfo is not None:
#             # Token 인증 시작  
#             try:
#                 jwt.decode(accessToken, current_app.config['JWT_SECRET_KEY'], algorithms='HS256')
#             except jwt.exceptions.InvalidTokenError:
#                  logging.warn("!!! Token is Invalid !!!")
#                  return Response(status=401)
            
#             # 중복체크 시작
#             serializedKeyStr = requestUrl+str(submitInfo['USERID'])+submitInfo['PAGEID']+submitInfo['SUBMITTIMSTAMP'].replace(" ","")
#             if rd.get(serializedKeyStr) is not None:
#                 return "중복데이터 있음"
#                 # return Response(status = 401) 
#             rd.set(serializedKeyStr, 'TEMP-VALUE')
#         else:
#             return Response(status = 401)  

#         return f(*args, **kwargs)
#     return decorated_function

def create_endpoints(app, services):
    app.json_encoder = JSONEncoder

    @app.route("/ping", methods=['GET'])
    def ping():
        return "pong"
    
