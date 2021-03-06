import requests
from bs4 import BeautifulSoup
from dbco import *
from datetime import datetime
import feedparser
import xml.etree.cElementTree as ET
from urllib.request import urlopen

class Story:
    'Common base class for all Stories'
    storyCount = 0

    def __init__(self, url, title, date, author, body, nextUrl, dateFetched, topic):
        self.url = url
        self.title = title
        self.date = date
        self.author = author
        self.body = body
        self.nextUrl = nextUrl
        self.dateFetched = dateFetched
        self.topic = topic

        Story.storyCount += 1

    def displayCount(self):
        print("Total Stories %d" % Story.storyCount)


def makeStoryFoxMobile(url):
    "turns a url into a story object"

    html = requests.get(url).text
    soup = BeautifulSoup(html, "lxml")
    elements = soup.findAll("div", {"class": "element"})
    # print("\n" + element.get_text() + "\n")
    title = elements[0].get_text().strip()
    author = elements[1].get_text().strip()
    date = elements[2].get_text().strip()
    body = elements[3].get_text().strip()
    links = elements[4].findAll(href=True)
    nextUrl = ""
    dateFetched = datetime.now()
    for link in links:
        if(link.get_text().strip() == "Next"):
            nextUrl = "http://www.foxnews.mobi/" + link['href'] + "&pageNum=-1"
            break
    if nextUrl is "":
        return

    out = Story(url, title, date, author, body, nextUrl, dateFetched, "")

    return out

def makeStoryBBC(url, topic):
    "turn an url from science daily into a story object"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "lxml")
    #print("URL: " + url)
    titleSearch = soup.find("h1", {"class": "story-body__h1"})
    if titleSearch is None:
        return None
    title = titleSearch.get_text().strip()
    #print("Title: " + title)
    dateSearch = soup.find("div", {"class": "date date--v2"})
    if dateSearch is None:
        return None
    if "hours" in dateSearch.get_text().strip():
        date = datetime.now().strftime("%b %d, %Y")
    else:
        date = dateSearch.get_text().strip()
    #print("Date: " + date)
    bodySearch = soup.findAll("div", {"class": "story-body__inner"})
    textList = []
    for tag in bodySearch:
        pTags = tag.find_all("p")
        for p in pTags:
            if p is not None:
                textList.append(p.get_text().strip())
    body = '\n\n'.join(textList)
    #print("Body: " + body)
    dateFetched = datetime.now()
    out = Story(url, title, date, "", body, "", dateFetched, topic)

    storyDoc = {
        "url": url,
        "title": title,
        "author": "",
        "date": date,
        "body": body,
        "links": "",
        "nextUrl": "",
        "dateFetched": dateFetched
    }

    return storyDoc

def makeStoryCNN(url, topic):
    "turns a url into a story object"

    html = requests.get(url).text
    soup = BeautifulSoup(html, "lxml")
    #print("URL: " + url)
    titleSearch = soup.find("h1", {"class": "pg-headline"})
    if titleSearch is None:
        titleSearch = soup.find("h1", {"class": "article-title"})
    title = titleSearch.get_text().strip()
    #print("title: " + title)

    authorSearch = soup.find("class", {"class": "metadata__byline__author"})
    if authorSearch is None:
        authorSearch = soup.find("class", {"class": "byline"})
    author = titleSearch.get_text().strip()[3:].split(",")[0]

    #print("author: " + author)
    dateSearch = soup.find("p", {"class": "update-time"})
    if dateSearch is None:
        dateSearch = soup.find("span", {"class": "cnnDateStamp"})
        date = dateSearch.get_text().strip()
    else:
        date = dateSearch.get_text().strip()[8:]
    #print("author: " + date)

    bodyList = soup.findAll(attrs={"class": "zn-body__paragraph"})
    body = ""
    for block in bodyList:
        if body is not "":
            body += "\n\n"

        body += block.get_text()
    #print("body: " + body)
    # input()

    dateFetched = datetime.now()

    out = Story(url, title, date, author, body, "", dateFetched, topic)

    return out


def readRss(rssURL, topic):
    bulk = articles.initialize_unordered_bulk_op()
    counter = 1;
    d = feedparser.parse(rssURL)
    print(d.entries[0].link)
    for entry in d.entries:
        cnnStory = makeStoryBBC(entry.link, topic)
        if cnnStory is None:
            continue
        bulk.insert(cnnStory)
        print(counter)
        counter = counter + 1

    try:
        bulk.execute()
    except BulkWriteError as bwe:
        pprint(bwe.details)
        # print(cnnStory.url)
        # print(cnnStory.title)
        # print(cnnStory.author)
        # print(cnnStory.date)
        # print(cnnStory.body)
        # print(cnnStory.nextUrl)
        # print(cnnStory.date)
        # input()
    # site = "http://www.cnn.com/2016/09/23/health/heroin-opioid-drug-overdose-deaths-visual-guide/index.html"

    # cnnStory = makeStoryCNN(site, "")

