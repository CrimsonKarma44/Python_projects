import bs4, requests,webbrowser, sys, time

# text = input("Input: ")
time.sleep(1)
print("Googling..")

res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
print("......")
time.sleep(1)

# res.status_code()
print("***...")
time.sleep(1)

soup = bs4.BeautifulSoup(res.text, features="lxml")
links = soup.select(".LC20lb a")
print("*****.")
time.sleep(2)

amount = min(5, len(links))
print("*****.")
time.sleep(3)

print("Processing...")
if links == non
for i in range(amount):
    print(links[i].get("href"))
    webbrowser.open('http://google.com' + links[i].get('href'))