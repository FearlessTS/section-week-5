import requests
from bs4 import BeautifulSoup

try:
    with open('nyt_frontpage.html', 'r',
              encoding='utf-8') as html_file:
        html = html_file.read()
except FileNotFoundError:
    html = requests.get(
        'http://www.nytimes.com/pages/todayspaper/index.html').text
    with open('nyt_frontpage.html', 'w',
              encoding='utf-8') as html_write:
        html_write.write(html)

soup = BeautifulSoup(html, 'html.parser')
column_first = soup.find('div', {'class': 'aColumn'})
# print(column_first)
list_story_soups = column_first.find_all('div', {'class': 'story'})
stories = []
for story in list_story_soups:
    # print(story.prettify)
    # print('-' * 10)
    title = story.find('h3').text.strip()
    authors = story.find('h6').text.strip()
    summary = story.find('p', {'class': 'summary'}).text.strip()
    # thumbnail = story.find('img')['src']
    # Access attribute using dict
    thumbnail_soup = story.find('img')
    if thumbnail_soup:
        thumbnail = thumbnail_soup.get('src')
    else:
        thumbnail = None

    # print(title, authors, summary, thumbnail)

    dict_story = {
        'title': title,
        'authors': authors,
        'summary': summary,
        'thumbnail': thumbnail
    }

    stories.append(dict_story)

