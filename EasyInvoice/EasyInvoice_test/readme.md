# ༼ つ ◕_◕ ༽つindividual_check-发票核验个人版

## 环境：

```python
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams, LTFigure
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfpage import PDFPage
import os
from os import path
import shutil
import numpy as np
from openpyxl import load_workbook
import datetime
```



## 使用：

### ①新建“工号-姓名”的文件夹

### ②将.exe文件，指定报销表和所有餐饮，交通发票放入文件夹内一级目录

### ③运行.exe文件

## 功能：

### ①核验发票(有概率核验错误，原因：pdf格式不统一)

- 发票的城市-上海
- 发票的年份-当前年份
- 纳税人名称-中国电信股份有限公司上海分公司
- 纳税人识别号-91310115671143758E
- 发票章
- 去除非指定类发票类型
- 去除餐饮发票内除**餐饮服务**类型的金额

### ②统计发票金额

- 同名-至多5张

### ③移动发票到各自对应的文件夹

### ④修改餐饮报销表，交通报销表电子发票部分