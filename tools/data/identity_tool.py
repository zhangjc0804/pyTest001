# -*- coding: utf-8 -*-
# @Project: guoya-tools-test
# @Author: 小吴老师
# @Email: wuling@guoyasoft.com
# @Weichat: 875955899
# @Create time: 2019/11/1 7:56
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version 2.7.13 or 3.7.2

import random
import re
# 导入某个模块的部分类或方法
from datetime import datetime, timedelta

# 导入常量并重命名
import tools.data.identity_constant as const
from tools.data import random_tool


class IdNumber(str):

    def __init__(self, id_number):
        super(IdNumber, self).__init__()
        self.id = id_number
        self.area_id = int(self.id[0:6])
        self.birth_year = int(self.id[6:10])
        self.birth_month = int(self.id[10:12])
        self.birth_day = int(self.id[12:14])

    def get_area_name(self):
        """根据区域编号取出区域名称"""
        return const.AREA_INFO[self.area_id]

    def get_birthday(self):
        """通过身份证号获取出生日期"""
        return "{0}-{1}-{2}".format(self.birth_year, self.birth_month, self.birth_day)

    def get_age(self):
        """通过身份证号获取年龄"""
        now = (datetime.now() + timedelta(days=1))
        year, month, day = now.year, now.month, now.day

        if year == self.birth_year:
            return 0
        else:
            if self.birth_month > month or (self.birth_month == month and self.birth_day > day):
                return year - self.birth_year - 1
            else:
                return year - self.birth_year

    def get_sex(self):
        """通过身份证号获取性别， 女生：0，男生：1"""
        return int(self.id[16:17]) % 2

    def get_check_digit(self):
        """通过身份证号获取校验码"""
        check_sum = 0
        for i in range(0, 17):
            check_sum += ((1 << (17 - i)) % 11) * int(self.id[i])
        check_digit = (12 - (check_sum % 11)) % 11
        return check_digit if check_digit < 10 else 'X'


def verify_id( cert_no):
    cls=IdNumber(cert_no)
    """校验身份证是否正确"""
    if re.match(const.ID_NUMBER_18_REGEX, cert_no):
        check_digit = cls.get_check_digit()
        return str(check_digit) == cert_no[-1]
    else:
        return bool(re.match(const.ID_NUMBER_15_REGEX, cert_no))


def generate_id(sex=-1,area_id='310112',birth_days="20170703"):
    """随机生成身份证号，sex = 0表示女性，sex = 1表示男性"""

    # 随机生成一个区域码(6位数)
    if area_id == '310112':
        area_id = random_tool.random_area()['code']
    id_number=area_id
    # 限定出生日期范围(8位数)
    if birth_days == '20170703':
        # start, end = datetime.strptime("1960-01-01", "%Y-%m-%d"), datetime.strptime("2000-12-30", "%Y-%m-%d")
        # birth_days = datetime.strftime(start + timedelta(random.randint(0, (end - start).days + 1)), "%Y%m%d")
        birth_days=random_tool.random_birthday(0,100)
    id_number += str(birth_days)
    # 顺序码(2位数)
    id_number += str(random.randint(10, 99))
    # 性别码(1位数)
    if sex ==-1:
        sex=str(random.randrange(sex, 10, step=2))
    elif sex==0:
        sex=str(random.randrange(1, 10, step=2))
    elif sex==1:
        sex=str(random.randrange(0, 10, step=2))
    id_number += sex
    # 校验码(1位数)
    cls = IdNumber(id_number)
    return id_number + str(cls.get_check_digit())
