import requests
from bs4 import BeautifulSoup
user_login = 'rfeldman9'
url = f'https://letterboxd.com/{user_login}/films/diary/'

r = requests.get(url)
with open('letterbox.html', 'w', encoding='utf-8') as output_file:
   output_file.write(r.text)
soup = BeautifulSoup(r.text, 'lxml')

entries = soup.find_all('tr', class_='diary-entry-row viewing-poster-container')
print(len(entries))
# 48
