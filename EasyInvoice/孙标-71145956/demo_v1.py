import re
import os
import datetime
from pdfminer.high_level import extract_text


def check_PDF(path):
    """
    :param path: 
    :return: 
    """"""
    遍历指定路径下的所有PDF文件，并使用Pdfminer 库返回每个PDF中的文本
    参数：
    path：包含PDF文件的文件夹路径
    返回值：
    一个字典，其中键是PDF文件名，值是文件中提取的文本字符串
    """

    # 检验文件夹格式是否符合要求
    folder_name = os.path.basename(os.getcwd())
    name_pattern = re.compile(r'[\u4e00-\u9fa5]+')
    num_pattern = re.compile(r'\d+')
    name_match = name_pattern.findall(folder_name)
    num_match = num_pattern.findall(folder_name)
    if num_match and name_match:
        invoice_count = 0
        total_amount = 0.00
        usr_num = num_match[0]
        usr_name = name_match[0]
        pdf_texts = {}
        correct_pdf = []
        error_pdf = []
        for filename in os.listdir(path):
            if filename.endswith('.pdf'):
                filepath = os.path.join(path, filename)
                with open(filepath, 'rb') as f:
                    pdf_texts[filename] = extract_text(f)
                
        payer = '中国电信股份有限公司上海分公司\n91310115671143758E'
        for key, value in pdf_texts.items():
            if payer in value:
                correct_pdf.append(key)
            else:
                error_pdf.append(key)
        print(correct_pdf)
    else:
        print("文件夹名格式错误")


if __name__ == '__main__':
    folder_path = os.getcwd()
    check_PDF(folder_path)

