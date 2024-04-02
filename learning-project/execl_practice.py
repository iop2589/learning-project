import openpyxl;

excel_file = openpyxl.Workbook();
excel_sheet = excel_file.active;

excel_sheet.column_dimensions["A"].width = 100;
excel_sheet.column_dimensions["B"].width = 150;

excel_sheet.title = "Report";

excel_sheet.append(["A","B"]);
excel_file.save("AAA.xlsx");
excel_file.close();