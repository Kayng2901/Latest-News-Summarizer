# Latest-News-Summarizer
Scrape news webs for latest news, then summarize them using Google's T5 AI Model. I use BeautifulSoup for web scraping, and Transformers for access to T5 AI to summarize the news. The code outputs into a text file. 

Currently works for Yahoo Finance, I will add other free news sites gradually. Don't just replace the URL, it won't work since each website uses different HTML structure. Unless you are well-versed in HTML and web-scraping then feel free to play around with it.

The maximum this code can pull is 10 latest articles, this is probably due to Yahoo's limit. 
