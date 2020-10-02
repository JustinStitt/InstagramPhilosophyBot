# InstagramPhilosophyBot
Generates a random philosophical quote using a Markov chain I wrote in C++ then scrapes
the web for a random photo. The text is overlayed then the image is posted to Instagram using a bot.

## Step 1 - HTML Scrape a Philosophy Corpus

**quoteScraper.py** will navigate to "https://www.goodreads.com/quotes/tag/philosophy" and use an
lxml tree to find all the content pertaining to quotes.

To do this, I create an lxml tree with the given parameters: **/div[@class="quoteText"]/text()**
Using this tree I can use RegEx to find only the information nested between quotation marks.

*Before RegEx*:

![](\images\documentation_images\beforeRegex.png)

*After RegEx*: 

![](\images\documentation_images\afterRegex.png)

## Step 2 - Create Markov Chain 
[My C++ Markov Chain Generator](https://github.com/JustinStitt/markovChainTextGenerator)

I fed all the web-scraped philosophy quotes into my Markov chain generator to create 1,000,000
quotes that mimic the syntax and word choice of the original philosophical quotes, however these sentences are uniquely made.

example sentences: 

