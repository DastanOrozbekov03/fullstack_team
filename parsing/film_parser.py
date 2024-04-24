import requests
from bs4 import BeautifulSoup as bs
import csv

def write_to_csv(data):
    with open('films.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow((data['title'], data['date'], data['photo']))

def get_html(url):
    response = requests.get(url)
    return response.text

def get_total_page(html):
    soup = bs(html, 'lxml')
    page_ul = soup.find('div', class_='navigation')
    if page_ul:
        total_pages = int(page_ul.find_all('a')[-2].text)
    else:
        total_pages = 1
    return int(total_pages)
def get_data(html):
    soup = bs(html, 'lxml')
    block = soup.find('div', id='dle-content')
    # print(block)
    if block:
        films = block.find_all('div', class_='shortpost')
        for film in films:
            try:
                photo = film.find('div', class_='postcover').find('a').find('img').get('src')
            except:
                photo = 'asdfghj'
            try:
                title = film.find('div', class_='posttitle').find('a').text
            except:
                title = ''
            try: 
                date = film.find('div', class_='postdata').find('div').text
            except:
                date = ''

            data = {'title': title, 
                    'date': date, 
                    'photo': photo }
            write_to_csv(data)


def main():
    url = 'https://baskino.film/films/boeviki/'
    pages = '?page='

    total_pages = get_total_page(get_html(url))

    for page in range(1, total_pages+1):
        url_with_page = url + pages + str(page)
        html = get_html(url_with_page)
        get_data(html)

with open('films.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['title', 'date', 'photo'])

main()