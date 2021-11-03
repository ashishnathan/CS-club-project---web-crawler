from typing import Text
from bs4 import BeautifulSoup
import requests
from requests.api import head

# taking the source website as coreyms.com
source = requests.get('https://coreyms.com').text

#the source website is parsed using lxml parser
soup = BeautifulSoup(source,'lxml')

#working with the classes, article texts from html using beautiful soup
article = soup.find('article')
headline = article.h2.a.text
print(headline)
summary = article.find('div', class_= 'entry-content').p.text
print(summary)

#pulling the link of the youtube video in the home page of the website
vid_src = article.find('iframe', class_='youtube-player')['src']
vid_id = vid_src.split('/')
video_id = vid_id[4].split('?')
video_ID = 'youtube.com/watch?v='+ video_id[0]
print(video_ID)
# video_ID holds the link which will directly work to show the video on the front page of the website.