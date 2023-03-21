# -*- coding: gbk -*-
import fitz
import os
import re
from pdfminer.high_level import extract_text
from openpyxl import Workbook
import datetime

# 指定文件夹路径
folder_path = os.getcwd()
folder_name = os.path.basename(os.getcwd())
name_pattern = re.compile(r'[\u4e00-\u9fa5]+')
num_pattern = re.compile(r'\d+')
name_match = name_pattern.findall(folder_name)
num_match = num_pattern.findall(folder_name)

# 初始化Excel表格
wb = Workbook()
ws = wb.active
ws.title = "Invoice Summary"
ws.append(["工号", "姓名", "电子发票数", "电子发票总金额"])

if num_match and name_match:
    usr_num = num_match[0]
    usr_name = name_match[0]
    value_pattern = r"\d+\.\d{2}"
    city_pattern = r"上海增值税电子普通发票?"
    # date_pattern =
    # payer__name_pattern =
    # payer_ID_pattern =
    invoice_count = 0
    total_amount = 0.00
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            invoice_count += 1
            try:
                # 读取PDF文件并匹配金额
                doc = fitz.open(filename)
                page = doc.load_page(0)
                text = page.get_text("text")
                if re.search(city_pattern,text):
                    value_matches = re.findall(value_pattern, text)
                    value_float_matches = [float(x) for x in value_matches if re.match(r"\d+\.\d{2}", x)]
                    amount = max(value_float_matches)
                    print(amount)
                    total_amount += amount
                    total_amount = round(total_amount, 2)
                    new_filename = usr_name + "-餐饮发票-" + str(amount) + ".pdf"
                    doc.close()
                    # print(new_file_name)
                    # 检查文件名是否重复
                    if filename != new_filename:
                        if os.path.exists(os.path.join(folder_path, new_filename)):
                            suffix = 1
                            while os.path.exists(os.path.join(folder_path, new_filename[:-4] + f"_{suffix}.pdf")):
                                suffix += 1
                            new_filename = new_filename[:-4] + f"_{suffix}.pdf"
                        # 重命名文件
                        os.rename(file_path, os.path.join(folder_path, new_filename))
               
            except PermissionError:
                print(f"PermissionError: {file_path} 文件被其他程序占用，无法访问。")

    print(usr_num, usr_name)
    print("电子发票张数：" + str(invoice_count))
    print("总金额：" + str(total_amount))
    # 将汇总结果写入Excel表格
    # ws.append([usr_num, usr_name, invoice_count, total_amount])
    # wb.save("餐饮报销表.xlsx")

else:
    print("文件夹名不包含员工名称。")
    print("文件夹名不包含员工工号。")
