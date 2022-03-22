from pymongo import MongoClient
from pprint import pprint
from lxml import html
import requests


class YandexParser:
    host = 'https://yandex.ru/news'
    headers = {'User-Agent': 'Chrome/76.0.3809.100'}

    def parse(self) -> list:
        news_list = []
        response = requests.get(self.host, headers=self.headers)
        dom = html.fromstring(response.text)
        news_elements = dom.xpath("//div[contains(@class,'mg-grid__row mg-grid__row_gap_8 news-top-flexible-stories news-app__top')]/div")
        for element in news_elements:
            news = {
                'title': str(element.xpath(".//a[@class='mg-card__link']/text()")),
                'url':  str(element.xpath(".//a[@class='mg-card__link']/@href")[0]),
                'source': str(element.xpath(".//span[@class='mg-card-source__source']/a/text()")),
                'publication_date': str(element.xpath(".//span[@class='mg-card-source__time']/text()"))
            }
            news_list.append(news)
        return news_list


client = MongoClient('127.0.0.1', 27017)
db = client['news']

news_result = YandexParser().parse()

db.news.insert_many(news_result)

pprint(news_result)