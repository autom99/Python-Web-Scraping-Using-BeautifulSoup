import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get("https://autom99.blogspot.com/")
soup = BeautifulSoup(page.content,'html.parser')
# print(soup.prettify())

posts = soup.find_all(class_ ='posts')
# print(posts)

postHierarchy = soup.find_all(class_ = 'hierarchy')
# print(postHierarchy)

# print(soup.find_all(id='ArchiveList'))

all = pd.DataFrame({
    'Posts': posts,
    'PostHierarchy': postHierarchy,
})

print(all)