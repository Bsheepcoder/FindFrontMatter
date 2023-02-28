# -*- coding:utf-8 -*-
"""
作者：71041
日期：2023年02月28日
"""
def find(str):
    # 返回字典
    result = {}
    # 记录识别---
    tag = 0
    # 格式化str
    strArray = str.split()
    for i, v in enumerate(strArray):
        # print(i, v)
        if v == '---':
            tag = tag + 1
        if tag == 1:
            istitle = strArray[i + 1]
            isinfo = strArray[i + 2]
            if istitle[-1] == ':' and istitle != '---':
                if isinfo[-1] != ':' and istitle != '---':
                    result[istitle[0:-1]] = isinfo
    return result