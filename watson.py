# Input: JSON object with articles extracted
# Output: JSON object with analyzed articles
# Structure of output JSON file:
#   Basic Info: URL, title, date created
#   Emotions: anger, disgust, fear, joy, sadness
#   Social Tone: openness, emotional range
#   Extras: most emotional sentence, dominant emotion

import json
from dbco import *
from watson_developer_cloud import ToneAnalyzerV3

# newsJSON = open('mocksJSON/articles.json', 'r')
# news = json.load(newsJSON)

articleData = articles.find({"emotional_range": {'$exists': False}}).sort( [ ("date", 1) ])


#print(news)

tone_analyzer = ToneAnalyzerV3(
   username='f74339b8-848d-4622-9e43-2fe02e958b0c',
   password='pKZ4jVwiJzV7',
   version='2016-05-19')

class Article(object):
    _id = ""
    url = "",
    title = "",
    date = "",
    emotional_sentence = "",
    dominant_emotion = "",
    anger = 0,
    disgust = 0,
    fear = 0,
    joy = 0,
    sadness = 0,
    openness = 0,
    emotional_range = 0

def classifyArticle(news):
    article = Article()
    article._id = news['_id']
    article.url = news['url']
    article.title = news['title']
    article.date = news['dateFetched']

    try:
        analyzed = tone_analyzer.tone(news['body'])
    except:
        articles.delete_one({"_id": article._id})
        return

    # print(analyzed)

    article.anger = analyzed['document_tone']['tone_categories'][0]['tones'][0]['score']
    article.disgust = analyzed['document_tone']['tone_categories'][0]['tones'][1]['score']
    article.fear = analyzed['document_tone']['tone_categories'][0]['tones'][2]['score']
    article.joy = analyzed['document_tone']['tone_categories'][0]['tones'][3]['score']
    article.sadness = analyzed['document_tone']['tone_categories'][0]['tones'][4]['score']
    article.emotional_range = analyzed['document_tone']['tone_categories'][2]['tones'][0]['score']
    article.emotional_range = analyzed['document_tone']['tone_categories'][2]['tones'][4]['score']

    onEdge = 0  # Find most emotional sentence - stores highest emotional_range value
    # Checks the emotional range
    if analyzed.get('sentences_tone') is None:
        articles.delete_one({"_id": article._id})
        return

    for sentence in analyzed['sentences_tone']:
        if len(sentence['tone_categories']) >= 2:
            sentenceEmotional = sentence['tone_categories'][2]['tones'][4]['score']
            if sentenceEmotional > onEdge:
                onEdge = sentenceEmotional
                article.emotional_sentence = "..." + sentence['text']
        else:
            article.emotional_sentence = "No content found."


    highestEmo = max(article.anger, article.fear, article.disgust, article.joy, article.sadness)
    if(highestEmo == article.anger):
        article.dominant_emotion = "anger"
    if(highestEmo == article.fear):
        article.dominant_emotion = "fear"
    if(highestEmo == article.disgust):
        article.dominant_emotion = "disgust"
    if(highestEmo == article.joy):
        article.dominant_emotion = "joy"
    if(highestEmo == article.sadness):
        article.dominant_emotion = "sadness"

    articleDoc = {
        "emotional_sentence" : article.emotional_sentence,
        "dominant_emotion" : article.dominant_emotion,
        "anger": article.anger,
        "disgust" : article.disgust,
        "fear" : article.fear,
        "joy" : article.joy,
        "sadness" : article.sadness,
        "openness" : article.openness,
        "emotional_range" : article.emotional_range
    }
    return articleDoc


# analyzed_articles = []
# for newsArticle in news['article']:
#     analyzed_articles.append(classifyArticle(newsArticle))
# bulk = articles.initialize_unordered_bulk_op()

i = 0
for newsArticle in articleData:
    print(articleData.count())
    if (newsArticle["body"].count(' ') > 3):
        print("article %i" % i)
        newArticle = classifyArticle(newsArticle)
        if newArticle is not None:
            articles.update({'_id': newsArticle['_id']},{'$set': newArticle}, upsert=True, multi=False)
    i +=1

# try:
#     bulk.execute()
# except BulkWriteError as bwe:
#     pprint(bwe.details)
# with open('mocksJSON/analyzed_articles.json', 'w') as outfile:
#     json.dump(analyzed_articles, outfile, default=lambda o: o.__dict__, indent=2)

# For example output, print this
# print(json.dumps(tone_analyzer.tone(text='I am really excited because David is here and he is my best friend and I love him so much! Yay!'), indent=2))