def readRssBBC():
    rssfeeds = {
        "business" : "http://feeds.bbci.co.uk/news/business/rss.xml",
        "health" :  "http://feeds.bbci.co.uk/news/health/rss.xml?edition=uk",
        "uk" : "http://feeds.bbci.co.uk/news/uk/rss.xml?edition=uk",
        "front_page" : "http://feeds.bbci.co.uk/news/rss.xml?edition=uk"
    }

    bulk = articles.initialize_unordered_bulk_op()

    counter = 1

    for key in rssfeeds.keys():
        d = feedparser.parse(rssfeeds[key])
        print(d.entries[0].link)
        for entry in d.entries:
            cnnStory = makeStoryBBC(entry.link, key)
            if cnnStory is None:
                continue
            bulk.insert(cnnStory)
            print(counter)
            counter = counter + 1

    try:
        bulk.execute()
    except BulkWriteError as bwe:
        pprint(bwe.details)

def getNextStory(story):
    "creates a story object of the next story"
    out = makeStoryFoxMobile(story.nextUrl)

    return out


def addFoxStorys():
    bulk = articles.initialize_unordered_bulk_op()

    # input("Please enter a URL")
    site = "http://www.foxnews.mobi/quickPage.html?page=38321&content=118383004&pageNum=-1"
    # print(site)
    myStory = makeStoryFoxMobile(site)

    storyDoc = {
        "url": myStory.url,
        "title": myStory.title,
        "author": myStory.author,
        "date": myStory.date,
        "body": myStory.body,
        "nextUrl": myStory.nextUrl,
        "dateFetched": myStory.dateFetched}
    bulk.insert(storyDoc)

    contStory = myStory

    for i in range(1000000):

        contStory = getNextStory(contStory)
        if (contStory is None):
            break
        storyDoc = {
            "url": contStory.url,
            "title": contStory.title,
            "author": contStory.author,
            "date": contStory.date,
            "body": contStory.body,
            "nextUrl": contStory.nextUrl,
            "dateFetched": contStory.dateFetched}
        bulk.insert(storyDoc)
        print("STORY NUMBER: " + str((i + 2)))
        # input()
    try:
        bulk.execute()
    except BulkWriteError as bwe:
        pprint(bwe.details)

def addWSJStories():
    bulk = articles.initialize_unordered_bulk_op()
    urlList = ["http://www.wsj.com/xml/rss/3_7041.xml", "http://www.wsj.com/xml/rss/3_7085.xml", "http://www.wsj.com/xml/rss/3_7031.xml", "http://www.wsj.com/xml/rss/3_7455.xml", "http://www.wsj.com/xml/rss/3_7201.xml"]
    for url in urlList:
        tree = ET.ElementTree(file=urlopen(url))
        root = tree.getroot()
        for story in root.iter('item'):
            storyURL = story.find('link').text
            html = requests.get(storyURL).text
            soup = BeautifulSoup(html, "lxml")

            # # elements = soup.findAll("h1", {"class": "wsj-article-headline"})
            title = [''.join(s.findAll(text=True))for s in soup.findAll("h1", {"class": "wsj-article-headline"})]
            dateList = [''.join(s.findAll(text=True))for s in soup.findAll("time", {"class": "timestamp"})]
            date = ''.join(dateList)
            date = date.replace('\n', '')
            date = date.replace('Updated:', '')
            date = date.replace('Updated', '')
            date = date.strip()
            print(date)

            # bodyList = [''.join(s.findAll(text=True))for s in soup.findAll("div", {"id": "wsj-article-wrap"})]
            textList = []
            div = soup.findAll('div', {'id': 'wsj-article-wrap'})
            for tag in div:
                pTag = tag.find_all("p")
                for t in pTag:
                    if t is not None:
                        textList.append(t.get_text().strip())
            text = '\n\n'.join(textList)
            if (text.strip()):
                storyDoc = {
                    "url": storyURL,
                    "title": title[0],
                    "author": None,
                    "date": date,
                    "body": text,
                    "links": None,
                    "nextUrl": None,
                    "dateFetched": datetime.now()
                }
                bulk.insert(storyDoc)

    try:
        bulk.execute()
    except BulkWriteError as bwe:
        pprint(bwe.details)

# addWSJStories()
# readRssBBC()
addFoxStorys()
