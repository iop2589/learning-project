import crawling_common_excel as common_excel;

import requests;
from bs4 import BeautifulSoup;


product_list = [];
for page_num in range(10):

  if (page_num == 0):
    res = requests.get("https://davelee-fun.github.io/");
  else:
    res = requests.get("https://davelee-fun.github.io/page" + str(page_num + 1));
    
  soup = BeautifulSoup(res.content, "html.parser");
  items = soup.select("div.card");
  
  for item in items:
    product_name = item.select_one("div.card-body h4.card-text");
    product_date = item.select_one("div.wrapfooter span.post-date");
    product_info = [product_name.get_text().strip(), product_date.get_text().strip()];
    product_list.append(product_info);
    
common_excel.save_excel_file("crawling_data.xlsx", "Report", product_list);



