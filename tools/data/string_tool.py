# -*- coding:utf-8 -*-
# Author : 小吴老师
# Data ：2019/7/14 8:26

# 字典转字符串
def dic_to_str(dic):
    s = ''
    for key in dic:
        s+="{0}: {1}\n".format(key,dic[key])
    return s