# FlavoredNews
A new lens for seeing the world: filters news from prominent sources based on mood/tone

# Inspiration
We like to read the news and keep up to date with what is happening in the world, but we know that it can start to feel discouraging to read a lot of negative articles in a row. What if there was an application that gave you the option to adjust the negativity level of the content you saw?

We decided to run with this idea after also coming up with its data visualization applications for future expansion; it would be very cool to see the general mood of the world charted against time, and create a heat map of emotion that's organized geographically for travel implications.

# What it does
Flavored News pulls news articles in several news categories from several prominent news providers--currently, CNN, BBC, and Fox, with the framework set in place to allow extension to more. It scrapes the articles and pulls out the important parts--title, author, date, body text--and displays their summaries in a dashboard feed. The features of the feed are as follows:

News articles are colored to indicate the dominant emotion in their text: joy, anger, sadness, disgust
Users can select a story's summary to view its breakdown in more detail:
The body of the article
A link to the article at its source
A metric indicating how strongly emotional it is
Indication of the most strongly emotional sentences in the article
Users can select to view a bubble map visualizing emotional heat in the world over time (emotional intensity plotted against month, with data points scaled to reflect intensity with their size as well)
How I built it
We split the work into several major tasks and distributed them among the members. Members moved around and changed tasks as they were completed. The task breakdown is as follows:

Web scraping (3 members). Used Beautiful Soup to create a scraper customized to each of our news providers
Conversion from web scraper to Watson analyzed object (2)
Made connection through process line (1)
Database setup & website creation (1)
Front end display (2)
Deployment (entire group)
Challenges I ran into
Scraping for articles and cleaning the text that we pulled was difficult because we found that a lot of news providers structure their articles in different ways. There obviously is not an enforced format across all news websites, but there often isn't a set format within one site either, which makes the process of searching for significant data a difficult and specialized one.

We also ran into some problems figuring out how to host the application, because we have not done it before.

Accomplishments that I'm proud of
Because the scraping was a little more difficult to accomplish and yet was a really significant part of our application--we needed this to do anything else--it was a really rewarding and exciting feature to complete.

We're also proud of the clear display we were able to create to represent the quantity of data that we've aggregated.

# What I learned
We learned a lot about specific technologies: specifically, how to use Python to create a complete web application, that Beautiful Soup is an intuitive and pretty powerful tool for web scraping, and about how to use Plotly data visualization software. We also learned some more holistic lessons, like the importance of the consistency of data formatting on the back end.

# What's next for LaCodingGranja_2016
The next step for this project is the creation of more, and more advanced, data visualization models for the customized news that we pull. In addition to the existing timewise mapping, we would really like to create a geographical map with the average emotion in different global regions over the past month, so that the application could be used to offer additional consideration when select travel destinations. We also would continue to grow outwards in terms of the number of news sources we are examining.

