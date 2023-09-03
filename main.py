from fastapi import Depends, FastAPI
import uvicorn
from sqlalchemy.orm import Session

from database.database_driver import get_db
from database.postgres_wrapper import PostgresWrapper
from twitter_scrapper import TwitterScrapper

app = FastAPI()

@app.get("/")
def root():
    return 'use the /user/<user_name> to scrap any user from twitter'

@app.post("/scrape_user/{user_name}")
def scrap_user(user_name: str, db: Session = Depends(get_db)):
    twitter_scrapper: TwitterScrapper = TwitterScrapper()
    scraped_profile = twitter_scrapper.scrape_profile(user_name)

    scraped_profile = scraped_profile.entity
    if scraped_profile == None:
        return "Couldn't scrap the user with this username"
    
    PostgresWrapper.add_twitter_user(scraped_profile, db)
    return scraped_profile



@app.get("/get_user/{user_name}")
def get_user_scraped_data(user_name: str, db: Session = Depends(get_db)):
    return PostgresWrapper.get_twitter_user(user_name, db)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)