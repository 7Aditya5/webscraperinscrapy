import scrapy
from scrapy.crawler import CrawlerProcess
import json
import csv

class ScrapJewellery(scrapy.Spider): 
    name = "scrapNecklaceSets"
     
    base_url='https://www.houseofindya.com'
    
    def start_requests(self):
        next_page = self.base_url+'/zyra/necklace-sets/cat'
      #  print('entering ',next_page)
        
        yield scrapy.Request(url=next_page,callback=self.parse)
    
    def parse(self, response):
        
        links=response.css("div.catgList a::attr(href)").extract()
       
        
        for link in links:
            new_url=self.base_url+link
            print('entering ',new_url)
            yield scrapy.Request(url=new_url,callback=self.parse)
            yield 
            { 
                'necklace_name': response.css('h1::text').extract(), 
                'img_urls': response.css("div.prodLeft li.zoomli img::attr(src)").extract() ,
                'desc': response.css('div.prodecCntr  p::text')[0].getall(),
                'price': response.css('div.prodRight h4 span::text').getall()[1]

            } 
            
        
 
# run spider  
   
process = CrawlerProcess()
process.crawl(ScrapJewellery)
process.start
ScrapJewellery.parse(ScrapJewellery,'')
