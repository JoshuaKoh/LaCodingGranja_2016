from dbco import *
import os
import colorsys
import json
from datetime import datetime
import pymongo
import numpy
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
from random import randint
import re

# plotlyKey = os.environ['PLOTLY_TOKEN']
# tls.set_credentials_file(username='JoshuaKoh', api_key='plotlyKey')

daysX = []
emotionsY = []

size = []
color = []

avgValues = []

_cache = {}
i = 0

# with open('mocksJSON/analyzed_articles.json') as data_file:
#     data = json.load(data_file)
for article in articles.find({"emotional_range": {'$gt': 0.25}}).sort([("emotional_range", pymongo.DESCENDING)]):
    # Format article date to get day number
    fullDate = article["date"].replace(',', ' ')
    print(fullDate)
    day = int(re.match(r'\s\d{2}\s|^\d{2}\s|\s\d\s|^\d\s', fullDate).group().strip())
    print(day)
    # Add day number to days, but don't if day + emotion combo is already in cache. Otherwise, cache day emotion combo.
    if ((day, article["dominant_emotion"]) in _cache):
        if(article["dominant_emotion"] == "anger"):
            avgValues[_cache[(day, article["dominant_emotion"])]].append(article["anger"])
        elif(article["dominant_emotion"] == "fear"):
            avgValues[_cache[(day, article["dominant_emotion"])]].append(article["fear"])
        elif(article["dominant_emotion"] == "disgust"):
            avgValues[_cache[(day, article["dominant_emotion"])]].append(article["disgust"])
        elif(article["dominant_emotion"] == "joy"):
            avgValues[_cache[(day, article["dominant_emotion"])]].append(article["joy"])
        elif(article["dominant_emotion"] == "sadness"):
            avgValues[_cache[(day, article["dominant_emotion"])]].append(article["sadness"])
        size[_cache[(day, article["dominant_emotion"])]] = size[_cache[(day, article["dominant_emotion"])]] + 5.0
        emotionsY[_cache[(day, article["dominant_emotion"])]] = numpy.mean(avgValues[_cache[(day, article["dominant_emotion"])]])
    else:
        daysX.append(day)
        if(article["dominant_emotion"] == "anger"):
            colorVal = 'rgb(255, 0, 0)'
            emotionsY.append(article["anger"])
            avgValues.append([article["anger"]])
        elif(article["dominant_emotion"] == "fear"):
            colorVal = 'rgb(205, 205, 193)'
            emotionsY.append(article["fear"])
            avgValues.append([article["fear"]])
        elif(article["dominant_emotion"] == "disgust"):
            colorVal = 'rgb(143, 188, 143)'
            emotionsY.append(article["disgust"])
            avgValues.append([article["disgust"]])
        elif(article["dominant_emotion"] == "joy"):
            colorVal = 'rgb(255, 215, 0)'
            emotionsY.append(article["joy"])
            avgValues.append([article["joy"]])
        elif(article["dominant_emotion"] == "sadness"):
            colorVal = 'rgb(30,144,255)'
            emotionsY.append(article["sadness"])
            avgValues.append([article["sadness"]])
        color.append(colorVal)
        size.append(20.0)

        _cache[(day, article["dominant_emotion"])] = i
        i = i + 1



trace0 = go.Scatter(
    x=daysX,
    y=emotionsY,
    mode='markers',
    marker=dict(
        size=size,
        color=color,
    )
)

layout = go.Layout(
    xaxis=dict(
        title='DAY IN SEPTEMBER',
        titlefont=dict(
            family='Arial, sans-serif',
            size=18,
            color='lightgrey'
        ),
        range=[0, 32]
    ),
    yaxis=dict(
        title='EMOTIONAL INTENSITY',
        titlefont=dict(
            family='Arial, sans-serif',
            size=18,
            color='lightgrey'
        ),
        range=[0, 1.5]
    )
)

data = [trace0]
fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='bubblechart-size')