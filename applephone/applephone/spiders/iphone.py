import scrapy
from selenium import webdriver
from scrapy.selector import Selector
import numpy as np


class IphoneSpider(scrapy.Spider):
    name = "iphone"
    allowed_domains = ["www.alifstores.com"]
    start_urls = ["https://www.alifstores.com"]

    def __init__(self):
        driver = webdriver.Chrome()
        driver.get("https://www.alifstores.com")
        self.html = driver.page_source
        driver.close()

    def parse(self, response):
        resp = Selector(text=self.html)

        for item in resp.xpath("//div[@class='block-title']/strong/text()")[:11]:
            category = item.get()
            for x in np.arange(1,11):
                for prod in resp.xpath(f"(//div[@class='slick-track'])[{x}]/div"):
                    elements = prod.getall()  # Convert the Selector to a list of elements
                    print(len(elements))
                    title = prod.xpath(".//strong[@class='product-item-name']/a/@title").get()
                    link = prod.xpath(".//strong[@class='product-item-name']/a/@href").get()
                    price = prod.xpath("normalize-space(.//div[@class='final-price']/text())").get()
                    currency = prod.xpath("normalize-space(.//span[@class='price']/text())").get()
                    slot = "none"

                    try:
                        slot = prod.xpath(".//div[@class='product-uc-wrapper']/span/text()").get()
                    except:
                        pass

                    yield{
                        'category' : category,
                        'title' : title,
                        'link': link,
                        'price': price,
                        'currency': currency,
                        'slot' : slot
                    }
