import docx
import openpyxl

book = openpyxl.load_workbook("D:/文件丶/名单.xlsx")
sheet = book["Sheet1"]
word = docx.Document("D:/文件丶/模板.docx")
for i in range(2, 5):
    name = sheet[f"A{i}"].value
    word.paragraphs[0].runs[0].text = name  # 需要修改的位置
    word.save(f"D:/文件丶/{name}.docx")
