import scrapy
from .. items import AmazonItem


class AmazonDetailsSpider(scrapy.Spider):
    name = 'amazon_details'
    start_urls = ['https://www.amazon.com/s?k=mens+sunglasses&crid=M3H6Z2C0EP7G&sprefix=mens+sung%2Caps%2C569&ref=nb_sb_ss_i_1_9'

    ]

    def parse(self, response):
        items = AmazonItem()
        product_title = response.css('.a-size-base-plus.a-text-normal::text').extract()
        product_price = response.css('.a-price span').css('::text').extract()
        product_imglink = response.css('.s-image-square-aspect .s-image::attr(src)').extract()
        product_rating = response.css('.aok-align-bottom').css('::text').extract()


        items['product_title'] = product_title
        items['product_price'] = product_price
        items['product_imglink'] = product_imglink
        items['product_rating'] = product_rating

        yield items
