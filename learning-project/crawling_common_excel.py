import openpyxl;

def save_excel_file (excel_file_name, excel_sheet_name, data_list):
  excel_file = openpyxl.Workbook();
  excel_sheet = excel_file.active;
  excel_sheet.title = excel_sheet_name;
  
  for data in data_list:
    excel_sheet.append(data);
    
  excel_file.save(excel_file_name);
  excel_file.close();