import requests;
from bs4 import BeautifulSoup;

res = requests.get("https://davelee-fun.github.io");
soup = BeautifulSoup(res.content, "html.parser");



# 1. Menu 가져오기
# items = soup.select("ul.navbar-nav > li.nav-item");

# for item in items:
#   print(item.get_text().strip());

# 2. 제목 가져오기
# item = soup.select_one("h1.sitetitle");
# print(item.get_text());


# 3. featured의 상품명 가져오기
# items = soup.select("section.featured-posts h4.card-text");

# for item in items:
#  print(item.get_text());


recent_post = soup.select_one("section.recent-posts");
items = recent_post.select("h4.card-text");

for item in items:
  print(item.get_text());

