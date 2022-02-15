from bs4 import BeautifulSoup
import requests
import urllib.request

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

source = requests.get('https://www.istockphoto.com/search/2/image?alloweduse=availableforalluses&mediatype=photography&page=4&phrase=men%20women%20and%20children&sort=best', headers = headers).text

soup =BeautifulSoup(source, 'lxml')

Images= []

img_links = soup.select('img[src^="https://media.istockphoto.com/photos"]')

#img_links = soup.findall('img', class ='nocoda')

for i in range(len(img_links)):
    Images.append(img_links[i]['src'])
    
#print(Images)

for i in range(len(Images)):
    
    #copies a network object denoted by a URL to a local file.

    name = "C:/Users/Sekyere Amponsah/Desktop/Twist/Dataset/" + str(i+1020)+ ".jpg"
    urllib.request.urlretrieve(Images[i],name)