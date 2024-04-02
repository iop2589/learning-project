import openpyxl;

# excel save 공통 모듈
def save_excel_file (excel_file_name, excel_sheet_name, data_list):
  excel_file = openpyxl.Workbook();
  excel_sheet = excel_file.active;
  excel_sheet.column_dimensions["A"].width = 100;
  excel_sheet.column_dimensions["B"].width = 30;
  
  if excel_sheet_name != "":
    excel_sheet.title = excel_sheet_name;
  
  for data in data_list:
    excel_sheet.append(data);
    
  excel_file.save(excel_file_name);
  excel_file.close();

# excel load & print 공통 모듈 
def load_excel_file (excel_file_name, excel_sheet_name):
  excel_file = openpyxl.load_workbook(excel_file_name);
  excel_sheet = excel_file[excel_sheet_name];
  
  for row in excel_sheet.rows:
    print(row[0].value, row[1].value);