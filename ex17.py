'''
Use the BeautifulSoup and requests Python packages to print out a list of
all the article titles on the New York Times homepage (http://www.nytimes.com/)
'''

def main():

    import requests, time
    from time import sleep
    from bs4 import BeautifulSoup

    url ='https://www.nytimes.com/'
    #r = requests.get(url)

    r = ''
    while r == '':
        try:
            r = requests.get(url)
        except:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            continue

    soup = BeautifulSoup(r.text)

    title = soup.find_all(class_ ='story-heading')
    print title

def something():
    pass

if __name__ == '__main__':
    main()
    



