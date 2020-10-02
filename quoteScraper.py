import requests
import re #(?<=\\u201C).+(?=\\u201D)
from lxml import html
import codecs
import pprint
import os

quotesText = codecs.open('database/quotes.txt', 'w', 'utf-16')

to_read = 50;
PAGENUM = 1
while(PAGENUM <= to_read):
    page = requests.get(f'https://www.goodreads.com/quotes/tag/philosophy?page={PAGENUM}')
    tree = html.fromstring(page.text)

    quotes = tree.xpath('//div[@class="quoteText"]/text()')
    quote_arr = []

    for quote in quotes:
        match = re.search('(?<=\\u201C).+(?=\\u201D)', quote)
        if match != None:
            quote_arr.append(match.group())

    for line in quote_arr:
        quotesText.write(line + '\n')
    print("next page")
    PAGENUM += 1

quotesText.close()

#print(quotes)
#.xpath('//div[@class="quoteText]/text()')
