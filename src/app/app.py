import logging
import os

from flask import (Flask, g, jsonify, request)

from application.exceptions import WrongFileStructureException
from application.services import (AcquirePdfFile, AnonymizeTxtFile, UserService, DepartmentService)
from controller.exceptions import BadRequestException
from controller.utils import (file_by_mimetype, filter_request_consistency)
from infrastructure.database import (close_db_connection, init_db_engine, db_connect)
from infrastructure.repositories import (ReportRepository, UserRepository, DepartmentRepository)

###################################### Configuration ########################################

app = Flask(__name__)

def get_db_connection(app):
    if 'db_con' not in g:
        db_engine = app.config.get('DB_ENGINE', None) or init_db_engine()
        g.db_con = db_connect(db_engine)
    return g.db_con

@app.errorhandler(BadRequestException)
@app.errorhandler(WrongFileStructureException)
def handle_bad_request(error):
    response = jsonify(error.to_dict())
    response.status_code = 400
    return response

@app.teardown_appcontext
def teardown_db(exception=None):
    db_con = g.pop('db_con', None)
    if db_con is not None:
        close_db_connection(db_con)

###################################### View Area Start ########################################

@app.route("/ping", methods=['GET'])
def ping():
    return "pong"

@app.route("/userAdd", methods=['GET', 'POST'])
def userAdd():
    if request.method == 'GET':
        return jsonify({'status': 'alive!'})
    userInfo = filter_request_consistency(request, int)
    # logging.warn(userInfo)
    repository=UserRepository(get_db_connection(app))
    return jsonify(UserService.addUser(userInfo['id'], userInfo['description'], userInfo['userName'], userInfo['deptId'], repository))

@app.route("/deptAdd", methods=['GET', 'POST'])
def deptAdd():
    if request.method == 'GET':
        return jsonify({'status': 'alive!'})
    deptInfo = filter_request_consistency(request, int)
    repository=DepartmentRepository(get_db_connection(app))
    # logging.warn(deptInfo)
    return jsonify(DepartmentService.addDepartment(deptInfo['id'], deptInfo['description'], deptInfo['deptName'], repository))

@app.route("/userInfoDetail/<userId>", methods=['GET', 'POST'])
def userInfoDetail(userId):
    if request.method == 'POST':
        return jsonify({'status': 'not accept POST method'})
    # userInfo = filter_request_consistency(request, int)
    repository=UserRepository(get_db_connection(app))
    return jsonify(UserService.detailUser(userId, repository))



@app.route('/acquire/pdf', methods=['GET', 'POST'])
def acquire_pdf():
    if request.method == 'GET':
        return jsonify({'status': 'alive!'})

    file = file_by_mimetype(request, 'application/pdf')
    plain_text = AcquirePdfFile().do(
        file_content=file.stream.read()
    )

    return jsonify({'plain_text': plain_text})


@app.route('/anonymize/txt', methods=['GET', 'POST'])
def anonymize_txt():
    if request.method == 'GET':
        return jsonify({'status': 'alive!'})

    file = file_by_mimetype(request, 'text/plain')
    anonymized_data = AnonymizeTxtFile().do(
        file_content=file.stream.read().decode("utf-8"),
        repository=ReportRepository(get_db_connection(app))
    )

    return jsonify(anonymized_data)

###################################### View Area End ########################################

if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='0.0.0.0', port=5001)
    # app.run(host=os.getenv('HOST'), port=os.getenv('PORT'))