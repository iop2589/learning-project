import requests;
from bs4 import BeautifulSoup;

res = requests.get("https://davelee-fun.github.io/");

if res.status_code != 200:
  print("Page Not Found");
else:
  soup = BeautifulSoup(res.content, "html.parser");
  data = soup.select("h4.card-text");
  
  for item in data:
    print(item.get_text().strip());