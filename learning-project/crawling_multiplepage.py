import requests;
from bs4 import BeautifulSoup;

for page_num in range(10):
  if page_num == 0:
    res = requests.get("https://davelee-fun.github.io/");
  else:
    res = requests.get("https://davelee-fun.github.io/page" + str(page_num + 1));
    
  soup = BeautifulSoup(res.content, "html.parser");
  data = soup.select("h4.card-text");
  
  for item in data:
    print(item.get_text().strip());