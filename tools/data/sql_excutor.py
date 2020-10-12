# -*- coding: utf-8 -*-
# @Project: py_online_server
# @Author: 小吴老师
# @Email: wuling@guoyasoft.com
# @Weichat: 875955899
# @Create time: 2019/10/28 17:50
from tools.data.mysql_tool import DataBaseHandle
import re


def excute(code, database='guoya_virtual_mall', rows=20):
    results = []
    conn = {
        "host": "www.guoyasoft.com",
        "port": 3306,
        "user": "stu",
        "password": "GYWiki2017",
        "database": database,
        "charset": "utf8"
    }
    db = DataBaseHandle(**conn)
    lines = parse_code(code)
    for line in lines:
        start = line.split(' ', 1)[0].lower()
        rlt = None
        if start == 'select':
            sql = ''
            # 判断是否有limit和order by
            has_limit = bool(re.search('limit', line, re.IGNORECASE))
            if not has_limit:
                sql = 'SELECT * FROM( %s ) gy LIMIT %d' % (line, rows)
            else:
                sql = line
            print(sql)
            rs = db.selectDb(sql)
            item = parse_resp('select', line, rs)
            results.append(item)
        elif start == 'insert':
            rs = db.insertDB(line)
            item = parse_resp('insert', line, rs)
            results.append(item)
        elif start == 'update':
            rs = db.updateDb(line)
            item = parse_resp('update', line, rs)
            results.append(item)
        elif start == 'delete':
            rs = db.deleteDB(line)
            item = parse_resp('delete', line, rs)
            results.append(item)
        elif start == 'show':
            rs = db.showDb(line)
            item = parse_resp('show', line, rs)
            results.append(item)
        elif start == 'use':
            rs = db.useDb(line)
            item = parse_resp('use', line, rs)
            results.append(item)
        else:
            item = ('error', line, '暂不支持该功能')
            results.append(item)
    return results


def parse_code(code):
    # 1. 去掉多行注释/* */
    while '/*' in code:
        start_index = code.find('/*')
        end_index = code.find('*/')
        code = code.replace(code[start_index:end_index + 2], ' ')
    # 2. 去掉单行注释#和--
    lines = code.split('\n')
    for i in range(len(lines)):
        line = lines[i]
        start_index = line.find('#')
        if start_index != -1:
            line = line[0:start_index]
        start_index = line.find('-- ')
        if start_index != -1:
            line = line[0:start_index]
        lines[i] = line

    # 3. 跨行sql变成一行
    code = ' '.join(lines)  # 重新合成code
    lines = code.split(';')  # 重新按分号分成语句
    # 去掉空行
    while '' in lines:
        lines.remove('')

    while ' ' in lines:
        lines.remove(' ')

    for i in range(len(lines)):
        line = lines[i]
        # 将多行变成1行
        line = line.replace('\n', ' ').strip()
        # 将制表符变成空格变成1行
        line = line.replace('\t', ' ').strip()
        lines[i] = line
    return lines


def parse_resp(type, line, rs):
    item = None
    if rs != None and rs['status'] == '0000':
        item = (type, line, rs['result'])
        if 'select' == type:
            item = (type, line, rs['result'])
        elif 'insert' == type:
            item = (type, line, '新增条数：%d' % rs['result'])
        elif 'update' == type:
            item = (type, line, '更新条数：%d' % rs['result'])
        elif 'delete' == type:
            item = (type, line, '删除条数：%d' % rs['result'])
        elif 'show' == type:
            item = (type, line, rs['result'])
        elif 'use' == type:
            item = (type, line, '使用成功')
        else:
            item = ('error', line, '暂不支持该功能')
    else:
        item = ('error', line, rs['error'])
    return item
