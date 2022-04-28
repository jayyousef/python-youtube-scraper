from selenium import webdriver
from bs4 import BeautifulSoup

urls = [
    'https://www.youtube.com/c/PsychHub',
    'https://www.youtube.com/c/osmosis',
    'https://www.youtube.com/c/AnxietyCanada',
    'https://www.youtube.com/c/Therapistaid',
    'https://www.youtube.com/c/Psych2go',
    'https://www.youtube.com/c/TherapyinaNutshell',
    'https://www.youtube.com/c/AnxietyUnited',
    'https://www.youtube.com/c/beyondblue',
    'https://www.youtube.com/c/DrRamiNader',
    'https://www.youtube.com/c/ThePsychShow',
    'https://www.youtube.com/channel/UCciA8PsPm3Z5E5vlKEct_lg',
    'https://www.youtube.com/c/Katimorton'
]

def main():
    driver = webdriver.Chrome()
    for url in urls:
        driver.get('{}/videos?view=0&sort=p&flow=grid'.format(url))
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, 'lxml')
        titles = soup.findAll('a',id='video-title')
        views = soup.findAll('span',class_='style-scope ytd-grid-video-renderer')
        video_urls = soup.findAll('a',id='video-title')
        print('Channel: {}'.format(url))
        i = 0 # views and time
        j = 0 # urls
        for title in titles[:20]:
            print('\n{},{},{},https://www.youtube.com{}'.format(title.text, views[i].text, views[i+1].text, video_urls[j].get('href')))
            i+=2
            j+=1

main()