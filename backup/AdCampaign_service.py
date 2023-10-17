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

    def properAdListByCtr(self, userInfo, adCount):
        userAdIdStr = ""
        ctrAnalyticList = []
        ctrAnalyticIndexLists = []
        ctrResultInfoList = []
        ctrResultInfoListDic = dict()

        userAdLists = json.loads(AdCampaignService.properAdList(self, userInfo['USERGENDER'], userInfo['USERNATION']))
        for userAdList in userAdLists:
            userAdIdStr+=str(userAdList['id'])
            userAdIdStr+=","
        ctrAnalyticList = self.ApiService.ctrAnalyticFind(userInfo['USERID'], userAdIdStr[:-1])
        for i in range(adCount):
            try:
                maxValue = max(ctrAnalyticList)
            except ValueError:
                logging.warn("해당하는 Return 값이 없습니다.")
                return "해당하는 Return 값이 없습니다."
            ctrAnalyticIndexLists.append(ctrAnalyticList.index(maxValue))
            ctrAnalyticList.remove(maxValue)
        for ctrAnalyticIndex in ctrAnalyticIndexLists:
            try:
                ctrResultInfoList.append(eval(AdCampaignService.adCampaignDetail(self, userAdLists[ctrAnalyticIndex]['id'])))
            except IndexError:
                logging.warn("해당하는 Return 값이 없습니다.")
                return "해당하는 Return 값이 없습니다."
        ctrResultInfoListDic['Advertises'] = ctrResultInfoList
        return ctrResultInfoListDic

    def properAdListByRandom(self, userInfo):
        randomResultInfoList = []
        randomResultInfoListDic = dict()
        userAdLists = json.loads(AdCampaignService.properAdList(self, userInfo['USERGENDER'], userInfo['USERNATION']))  
        try:
            for userAdList in random.sample(userAdLists, 3):
                randomResultInfoList.append(eval(AdCampaignService.adCampaignDetail(self, userAdList['id'])))
        except ValueError:
            logging.warn("해당하는 Return 값이 없습니다.")
            return "해당하는 Return 값이 없습니다."
        randomResultInfoListDic['Advertises'] = randomResultInfoList
        return randomResultInfoListDic
    
    def properAdListByWgtCtrMix(self, userInfo):
        wgtCtrMixResultInfoLists = []
        wgtCtrMixResultInfoListDic = dict()
        try:
            wgtCtrMixResultInfoLists = self.properAdListByCtr(self, userInfo, 1)['Advertises'] + self.properAdListByWeight(self, userInfo, 2)['Advertises']
        except TypeError:
            logging.warn("해당하는 Return 값이 없습니다.")
            return "해당하는 Return 값이 없습니다."
        wgtCtrMixResultInfoListDic['Advertises'] = wgtCtrMixResultInfoLists
        return wgtCtrMixResultInfoListDic

    ### [과제3. 트래픽의 증가, 데이터의 증가에 따른 성능 문제에 대응하기 위해 적용한 부분]
    # @caching.cache_string()
    # def properAdList(arg, self, userGender, userNation):
    def properAdList(self, userGender, userNation):
            return json.dumps(self.AdCampaignDao.selectProperAdList(userGender, userNation))

    ### [과제3. 트래픽의 증가, 데이터의 증가에 따른 성능 문제에 대응하기 위해 적용한 부분]
    # @caching.cache_string()
    # def adCampaignDetail(arg, self, id):
    def adCampaignDetail(self, id):
        return json.dumps(self.AdCampaignDao.selectAdCampaignInfo(id))
    
################################### 임시 메서드 #####################################
    def importSourceDatas2DB(self):
        with open('src/resources/ad_campaigns.json') as file:
            datas = json.load(file)
            result=0
            for data in datas:
                result += self.AdCampaignDao.insertSourceData(data['id'], data['name'], data['image_url'], data['landing_url'], data['weight'], data['target_country'], data['target_gender'], data['reward'])               
        logging.warning("!!! Import  : %s  Rows finished !!!", result)
        return "Import finished"
####################################################################################