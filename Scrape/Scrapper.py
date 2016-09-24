import requests
from bs4 import BeautifulSoup


class Story:
    'Common base class for all Stories'
    storyCount = 0

    def __init__(self, url, title, date, author, body, nextUrl):
        self.url = url
        self.title = title
        self.date = date
        self.author = author
        self.body = body
        self.nextUrl = nextUrl

        Story.storyCount += 1

    def displayCount(self):
        print("Total Stories %d" % Story.storyCount)


def makeStory(url):
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
    for link in links:
        if(link.get_text().strip() == "Next"):
            nextUrl = "http://www.foxnews.mobi/" + link['href'] + "&pageNum=-1"
            break
    if nextUrl is "":
        return

    out = Story(url, title, date, author, body, nextUrl)

    return out


def getNextStory(story):
    "creates a story object of the next story"
    out = makeStory(story.nextUrl)

    return out


# input("Please enter a URL")
site = "http://www.foxnews.mobi/quickPage.html?page=38321&content=118383004&pageNum=-1"
# print(site)
myStory = makeStory(site)

print("\nThe Story URL:\n" + myStory.url)
print("\nThe Story title:\n" + myStory.title)
print("\nThe Story date:\n" + myStory.date)
print("\nThe Story author:\n" + myStory.author)
print("\nThe Story body:\n" + myStory.body)
print("\nThe Story nextUrl:\n" + myStory.nextUrl)

contStory = myStory
for i in range(1000000):

    contStory = getNextStory(contStory)
    # print("\nThe Story URL:\n" + contStory.url)
    # print("\nThe Story title:\n" + contStory.title)
    # print("\nThe Story date:\n" + contStory.date)
    # print("\nThe Story author:\n" + contStory.author)
    # print("\nThe Story body:\n" + contStory.body)
    # print("\nThe Story nextUrl:\n" + contStory.nextUrl)
    print("STORY NUMBER: " + str((i + 2)))
    # input()
