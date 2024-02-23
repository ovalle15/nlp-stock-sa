from pathlib import Path
import scrapy
from scraper.items import ScraperItem
from bs4 import BeautifulSoup
import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import PunktSentenceTokenizer
import nltk
nltk.download('punkt') 
nltk.download('stopwords')
nltk.download('wordnet')

class NewsSpider(scrapy.Spider):
    name = "news"
    custom_settings = {
        'USER_AGENT': 'ScrapyBot',
        'DOWNLOAD_DELAY': 2 
        }

    def preprocess(self, documents):
        '''
        Preprocesses a list of text documents by cleaning each one.
        '''
        preprocessed_docs = []
        for doc in documents:
            preprocessed_docs.append(self.clean(doc)) 
        return preprocessed_docs 
    
    def clean(self, text):
        '''
        Cleans text by:
        - Removing URLs
        - Converting text to lowercase
        - Removing punctuation
        - Removing stopwords
        - Lemmatizing words
        '''
        tokenizer = PunktSentenceTokenizer()
        lemmatizer = WordNetLemmatizer()

        text = re.sub(r'http\S+', '', text) # Remove URLs
        text = text.lower() # Convert to lowercase
        text = re.sub(r'[^a-zA-Z0-9]', ' ', text) # Remove punctuation
        
        text = tokenizer.tokenize(text)
        stops = set(stopwords.words('english'))
        text = [word for word in text if word not in stops] # Remove stopwords
        text = [lemmatizer.lemmatize(word=word_1) for word_1 in text] # Lemmatize
        return text
    
    def start_requests(self):
        urls = [
            "https://finance.yahoo.com"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        '''
        - parse html 
        - runs methods to pre-process data for nlp models
        - yields item
        '''
        soup = BeautifulSoup(response.body, 'html.parser')
        all_hrefs = []
        for link in soup.find_all('a'):
            href = link.get('href')
            if 'https' in href:
                all_hrefs.append(href)
        
        cleaned_text = self.clean(soup.get_text())
        item = ScraperItem()
        item['content'] = cleaned_text
        item['title'] = soup.title
        item['hrefs'] = all_hrefs
        yield item
        