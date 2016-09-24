from dbco import *
import plotly.plotly as py
import plotly.graph_objs as go

daysX = []
emotionsY = []

dayFreq = [31]
size = []

_cache = {}

for article in stocks.find({"emotions": {$gt: 0.25}}).sort([
        ("emotions", pymongo.DESCENDING):
    daysX.append(article["date"])
    # Format article date to get day number

    # Add day number to days, but don't if day + emotion combo is already in cache. Otherwise, cache day emotion combo.

    # Count day number in dayFreq.

    # Add color to node

    emotionsY.append(article["emotions"])

# Grow size of bubbles.
for day in daysX:
    if (size[day-1] is None):
        size[day-1] = 1.0
    else:
        size[day-1] = size[day-1] + 0.1

trace0 = go.Scatter(
    x=daysX,
    y=emotionsY,
    mode='markers',
    marker=dict(
        size=size,
    )
)

data = [trace0]
py.iplot(data, filename='bubblechart-size')