from scrapy import Selector
html = """
<html>
    <body>
        <div class ='hello datacamp'>
            <p>Hello World</p>
        </div>
        <p>Enjoy Datacamp!</p>
    </body>
</html>
"""
sel = Selector(text = html)
#  extract all p elemnts
print(sel.xpath('//p').extract())

# extract the first p element
print(sel.xpath('//p')[0].extract()) 
print(sel.xpath('//p').extract_first())
