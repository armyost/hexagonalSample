from flask import current_app
import requests
import logging

class ApiService:
    def __init__(self, RecommAdServerUrl):
        self.RECOMM_AD_SERVER_URL = RecommAdServerUrl

    def ctrAnalyticFind(self, userId, candidateAds):
        url = self.RECOMM_AD_SERVER_URL+"/?user_id="+str(userId)+"&ad_campaign_ids="+candidateAds
        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'} 
        try: 
            responseJson = requests.get(url, headers=headers)
        except Exception as ex: 
            logging.warn(ex)
        return responseJson.json()['pctr']