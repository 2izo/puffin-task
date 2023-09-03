import snscrape.modules.twitter as scrapeTwitter
from snscrape.modules.twitter import TwitterProfileScraper
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

class TwitterScrapper:
    def __init__(self) -> None:
        pass

    def scrape_profile(self, user_name: str) -> TwitterProfileScraper:
        try: 
            user = scrapeTwitter.TwitterProfileScraper(user_name)
            return user
        except Exception as e:
            print(e)

    # def scrape_tweets(self, user_name) -> None:
    #     session = HTMLSession()
    #     user_page = session.get(f'http://www.twitter.com/{user_name}',cookies=None)
    #     page_content = user_page.content
    #     f = page_content.decode()
    #     user_soup = BeautifulSoup(page_content, "lxml")
    #     tweets = user_soup.find_all("div", {'class':["css-1dbjc4n", "r-1iusvr4", "r-16y2uox", "r-1777fci", "r-kzbkwu"]})
    #     x = [tweet.find("span", {'class':["css-901oao", "css-16my406", "r-poiln3", "r-bcqeeo", "r-qvutc0"]}) for tweet in tweets]
    #     x = u
