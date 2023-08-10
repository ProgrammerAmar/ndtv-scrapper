from bs4 import BeautifulSoup
# requests module is easy to operate some people use urllib but I prefer this one because it is easy to use.
import requests
import csv


# I put here my own blog url ,you can change it.
url="https://www.ndtv.com/"

#Requests module use to data from given url
source=requests.get(url)


# BeautifulSoup is used for getting HTML structure from requests response.(craete your soup)
soup=BeautifulSoup(source.text,'html')

news = soup.find_all('h3')
news_list = []
for item in news:
    news_title = item.find('a').text
    news_link = item.find('a')['href']
    news_list.append([news_title, news_link])


# fields for csv files
fields = ['Title', 'Link']
 
 # name of csv file 
filename = "ndtv_news.csv"
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(news_list)


    