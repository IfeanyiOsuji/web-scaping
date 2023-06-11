from scrapy import Selector
import scrapy
from scrapy.crawler import CrawlerProcess
"""
. In this lesson, we will introduce Response objects in scrapy, 
which behave like Selectors, but give us extra tools to mobilize our 
scraping efforts across multiple websites

What makes us want to use a Response object rather than a Selector is that, on top of all the Selector functionality, 
the Response object keeps track of which URL the HTML code is from, 
and hence gives us a tool to not only scrape one single site, but crawl between links on sites and scrape multiple sites automatically! 
"""

url_short = 'https://assets.datacamp.com/production/repositories/2560/datasets/19a0a26daa8d9db1d920b5d5607c19d6d8094b3b/all_short'

"""
Fill in the two blanks below (one in each of the parsing methods) with the appropriate entries so that the spider can move from the first parsing method to the second correctly.
"""

# Create the Spider class
class DCdescr( scrapy.Spider ):
  name = 'dcdescr'
  # start_requests method
  def start_requests( self ):
    yield scrapy.Request( url = url_short, callback = self.parse )
  
  # First parse method
  def parse( self, response ):
    links = response.css( 'div.course-block > a::attr(href)' ).extract()
    # Follow each of the extracted links
    for link in links:
      yield response.follow(url=link, callback=self.parse_descr)
      
  # Second parsing method
  def parse_descr( self, response ):
    # Extract course description
    course_descr = response.css( 'p.course__description::text' ).extract_first()
    # For now, just yield the course description
    
    yield course_descr

process1 = CrawlerProcess()
process1.crawl(DCdescr)
process1.start()

