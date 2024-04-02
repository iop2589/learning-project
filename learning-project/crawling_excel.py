import openpyxl;


# excel file 객체 생성
excel_file = openpyxl.Workbook();

# excel file sheet 생성
excel_sheet = excel_file.active;

# excel sheet 이름 변경
excel_sheet.title = "Report";

# excel sheet에 Data append
excel_sheet.append(["data1", "data2", "data3"]);

# excel file download
excel_file.save("tmp.xlsx");

# 최종적으로 excel file close 해야 완료됨.
excel_file.close();
