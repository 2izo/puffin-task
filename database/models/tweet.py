from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.models.base_model import Base


class Tweet(Base):
    __tablename__ = "tweet"

    id = Column(Integer, primary_key=True, autoincrement=True)
    body = Column(String)
    likes_count = Column(Integer)
    retweets_count = Column(Integer)
    replys_count = Column(Integer)
    tweeter_user_name = Column(String, ForeignKey("twitter_user.user_name"))
    tweeter_user = relationship("TwitterUser", back_populates="tweets")