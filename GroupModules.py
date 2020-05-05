import time
def processCommand(inputMessage):
    command = inputMessage.split(" ",1)[0]
    content = inputMessage.split(" ",1)[1]
    if command == "!news":
        return news(content)
    elif command == "!noticias":
        return noticias(content)
    elif command == "!video":
        return video(content)
    elif command == "!test":
        return test(content)
    elif command == "!printweb":
        return printScreen(content)
    elif command == "!xkcd":
        return xkcdR(content)
    elif command == "!randint":
        return randInt(content)
    elif command == "!web":
        return webText(content)
    else:
        return None
def news(content):
    from newsapi import NewsApiClient
    API_Key = "Insert yours here"
    newsapi = NewsApiClient(api_key=API_Key)
    top_headlines = newsapi.get_top_headlines(q=content , page_size = 6)
    finalText = ""
    for article in top_headlines["articles"]:
        finalText += "*"
        finalText += article["source"]["name"]
        finalText += ": "
        finalText += article["title"] + "*"
        finalText += " \n "
        finalText +=  article["description"]
        finalText += " \n " + article["url"] + " \n "
    return finalText
def noticias(content):
    from newsapi import NewsApiClient
    API_Key = "Insert yours here"
    newsapi = NewsApiClient(api_key=API_Key)
    top_headlines = newsapi.get_top_headlines(q=content , page_size = 6, country = "br")
    finalText = ""
    for article in top_headlines["articles"]:
        finalText += "*"
        finalText += article["source"]["name"]
        finalText += ": "
        finalText += article["title"] + "*"
        finalText += " \n "
        finalText +=  article["description"]
        finalText += " \n " + article["url"] + " \n "
    return finalText
def video(content):
    print("init video")
    print(content)
    from pytube import YouTube
    print("Pytube loaded")
    yt = YouTube(content)
    print("Loading video")
    title = yt.title
    print(title)
    yt = yt.streams.get_by_itag('134')
    if int(yt.filesize) <= 5000000:
        print("Downloading video")
        yt.download(filename='temp_video')
        print("Download complete")
        return "!"+"temp_video.mp4|"+ title
    else:
        return "Video too long"
def printScreen(content):
    from selenium import webdriver
    temp_driver = webdriver.Firefox()
    try:
        temp_driver.get(content)
        screenshot = temp_driver.save_screenshot('temp_screenshot.png')
        title = temp_driver.title
        time.sleep(2)
    except:
        pass
    temp_driver.quit()
    return "!" + "temp_screenshot.png" + "|" + title
def xkcdR(content):
    import xkcd
    print("Loading xkcd")
    print(content)
    if content == "random":
        print("Getting Random")
        comic = xkcd.getRandomComic()
    elif content == "latest":
        print("Getting latest")
        comic = xkcd.getLatestComic()
    else:
        print("Getting by id")
        comic = xkcd.getComic(int(content))
    print("Downloading Comic")
    comic.download(output = "/home/victor/PycharmProjects/wppchatbot/",outputFile="xkcd.png")
    altText = comic.getAltText()
    print(altText)
    return "!xkcd.png|" + altText
def randInt(content):
    import random
    a,b = [int(i) for i in content.split()]
    number = random.randint(a,b)
    return "Your random number: " + str(number)
def webText(content):
    from bs4 import BeautifulSoup
    import requests
    r = requests.get(content)
    soup = BeautifulSoup(r.content)
    print("got page")
    mainText = soup.getText()
    urls = soup.find_all("a")
    print("Parsing text")
    newUrls = []
    for url in urls:
        try:
            url["href"]
            newUrls.append(url)
        except:
            pass
    urls = [i["href"] for i in newUrls if "http" in i["href"]]
    urlsText= "\n_________".join([cleanNone(i.string) + ": " + i["href"] for i in newUrls])
    return mainText[::1000] + "_____________" + urlsText[::300]
def cleanNone(thing):
    if thing == None:
        return ""
    else:
        return thing
def test(content):
    return "!" + "test.png"+"|Testing Image"

