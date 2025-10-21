from openpyxl import Workbook
from datetime import datetime

class ExcelWorkBook:
     def __init__(self,filename):
          self.filename = filename
          self.workbook = Workbook()
          self.excelsheet = self.workbook.active

     def setheaders(self,headers):
          self.excelsheet.append(headers)

     def setrows(self,row):
          rowwithtimestamp = row+[datetime.now().strftime("%d-%m-%Y %H:%M:%S")]
          self.excelsheet.append(rowwithtimestamp)
     def savefile(self):
          self.workbook.save(self.filename)
          print(f"Excel file saved as {self.filename}!")

if __name__ == "__main__":
     headers = ["ID","Name","Email","Created_at"]

     

     excelworkbookObj = ExcelWorkBook("users.xlsx")
     excelworkbookObj.setheaders(headers)

     initidx = 1
     while True:
          name = input("Enter Name (or type 'exit' to stop): ").strip("") # strip("#!") #####Hello

          if name.lower() == 'exit':
               break
          email = input("Enter Email: ").strip("")

          excelworkbookObj.setrows([initidx,name,email])
          initidx += 1
          print("Row added! \n")
 
     excelworkbookObj.savefile()

   

# 28EP