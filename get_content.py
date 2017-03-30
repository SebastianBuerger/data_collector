import urllib2

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
    body = resp.read()
    print body

