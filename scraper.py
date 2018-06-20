from bs4 import BeautifulSoup
import urllib.request
# from functions import *

def save_html(html, name):
    file = open(name + ".html","w+") 
    file.write(str(html))
    file.close() 

home_url = 'http://libgen.io/search.php?req=topicid59&open=0&column=topic'
with urllib.request.urlopen(home_url) as response:
    html = response.read()

soup = BeautifulSoup(html, 'html.parser')        
save_html(soup, "trial")

# get all rows that doesnt have bgcolor="#C0C0C0"
