import requests
from bs4 import BeautifulSoup
import json

#Create a seperate function to print headlines from the response text in a file named "headlines.txt". 
def print_headlines(response_text):
    soup = BeautifulSoup(response_text, 'lxml')
    headlines = soup.find_all(attrs={"itemprop": "headline"})
    f=open("headlines.txt","a")
    for headline in headlines:
        f.write(headline.text)
        f.write("\n")
        print(headline.text)
    f.close()

#Lets start by getting the response from the homepage url.
url = 'https://inshorts.com/en/read'
response = requests.get(url)
print_headlines(response.text)

"""
Fetching more headlines:
On the news website's homepage, you will see a load more button at the bottom. Open the devtool on chrome by pressing F12 and click on network tab. 
Here you can see all requests and responses.When you click the Load More button, a request is sent to the server with 2 key values in form data which you can see in screenshot below.
https://github.com/JaynilJaiswal/bipolar/blob/master/devtools.png

Value of news_offset variable can be found from the source code of homepage. Open the source code of homepage and search for text min_news_id.
Use value of this variable in news_offset.

URL used to load more news headlines is https://inshorts.com/en/ajax/more_news. 
Lets send the post request to this URL with required form data to fetch more headlines. 
"""
url = 'https://inshorts.com/en/ajax/more_news'
news_offset = "tjederr6-1"                                 
i=1
while i<=2000 and True:
    response = requests.post(url, data={"category": "", "news_offset": news_offset})
    if response.status_code == 200:
        response_json = json.loads(response.text)
        print_headlines(response_json["html"])
        news_offset = response_json["min_news_id"]
        i+=1
    # else:                                                 Uncomment this part if you want to stop scraping if there error in communication
        # print(response.status_code)
        # break
"""
Since the response returned is JSON string with two keys, min_news_id and html, we will parse the response into json object and get values of these two keys. 
min_news_id will be used to send next post request and html text will be used to get headlines by passing this text to the print_headlines function we defined earlier.
"""



print_headlines(response.text)