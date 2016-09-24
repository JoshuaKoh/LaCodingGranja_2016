import requests
from bs4 import BeautifulSoup
from dbco import *
from datetime import datetime


class Story:
    'Common base class for all Stories'
    storyCount = 0

    def __init__(self, url, title, date, author, body, nextUrl, dateFetched):
        self.url = url
        self.title = title
        self.date = date
        self.author = author
        self.body = body
        self.nextUrl = nextUrl
        self.dateFetched = dateFetched

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

    out = Story(url, title, date, author, body, nextUrl, dateFetched)

    return out


def makeStoryCNN(url):
    "turns a url into a story object"

    html = requests.get(url).text
    soup = BeautifulSoup(html, "lxml")
    elements = soup.findAll("div", {"class": "element"})
    # print("\n" + element.get_text() + "\n")
    title = elements[0].get_text().strip()
    author = elements[1].get_text().strip()
    date = elements[2].get_text().strip()
    body = elements[3].get_text().strip()
    out = Story(url, title, date, author, body, "")

    return out


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
        "links": myStory.links,
        "nextUrl": myStory.nextUrl,
        "dateFetched": myStory.dateFetched}
    bulk.insert(storyDoc)

    contStory = myStory

    for i in range(1000000):

        contStory = getNextStory(contStory)
        storyDoc = {
            "url": contStory.url,
            "title": contStory.title,
            "author": contStory.author,
            "date": contStory.date,
            "body": contStory.body,
            "links": contStory.links,
            "nextUrl": contStory.nextUrl,
            "dateFetched": contStory.dateFetched}
        bulk.insert(storyDoc)
        print("STORY NUMBER: " + str((i + 2)))
        # input()
    try:
        bulk.execute()
    except BulkWriteError as bwe:
        pprint(bwe.details)
