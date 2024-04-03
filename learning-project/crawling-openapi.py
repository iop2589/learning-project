import requests;
import crawling_common_excel as cme;

service_key = "RyvpO%2BRt0PTChV%2Bb4ihzA%2F9pIhxUAC70BBjjG0UOBwrSOOXjtuM6X4zE60SJLwQMZNenqmuHiqCLkz6lbt6NLg%3D%3D";
type = "json";
page = "1";
per_page = "30";
url = "https://api.odcloud.kr/api/15063826/v1/uddi:b0e93f5e-f5ca-49f2-9352-ca08381a9f6a?page=" + page + "&perPage=" + per_page + "&returnType=" + type + "&serviceKey=" + service_key;

res = requests.get(url);

excel_items = [];

# Encoding이 된상태로 들어옴.
# print(json_data.content);

# json 함수를 통해 json형식으로 호출하면서 동시에 decoding도 수행
if (res.status_code == 200):
  json_data = res.json();
  items = json_data["data"];
  
  for index, item in  enumerate(items):
    excel_row = [index + 1, ":", item["장비명"], item["작업일"], item["구간"]];
    excel_items.append(excel_row);
  
  cme.save_excel_file("odcloud_data.xlsx", "Report", excel_items);
  
  cme.load_excel_file("odcloud_data.xlsx", "Report");

