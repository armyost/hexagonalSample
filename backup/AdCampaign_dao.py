from sqlalchemy import text

class AdCampaignDao:
    def __init__(self, database):
        self.db = database

    def selectProperAdList(self, userGender, userNation):
        rows = self.db.execute(text("""
            SELECT id, name, image_url, landing_url, weight, target_country, target_gender, reward
            FROM ad_campaigns 
            WHERE target_gender = :userGender
            AND target_country = :userNation
            ORDER BY weight DESC
            """),{
                'userNation' : userNation,
                'userGender' : userGender
            }).fetchall()
        return [{
            'id' : row['id'],
            'weight' : row['weight']
        } for row in rows]


    def selectAdCampaignInfo(self, id):
        row = self.db.execute(text("""
            SELECT image_url, landing_url, reward
            FROM ad_campaigns 
            WHERE id = :id
            """), {
                'id' : id
            }).fetchone()
        return {
            'image_url' : row['image_url'],
            'landing_url' : row['landing_url'],
            'reward' : row['reward']
        } if row else None
    
    def selectAdCampaignInfoDetail(self, id):
        row = self.db.execute(text("""
            SELECT id, name, image_url, landing_url, weight, target_country, target_gender, reward
            FROM ad_campaigns 
            WHERE id = :id
            """), {
                'id' : id
            }).fetchone()
        return {
            'id' : row['id'],
            'name' : row['name'],
            'image_url' : row['image_url'],
            'landing_url' : row['landing_url'],
            'weight' : row['weight'],
            'target_country' : row['target_country'],
            'target_gender' : row['target_gender'],
            'reward' : row['reward']
        } if row else None

    def insertSourceData(self, id, name, image_url, landing_url, weight, target_country, target_gender, reward):
        return self.db.execute(text("""
            INSERT INTO ad_campaigns (
                id, name, image_url, landing_url, weight, target_country, target_gender, reward
            ) VALUES (
                :id, :name, :image_url, :landing_url, :weight, :target_country, :target_gender, :reward
            )
        """), {
            'id' : id,
            'name' : name,
            'image_url' : image_url,
            'landing_url' : landing_url,
            'weight' : weight,
            'target_country' : target_country,
            'target_gender' : target_gender,
            'reward' : reward
        }).rowcount
    
    def updateAdReward(self, adId, rewardVolume):
        return self.db.execute(text("""
            UPDATE ad_campaigns
            SET reward = :rewardVolume
            WHERE id = :adId
            """), {
                'adId'     : adId,
                'rewardVolume'      : rewardVolume
            }).rowcount