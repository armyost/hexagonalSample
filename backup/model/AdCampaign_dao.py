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
