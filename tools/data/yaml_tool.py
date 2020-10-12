# -*- coding:utf-8 -*-
# Author : 小吴老师
# Data ：2019/7/31 22:47
import yaml

def get_yaml(yaml_path):
    with open(yaml_path,'r',encoding='utf-8') as f:
        content =yaml.load(f.read(),Loader=yaml.FullLoader)
    return content