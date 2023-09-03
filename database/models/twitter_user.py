from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.models.base_model import Base


class TwitterUser(Base):
    __tablename__ = "twitter_user"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, index=True, unique=True)
    display_name = Column(String, index=True)
    image_url = Column(String)
    location = Column(String)
    bio = Column(String)
    followers_count = Column(Integer)
    followings_count = Column(Integer)
    likes_count = Column(Integer)
    protected = Column(Boolean)
    tweets = relationship("Tweet", back_populates="tweeter_user")

    def as_dict(self):
       return {twitter_user.name: getattr(self, twitter_user.name) for twitter_user in self.__table__.columns}