# Input: JSON object with articles extracted
# Output: JSON object with analyzed articles
# Structure of output JSON file:
#   Basic Info: URL, title, date created
#   Emotions: anger, disgust, fear, joy, sadness
#   Social Tone: openness, emotional range
#   Extras: most emotional sentence

import json
from watson_developer_cloud import ToneAnalyzerV3

news = open('articles.json', 'r')

tone_analyzer = ToneAnalyzerV3(
   username='f74339b8-848d-4622-9e43-2fe02e958b0c',
   password='pKZ4jVwiJzV7',
   version='2016-05-19')

class Article(object):
    url = "",
    title = "",
    date = "",
    emotional_sentence = "",
    anger = 0,
    disgust = 0,
    fear = 0,
    joy = 0,
    sadness = 0,
    openness = 0,
    emotional_range = 0

def classifyArticle(news):
    article = Article()
    article.url = news.url
    article.title = news.title
    article.date = news.dateCreated

    analyzed = tone_analyzer.tone(news.body)
    article.anger = analyzed.document_toned.tone_categories[0].tones[0].score
    article.disgust = analyzed.document_toned.tone_categories[0].tones[1].score
    article.fear = analyzed.document_toned.tone_categories[0].tones[2].score
    article.joy = analyzed.document_toned.tone_categories[0].tones[3].score
    article.sadness = analyzed.document_toned.tone_categories[0].tones[4].score
    article.emotional_range = analyzed.document_toned.tone_categories[2].tones[0].score
    article.emotional_range = analyzed.document_toned.tone_categories[2].tones[4].score

    onEdge = 0  # Find most emotional sentence - stores highest emotional_range value
    # Checks the emotional range
    for sentence in analyzed.sentences_tone:
        sentenceEmotional = sentence.tone_categories[2].tones[4].score
        if sentenceEmotional > onEdge:
            onEdge = sentenceEmotional
            article.emotional_sentence = sentence.text
    return article

analyzed_articles = list()

for newsArticle in news:
    analyzed_articles.append(classifyArticle(newsArticle))

with open('analyzed_articles.json', 'w') as outfile:
    json.dump(analyzed_articles, outfile, default=lambda o: o.__dict__, indent=2)

# For example output, print this
# print(json.dumps(tone_analyzer.tone(text='I am really excited because David is here and he is my best friend and I love him so much! Yay!'), indent=2))
