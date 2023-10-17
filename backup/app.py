from flask 		import Flask
from sqlalchemy	import create_engine
from flask_cors import CORS

from view		import create_endpoints
from model		import *
from service	import *


class Services:
    pass

class Models:
    pass

###################################################################
# Create APP
###################################################################
	
def create_app(config_path):
    app = Flask(__name__)
    CORS(app)

    app.config.from_pyfile(config_path)

    database = create_engine(app.config['DB_URL'], encoding = 'utf-8', max_overflow = 0, echo=True)
    recommAdServerUrl=app.config['RECOMM_AD_SERVER_URL']

	## Entity Layer
    model = Models
    model.AdCampaignDao = AdCampaignDao(database)
	
	## Business Layer
    services = Services
    services.ApiService = ApiService(recommAdServerUrl)
    services.AdCampaignService = AdCampaignService(model.AdCampaignDao, services.ApiService)

	## Create EndPoint
    create_endpoints(app, services)

    return app