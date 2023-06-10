from scrapy import Selector

# Assign to the variable css_locator a CSS Locator string which is equivalent to the XPath string given.

# Create the XPath string equivalent to the CSS Locator 
xpath = '/html/body/span[1]//a'

# Create the CSS Locator string equivalent to the XPath
css_locator = 'html > body > span:nth-of-type(1) a'

# Assign to the variable xpath a XPath string which is equivalent to the CSS Locator string given.

# Create the XPath string equivalent to the CSS Locator 
xpath = '//div[@id="uid"]/span//h4'

# Create the CSS Locator string equivalent to the XPath
css_locator = 'div#uid > span h4'


"""
    Set up the Selector object sel using the string html as the text input.
    Assign to the variable hrefs_from_xpath the href attribute values from the elements in course_as. Your solution should match hrefs_from_css!
"""
html = ''# html content not availabe yet

# Create a selector object from a secret website
sel = Selector( text = html )

# Select all hyperlinks of div elements belonging to class "course-block"
course_as = sel.css( 'div.course-block > a' )

# Selecting all href attributes chaining with css
hrefs_from_css = course_as.css( '::attr(href)' )

# Selecting all href attributes chaining with xpath
hrefs_from_xpath = course_as.xpath( './@href' )


"""
    Assign to the variable xpath an XPath string directing to the text within the paragraph p element with id equal to p3, which does not include the text of future generations of this p element.
    Assign to the variable css_locator a CSS Locator string directing to this same text.
"""

# Create an XPath string to the desired text.
xpath = '//p[@id="p3"]/text()'

# Create a CSS Locator string to the desired text.
css_locator = 'p#p3::text'




"""
    Assign to the variable xpath an XPath string directing to the text within the paragraph p element with id equal to p3, which includes the text of future generations of this p element.
    Assign to the variable css_locator a CSS Locator string directing to this same text.
"""

# Create an XPath string to the desired text.
xpath = '//p[@id="p3"]//text()'

# Create a CSS Locator string to the desired text.
css_locator = 'p#p3 ::text'