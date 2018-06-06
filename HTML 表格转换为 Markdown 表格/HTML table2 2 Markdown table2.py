# _*_coding:utf-8_*_

from bs4 import BeautifulSoup
import re


f = open('HTML tables.html', encoding='UTF-8')
contents = f.read()
# print(contents)
f_out = open('Markdown tables.md','w+', encoding='UTF-8')

bsObj = BeautifulSoup(contents, 'html.parser')

for idx, tr in enumerate(bsObj.findAll('tr')):
    if idx != 0:
        # 写入表格内容（第二行起），表格的每一行为一个 list 元素
        tds = tr.findAll('td')
        row_str = "|"
        for td in tds:
            td_content_list = ""
            for content in td.findAll('p'):
                # 处理 p 标签下可能存在的子标签
                print("content:", content)
                p_regex = re.compile(r">(.+?)[\s\n]*?<")
                td_content_list = p_regex.findall(str(content))
                td_content_list = ''.join(td_content_list)
                # 使用 markdown 转义字符，避免 | 竖杠引起数据丢失
                td_content_list = td_content_list.replace(r"|", r"\|")
                print("td_content_list:", td_content_list)
            row_str = row_str + " " + td_content_list + " |"
        f_out.write(row_str + "\n")
    else:
        # 表头
        headers = tr.findAll('td')
        row_str = "|"
        row_str2 = "|"
        # 写入表头内容，以及 列表右对齐
        for hearder in headers:
            row_str = row_str + " " + hearder.find('p').get_text() + " |"
            row_str2 = row_str2 + " :- |"
        f_out.write(row_str + "\n")  
        f_out.write(row_str2 + "\n") 

f.close()
f_out.close()
