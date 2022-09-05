# InstagramPhilosophyBot

### 09/04/2022 Frontend Update

The instagram bot account got banned so I made a web frontend instead.
[Check it out!](philosophy-ai.vercel.app)

Generates a random philosophical quote using a Markov chain I wrote in C++ then scrapes
the web for a random photo. The text is overlayed then the image is posted to Instagram using a bot.

**Example Post**

![](/images/documentation_images/examplePost.jpg)

## Step 1 - HTML Scrape a Philosophy Corpus

**quoteScraper.py** will navigate to "https://www.goodreads.com/quotes/tag/philosophy" and use an
lxml tree to find all the content pertaining to quotes.

To do this, I create an lxml tree with the given parameters: **/div[@class="quoteText"]/text()**
Using this tree I can use RegEx to find only the information nested between quotation marks.

*Before RegEx*:

![](/images/documentation_images/beforeRegex.png)

*After RegEx*: 

![](/images/documentation_images/afterRegex.png)

## Step 2 - Create Markov Chain 
[My C++ Markov Chain Generator](https://github.com/JustinStitt/markovChainTextGenerator)

I fed all the web-scraped philosophy quotes into my Markov chain generator to create 1,000,000
quotes that mimic the syntax and word choice of the original philosophical quotes, however these sentences are uniquely made.

example sentences: 

* "A convention is a third which neither comprehends by itself nor by the underlying population."
* "Body is a futile exercise."
* "We all have the perfect crime."
* "Happiness consists in love."

## Step 3 - Web Scrape Random Nature Image

Using a random Unsplash fetch url: https://source.unsplash.com/random/1080x1080/?nature 
I can essentially grab a random 1080x1080 (1:1) image to use with the Markov-generated quote.

## Step 4 - Instabot.py API calls

Login as an Instagram agent using Username and Password and proceed to post our image.

## Some of my personal favorites:

![](/images/documentation_images/fav0.jpg)

![](/images/documentation_images/fav1.jpg)

![](/images/documentation_images/fav2.jpg)

![](/images/documentation_images/add1.jpg)
