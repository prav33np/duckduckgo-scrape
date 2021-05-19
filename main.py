import bs4 as bs
import urllib.request
import requests
me = input(search: )

url = 'https://html.duckduckgo.com/html?q='+urllib.parse.quote(me)
sauce = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(sauce, "lxml")
well = soup.find_all('a')

res = []

for i in well:
	b =i.get_text(separator=' - ', strip=True)
  
	res.append(b)
  
l =  ' \n '.join([str(elem) for elem in res])

print(l)
