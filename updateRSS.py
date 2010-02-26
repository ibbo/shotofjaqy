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
    feed = getSoJFeed()
    print feed

if __name__ == "__main__":
    main()
