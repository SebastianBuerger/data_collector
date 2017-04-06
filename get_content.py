import urllib2
# lxml/xpath usage: https://www.w3schools.com/xml/xpath_syntax.asp 
# nomenclature of xml: http://archive.oreilly.com/pub/a/perl/excerpts/system-admin-with-perl/ten-minute-xpath-utorial.html

import lxml.html
from lxml import etree


req = urllib2.Request('http://www.wg-gesucht.de/wg-zimmer-in-Aachen.1.0.1.0.html')
try:
    resp = urllib2.urlopen(req)
except urllib2.HTTPError as e:
    if e.code == 404:
        # do something..
        print '404'
    else:
        print 'another serverside error'
except urllib2.URLError as e:
    # Not an HTTP-specific error (e.g. connection refused)
    print 'a not HTTP specific error'
else:
    # 200
    content = resp.read()
    

    
    doc = lxml.html.fromstring(content)
    
    watch_els = []

    links = doc.xpath('//a[@href]')

    #els = doc.xpath('//a')
#     for el in els:
#         text = el.xpath("//text()")
#         href = el.xpath("//@href")
#         #check text and href arrays are not empty...
#         if len(href) <= 0 or len(text) <= 0:
#             #empty text/href, skip.
#             continue
#     
#         text = text[0]
#         href = href[0]
#         print text
#         print href
#         
#         if "/watch?" in href:
#             #do something with a youtube video link...
#             watch_els.append((text, href))
    
    
    print links[0].xpath("//@href")

