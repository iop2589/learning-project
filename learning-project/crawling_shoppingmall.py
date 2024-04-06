import requests;
import crawling_common_excel as cme;

query = "iphone";
display = 100;
start_num, num = 1, 0;

naver_client_id = "t0EasDWuKRaeFn7Es2gz";
naver_client_secret = "dokveQ8FP7";
head_param = {"X-Naver-Client-Id":naver_client_id, "X-Naver-Client-Secret":naver_client_secret};
items = [];

for ind in range(10):
  start_num += ind * 100;
  url = "https://openapi.naver.com/v1/search/shop.json?query=" + query + "&display=" + str(display) + "&start=" + str(start_num);
  res = requests.get(url,headers=head_param);
  
  if (res.status_code == 200):
    return_data = res.json();
    for item in return_data["items"]:
      item_info = [num + 1, item["title"], item["link"]];
      items.append(item_info);
      num += 1;

cme.save_excel_file("shopping_report.xlsx", "report", items);

