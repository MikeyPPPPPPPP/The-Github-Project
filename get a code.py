import urllib.request
from bs4 import BeautifulSoup

site = 'https://github.com/MikeyPPPPPPPP/Python_google_search/blob/master/bs4_parse%20google.py'

a = urllib.request.urlopen(site)

sitehtml = a.read()

soup = BeautifulSoup(sitehtml, 'lxml')#'html.parser')
       
table = soup.find('table')
table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row[1])              

