import requests;
from bs4 import BeautifulSoup;

res = requests.get("https://davelee-fun.github.io/blog/crawl_test");
soup = BeautifulSoup(res.content, "html.parser");


dev_course_list = soup.find("ul", id="dev_course_list");
titles = dev_course_list.find_all("li", class_="course");

for index, title in enumerate(titles):
  print(index + 1, ":", title.get_text().split("[")[0].split("-")[1].strip());