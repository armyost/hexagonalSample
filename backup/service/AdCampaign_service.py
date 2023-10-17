import random
import json
import logging
from redis_decorators   import RedisCaching

class AdCampaignService:
    # REDIS_URL="redis://hostname-redis:6379"
    # caching = RedisCaching(REDIS_URL)
    
    def __init__(self, AdCampaignDao, ApiService):
        self.AdCampaignDao = AdCampaignDao
        self.ApiService = ApiService

    def properAdListByWeight(self, userInfo, adCount):
        userAdIdList = []
        userAdWeightList = []
        weightResultInfoList = []
        weightResultInfoListDic = dict()
        userAdLists = json.loads(AdCampaignService.properAdList(self, userInfo['USERGENDER'], userInfo['USERNATION']))
        for userAdList in userAdLists:
            userAdIdList.append(userAdList['id'])
            userAdWeightList.append(userAdList['weight'])
        try:
            weightResultIds = random.choices(userAdIdList, userAdWeightList, k = adCount)
        except IndexError:
            logging.warn("해당하는 Return 값이 없습니다.")
            return "해당하는 Return 값이 없습니다."
        for weightResultId in weightResultIds:
            weightResultInfoList.append(eval(AdCampaignService.adCampaignDetail(self, weightResultId)))
        weightResultInfoListDic['Advertises'] = weightResultInfoList
        return weightResultInfoListDic
