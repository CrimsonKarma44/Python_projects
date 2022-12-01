import bs4, requests

# url = input("Url: ")
url = 'https://www.google.com/search?q=l'

response = requests.get(url)

soup = bs4.BeautifulSoup(response.content, 'lxml')

title = soup.find_all('h3', {'class': 'LC20lb MBeuO DKV0Md'})
print(title)