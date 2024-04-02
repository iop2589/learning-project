from bs4 import BeautifulSoup
import requests;

res = requests.get("https://news.v.daum.net/v/20170615203441266");
soup = BeautifulSoup(res.content, "html.parser");

title = soup.find("h3", class_="tit_view");
data_list = soup.find_all("span", class_="txt_info");
print(title.get_text());
for item in data_list:
  print(item.get_text());
