# from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.google.com/")
response.raise_for_status()
# with open("Love.html", 'w') as file:
#     file.write(response.content)