import re
text = "My email is sei_sunbiao@163.com"
pattern = '\w+@\w+\.\w+'
result = re.findall(pattern,text)
print(result) # 输出['sei_sunbiao@163.com']