# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WatchItem(scrapy.Item):
    # define the fields for your item here like:
    watch_id = scrapy.Field()
    watch_title = scrapy.Field()
    watch_price = scrapy.Field()
    watch_details = scrapy.Field()
