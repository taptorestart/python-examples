from openpyxl import Workbook


wb = Workbook()
ws = wb.active
data = [
    ['Jane', 80, 70],
    ['John', 70, 80],
]
ws.append(["Student", "English", "Math"])
for row in data:
    ws.append(row)
ws1 = wb.create_sheet("Sheet1")
ws2 = wb.create_sheet("Sheet2")
print(wb.sheetnames)
wb.remove(ws1)
print(wb.sheetnames)
wb.save("table.xlsx")
