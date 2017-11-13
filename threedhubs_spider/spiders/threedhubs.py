# -*- coding: utf-8 -*-
# pylint: disable-all
import scrapy
import json

data = json.load(open('./data.json'))
urls_to_crawl = []

for page in data['data']:
    urls = map(lambda x: x['url'], page)
    urls_to_crawl += urls


class ThreedhubsSpider(scrapy.Spider):
    name = 'threedhubs'
    allowed_domains = ['https://www.3dhubs.com']
    start_urls = urls_to_crawl

    def parse(self, response):
        yield {
            'name': response.css('.printer-info-headline-brand h1::text').extract_first()[:-1],
            'description': response.css('.printer-info-headline .field-name-body .field-item.item-1 p::text').extract_first(),
            'price': response.css('.h3d-affiliate-links__price::text').extract_first(),
            'alternative_price': response.css('.field-name-field-printer-price-from .item-1::text').extract_first(),
            'printer_type': response.css('.field-name-field-printer-type .item-1::text').extract_first(),
            'material': response.css('.field-name-field-printer-material .item-1::text').extract_first(),
            'buildvolume': response.css('.field-name-field-printer-buildvolume .item-1::text').extract_first(),
            'min_layer_height': response.css('.field-name-field-printer-layer-min .item-1::text').extract_first(),
            'extruder_head': response.css('.field-name-field-printer-extruder-head .item-1::text').extract_first(),
            'speed': response.css('.field-name-field-printer-speed .item-1::text').extract_first(),
            'open_source': response.css('.field-name-field-printer-open .item-1::text').extract_first(),
            'third_party_material': response.css('.field-name-field-printer-restricted-mat .item-1::text').extract_first(),
            'filament_diameter': response.css('.field-name-field-filament-diameter .item-1::text').extract_first(),
            'connectivity': response.css('.field-name-field-printer-connectivity .item-1::text').extract_first(),
            'url': response.url
        }
