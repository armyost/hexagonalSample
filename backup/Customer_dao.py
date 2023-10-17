from sqlalchemy import text

class CustomerDao:
    def __init__(self, database):
        self.db = database

    def selectUserRewardHistoryList(self, userId):
        rows = self.db.execute(text("""
            SELECT id, vector, amount, CONVERT(regidate, char) as regidate
            FROM user_reward_history
            WHERE id = :userId
            ORDER BY regidate DESC
            """),{
                'userId' : userId
            }).fetchall()
        return [{
            'vector' : row['vector'],
            'amount' : row['amount'],
            'regidate' : row['regidate']
        } for row in rows]
        
    def selectUserCurrentReward(self, userId):
        row = self.db.execute(text("""
            SELECT id, name, current_reward 
            FROM ad_users 
            WHERE id = :userId
            """), {
                'userId' : userId
            }).fetchone()
        return {
            'current_reward' : row['current_reward']
        } if row else None
    
    def updateUserReward(self, userId, rewardAmount):
        return self.db.execute(text("""
            UPDATE ad_users
            SET current_reward = :rewardAmount
            WHERE id = :userId
            """), {
                'userId'     : userId,
                'rewardAmount'      : rewardAmount
            }).rowcount

    def insertRewardHistory(self, userId, rewardAmount, vector):
        return self.db.execute(text("""
            INSERT INTO user_reward_history (
                id, vector, amount
            ) VALUES (
                :userId, :vector, :amount
            )
        """), {
            'userId' : userId,
            'vector' : vector,
            'amount' : rewardAmount
        }).rowcount