import urllib.request as urllib

print("This is a site connectivity checker program")
url = input("input thr url of the site: ")

def main(url):
    print("Checking connectivity***")

    response = urllib.urlopen(url)
    print("Connected to", url, "Successfully")
    print("The response code is:", response.getcode())

main(url)