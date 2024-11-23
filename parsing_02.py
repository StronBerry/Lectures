import requests
from bs4 import BeautifulSoup

user_login = 'rfeldman9'
url = f'https://letterboxd.com/{user_login}/films/diary/'


html_content = requests.get(url).text

soup = BeautifulSoup(html_content, 'lxml')

# Находим все элементы <tr> с классом diary-entry-row viewing-poster-container
entries = soup.find_all('tr', class_='diary-entry-row viewing-poster-container')

data = []
for entry in entries:
    td_film_details = entry.find('td', class_='td-film-details')
    film_name = td_film_details.find('a').text

    # Находим элемент td класса td-released center и получаем текстовое представление
    release_date = entry.find('td', class_='td-released center').text

    # Добавляем новую пару ключ-значение
    data.append({'film_name': film_name, 'release_date': release_date})

print(data[:5])
# [{'film_name': 'Godzilla Minus One', 'release_date': '2023'},
# {'film_name': 'Gladiator II', 'release_date': '2024'},
# {'film_name': 'Wicked', 'release_date': '2024'},
# {'film_name': 'The Blair Witch Project', 'release_date': '1999'},
# {'film_name': 'Killer Klowns from Outer Space', 'release_date': '1988'}]