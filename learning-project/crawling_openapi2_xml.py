import requests;
from bs4 import BeautifulSoup as bfs;

url = 'https://www.fun-coding.org/posts/dust-forecast'
request_params = {
    'serviceKey' : 'Bx2fQ8Kp7Ld1Rz5Mj9Nh3Gt6Ws4Uc0Vk1Ea8Hb7Jc3Xt9Fy6Dg0Sj2Zw7Ar4Li5Kq1Pv', 
    'returnType' : 'xml', 
    'numOfRows' : '100', 
    'pageNo' : '1', 
    'searchDate' : '2024-03-22', 
    'InformCode' : 'PM10' 
}

response = requests.get(url, params=request_params);
xml_data = response.content.decode('utf-8');

soup = bfs(xml_data, "lxml");
items = soup.find_all("item");

for item in items:
  print(item.find("datatime").get_text(), item.find("informoverall").get_text());


