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

# XPath Chaining
"""
Selector and SelectorList objects allow for chaining when using the xpath method. What this means is that you can apply the xpath method over once you've already applied it. For example, if sel is the name of our Selector, then

sel.xpath('/html/body/div[2]')

is the same as

sel.xpath('/html').xpath('./body/div[2]')

or is the same as

sel.xpath('/html').xpath('./body').xpath('./div[2]')

The only catch is that you need to "glue together" the XPath pieces by using a period at the start of each subsequent XPath string (notice the periods we added to the XPath strings in our examples).
"""

#  Fill in the blank below to chain together two xpath calls which result in the same selection as

# sel.xpath('//div/span/p[3]')

sel.xpath( '//div' ).xpath( './span/p[3]' )

html = '\n<html>\n<body>\n<div>Div 1: <p>paragraph 1</p></div>\n<div>Div 2: <p>paragraph 2</p> <p>paragraph 3</p> </div>\n<div>Div 3: <p>paragraph 4</p> <p>paragraph 5</p> <p>paragraph 6</p></div>\n<div>Div 4: <p>paragraph 7</p></div>\n<div>Div 5: <p>paragraph 8</p></div>\n</body>\n</html>\n'
"""
    Set up the Selector object sel with the html variable passed as the text argument.
    Assign to the variable divs a SelectorList of all div elements within the HTML document.
"""

# Create a Selector selecting html as the HTML document
sel = Selector(text = html)

# Create a SelectorList of all div elements in the HTML document
divs = sel.xpath('//div' )


"""
Fill in the two blanks below to assign to create the Selector object sel which uses the string html as the text it inputs.
"""

# Import requests
import requests

url = 'https://assets.datacamp.com/production/repositories/2560/datasets/19a0a26daa8d9db1d920b5d5607c19d6d8094b3b/all_short'

# Create the string html containing the HTML source
html = requests.get( url ).content

# Create the Selector object sel from html
sel = Selector( text = html )

# Print out the number of elements in the HTML document
print( "There are 1020 elements in the HTML document.")
print( "You have found: ", len( sel.xpath('//*') ) )
