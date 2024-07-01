# Scrape Yahoo Finance's Market Section News
from bs4 import BeautifulSoup
from transformers import pipeline
import requests
from datetime import datetime

yahoo_finance = 'https://finance.yahoo.com/topic/stock-market-news/'

class Summarizer:
    def __init__(self, url):
        self.url = url
        self.summarizer = pipeline('summarization', model='t5-base')

    def summarize_article(self):
        html_text = requests.get(self.url).text
        soup = BeautifulSoup(html_text, 'lxml')
        paragraphs = soup.find_all('p')
        article_text = ''.join([p.text for p in paragraphs])
        summary = self.summarizer(article_text, max_length=150, min_length=30, do_sample=False)
        return summary[0]['summary_text']

    def scrape_news(self):
        html_text = requests.get(self.url).text
        soup = BeautifulSoup(html_text, 'lxml')
        article_headlines = soup.find_all('h3', class_='Mb(5px)')
        with open('news_summary.txt', 'w') as file:
            file.write(datetime.now().strftime('%m/%d/%Y') + '\n\n')
            for headline in article_headlines[:2]:
                article_link = headline.a.get('href')
                self.url = article_link
                summarized_article = self.summarize_article()
                headline_text = headline.a.text
                file.write(f"Title: {headline_text}\n\n")
                file.write(f"Link: {article_link}\n\n")
                file.write(f"Summary: {summarized_article}\n\n")

session = Summarizer(yahoo_finance)
session.scrape_news()
