import scrapy

class EbookSpider(scrapy.Spider):
    nama = "ebook"

    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        print("[ OUR RESPONSE ]")
        print(response)