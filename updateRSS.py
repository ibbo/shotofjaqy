#!/usr/bin/python
import feedparser

def getSoJFeed():
    d = feedparser.parse("http://www.shotofjaq.org/feed")
    latest = d.entries[0]
    title = '<h2>'+latest.title+'</h2>'
    body = latest.content[0]['value']
    return title+body

def main():
    print "Content-Type: text/html"
    print
    print '<script type="text/javascript" src="http://shotofjaqybot.appspot.com/assets/shotofjaqy.js"></script>'
    print '<div id="content_div">'
    feed = getSoJFeed()
    print feed
    print '</div>'

if __name__ == "__main__":
    main()
