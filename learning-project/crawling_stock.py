import requests;
from bs4 import BeautifulSoup;

res = requests.get("https://davelee-fun.github.io/blog/crawling_stock_example.html");
soup = BeautifulSoup(res.content);

data = soup.select("li.row_sty");

for item in data:
  company = item.select_one("div.st_name").get_text().strip();
  price = item.select_one("div.st_price").get_text().strip();
  
  print(company, ":", price);
  