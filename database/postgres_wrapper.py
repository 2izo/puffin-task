from database.models.twitter_user import TwitterUser
from sqlalchemy.orm import Session

class PostgresWrapper:
    @staticmethod
    def add_twitter_user(scrapped_profile, db: Session):
        twitter_user: TwitterUser = TwitterUser()
        twitter_user.user_name = scrapped_profile.username
        twitter_user.display_name = scrapped_profile.displayname
        twitter_user.followers_count = scrapped_profile.followersCount
        twitter_user.followings_count = scrapped_profile.friendsCount
        twitter_user.likes_count = scrapped_profile.favouritesCount
        twitter_user.protected = True if scrapped_profile.protected else False
        twitter_user.bio = scrapped_profile.renderedDescription
        twitter_user.image_url = scrapped_profile.profileImageUrl
        twitter_user.location = scrapped_profile.location
        db.add(twitter_user)
        db.commit()
    
    @staticmethod
    def get_twitter_user(user_name: str, db: Session):
        twitter_user = db.query(TwitterUser).filter(TwitterUser.user_name == user_name).first()
        if twitter_user == None:
            return None
        
        return twitter_user.as_dict()