import requests;
from bs4 import BeautifulSoup;
import openpyxl;


# 게시글 가져오기
res = requests.get("https://davelee-fun.github.io/trial/board/news.html");
soup = BeautifulSoup(res.content, "html.parser");

items = soup.select("div.list_item");

index = 1;

xl_list = [];
xl_list.append(["No", "제목", "댓글", "URL"]);

for item in items[:7]:
  if item.select_one("span.subject_fixed") != None:
    title = item.select_one("span.subject_fixed").get_text().strip();
    coment_count = item.select_one("span.rSymph05").get_text().strip();
    link = item.select_one("a.list_subject");
    
    # 게시글의 댓글 가져오기
    rep_title = requests.get("https://davelee-fun.github.io/trial/board/" + link["href"], "html.parser");
    rep_soup = BeautifulSoup(rep_title.content, "html.parser");
    
    replies = rep_soup.select("div.comment_content");
    
    xl_info = [index, title, coment_count, "https://davelee-fun.github.io/trial/board/" + link["href"]];
    xl_list.append(xl_info);
    
    for re_ind, reply in enumerate(replies):
      comment_content = str(re_ind + 1) + ". " + reply.select_one("div.comment_view").get_text().strip().replace("\n", "").replace("\t", "");
      xl_info = ["", "", comment_content, ""];
      xl_list.append(xl_info);
      
    index += 1;

# excel save logic
excel_file = openpyxl.Workbook();
excel_sheet = excel_file.active;
excel_sheet.title = "Reporting to Website";

# excel colomun width 조정
excel_sheet.column_dimensions["A"].width = "20";
excel_sheet.column_dimensions["B"].width = "50";
excel_sheet.column_dimensions["C"].width = "100";
excel_sheet.column_dimensions["D"].width = "100";

for xl_data in xl_list:
  excel_sheet.append(xl_data);
  
excel_file.save("xl_data_report.xlsx");
excel_file.close();