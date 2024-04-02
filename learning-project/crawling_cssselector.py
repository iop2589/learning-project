import requests;
from bs4 import BeautifulSoup;

res = requests.get("https://davelee-fun.github.io/blog/crawl_html_css.html");
soup = BeautifulSoup(res.content, "html.parser");

# ul tag 바로 아래 li가 있을 경우
# data = soup.select("ul > li");

# ul tag 안에 어디든 li가 있을 경우
# data = soup.select("ul li");

# id 로 할 경우
# data = soup.select("#start");

# class로 할경우
# data = soup.select(".course");

# 복합적으로 할경우
# data = soup.select("ul#hobby_course_list > li.course");

# for item in data:
#  print(item.get_text());

# 하나만 가져올 때
# data = soup.select_one("ul#dev_course_list > li.course.paid");
# print (data.get_text());

# find, find_all, select 호환 code example
items = soup.find_all("tr");

for item in items:
  columns = item.select("td");
  row_str = "";
  for column in columns:
    row_str += ', ' + column.get_text();
  print(row_str[2:]);
    
