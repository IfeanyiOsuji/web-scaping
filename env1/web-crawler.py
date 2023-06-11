"""
This exercise gives you a chance to show off what you've learned! In this exercise, you will write the parse function for a spider and then fill in a few blanks to finish off the spider. On the course directory page of DataCamp, 
each listed course has a title and a short course description. This spider will be used to scrape the course directory to extract the 
course titles and short course descriptions. You will not need to follow any links this time. Everything you need to know is:

    The course titles are defined by the text within an h4 element whose class contains the string block__title (double underline).
    The short course descriptions are defined by the text within a paragraph p element whose class contains the string block__description (double underline).
"""

# Import scrapy
import scrapy

# Import the CrawlerProcess
from scrapy.crawler import CrawlerProcess

# Create the Spider class
class YourSpider(scrapy.Spider):
  name = 'yourspider'
  # start_requests method
  def start_requests( self ):
    url_short = 'https://assets.datacamp.com/production/repositories/2560/datasets/19a0a26daa8d9db1d920b5d5607c19d6d8094b3b/all_short'
    yield scrapy.Request(url = url_short, callback = self.parse)
      
  def parse(self, response):
    # My version of the parser you wrote in the previous part
    crs_titles = response.xpath('//h4[contains(@class,"block__title")]/text()').extract()
    crs_descrs = response.xpath('//p[contains(@class,"block__description")]/text()').extract()
    for crs_title, crs_descr in zip( crs_titles, crs_descrs ):
      dc_dict[crs_title] = crs_descr
    
# Initialize the dictionary **outside** of the Spider class
dc_dict = dict()

# Run the Spider
process = CrawlerProcess()
process.crawl(YourSpider)
process.start()

# Print a preview of courses
print(dc_dict)