import sqlite3

import requests
from bs4 import BeautifulSoup
import re

def cleanhtml(raw_html):
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext


main_url = "https://www.flip.kz"
genreurl="https://www.flip.kz/catalog?subsection=1"
genre_massiv=[]
genre_href_massiv=[]
response = requests.get(genreurl)

response_text = response.text

soup = BeautifulSoup(response_text, "html.parser")

good_list = soup.find("div", {"id": "content"})
all_genre = good_list.find_all("div", {"class": "title_m"})
all_pages_massiv=[]
base=[]
for genre in all_genre:
    #print(genre.text)
    genre_massiv.append(genre.text)
    genre_href = genre.find('a', {'class': "title"})

    response_each_genre_page = requests.get(main_url + genre_href['href'])

    genre_href_massiv.append(main_url+genre_href['href'])



i=0



for href in genre_href_massiv:
    #print("sdasdsd", genre_massiv[i])
    pageurl = href

    response = requests.get(pageurl)
    response_text = response.text
    soup = BeautifulSoup(response_text, "html.parser")
    good_list = soup.find("div", {"id": "content"})
    page_table = good_list.find("table", {"class": "pages"})

    all_pages = page_table.find_all("a", {"style": "font-weight:normal"})

    all_pages_href_massiv = []
    for page in all_pages:
        # print(genre.text)
        page_href = main_url+"/"+page['href']
        all_pages_href_massiv.append(page_href)

    i=i+1
    caturl = href

    all_pages_href_massiv.insert(0,href)
    if len(all_pages_href_massiv)>3:
        all_pages_href_massiv =all_pages_href_massiv[0:3]

    for pages in all_pages_href_massiv:

        response = requests.get(pages)
        response_text = response.text
        soup = BeautifulSoup(response_text, "html.parser")


        good_list = soup.find("div", {"class": "good-list"})
        all_books = good_list.find_all("div", {"class": "placeholder"})

        # print(len(all_books))
        for book in all_books:
            book_href = book.find('a', {'class': "pic l-h-250"})
            # print("jjhk",book_href)
            response_each_book_page = requests.get(main_url + book_href['href'])


            each_book_soup = BeautifulSoup(response_each_book_page.text, "html.parser")
            each_book_content = each_book_soup.find("div", {'id': 'content'})

            book_table = each_book_content.find("table", {'id': 'prod'})
            tr = book_table.find("tr")
            name = tr.find("h1").text
            price = each_book_soup.find("meta", {'itemprop': 'price'})
            print(name)

            description = each_book_soup.find("span", {'itemprop': 'description'})
            CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
            description = cleanhtml(description.text)

            img_book=each_book_soup.find("div",{"class":"product_img_cell"})
            img=img_book.find("img")
            img_url=img['src']
            img_url="https:"+img_url

            publishing=each_book_soup.find("div",{"style":"padding:10px"})
            publishing = publishing.find("p", {"style": "width:90%;margin-bottom:5px"}).find("b").text

            import random

            page = random.randint(200, 600)

            author = tr.find_all("td")[1].find("p").text
            author_massiv=[author]
            genre_massiv=[genre.text]
            publishing_massiv=[publishing]
            books_massiv=[name,img_url,page,description,author,genre,publishing]
            base.append(img_url)
            base.append(name)
            base.append(description)
            base.append(author)
            base.append(publishing)
            base.append(price)
            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO book_author (name) VALUES (?)",author_massiv)
            cursor.execute(f"INSERT INTO book_publishing (name) VALUES (?)", publishing_massiv)
            cursor.execute(f"INSERT INTO book_genre (genrename) VALUES (?)", genre_massiv)
            cursor.execute(f"INSERT INTO book_genre (genrename) VALUES (?)", genre_massiv)
            conn.commit()
            cursor.close()
            conn.close()

print(base)

