import requests;
from bs4 import BeautifulSoup;

service_key = "RyvpO%2BRt0PTChV%2Bb4ihzA%2F9pIhxUAC70BBjjG0UOBwrSOOXjtuM6X4zE60SJLwQMZNenqmuHiqCLkz6lbt6NLg%3D%3D";
url = "https://api.odcloud.kr/api/15127532/v1/uddi:c1d09745-9e5c-48e4-b26c-c1833592509c?page=1&perPage=1000&returnType=XML&serviceKey=" + service_key;

res = requests.get(url);
soup = BeautifulSoup(res.content, "lxml");

data = soup.select("data item");
print(data);

for item in data:
  print(item.select("col[name='역명']"));


