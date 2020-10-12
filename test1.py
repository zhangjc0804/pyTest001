# -*- coding: utf-8 -*-
# @Project: guoya-app-test
# @Author: 小吴老师
# @Email: wuling@guoyasoft.com
# @Weichat: 875955899
# @Create time: 2019/9/22 8:28

# 请在terminal窗口输入下方命令：
# pip3 install --upgrade guoya-api

# -*- coding:utf-8 -*-
# Author : 小吴老师
# Data ：2019/7/18 20:27
import os
import shutil
import stat
import subprocess
import yaml
import time
import requests


def _get_yaml(yaml_path):
    with open(yaml_path, 'r', encoding='utf-8') as f:
        content = yaml.load(f.read(), Loader=yaml.FullLoader)
    return content


def _invoke(cmd):
    try:
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        print(o)
        return o
    except Exception as e:
        print('执行命令失败，请检查环境配置')
        print(e)
        raise


def _copy_file(src_file, target_dir):
    shutil.copy(src_file, target_dir)


def _copy_dir_simple(src_dir, target_dir):
    if not os.path.exists(target_dir):
        shutil.copytree(src_dir, target_dir)


"""
利用递归实现目录的遍历
@para sourcePath:原文件目录
@para targetPath:目标文件目录
"""
def _copy_dir(sourcePath, targetPath):
    if not os.path.exists(sourcePath):
        return
    if not os.path.exists(targetPath):
        os.makedirs(targetPath)

    # 遍历文件夹
    for fileName in os.listdir(sourcePath):
        # 拼接原文件或者文件夹的绝对路径
        absourcePath = os.path.join(sourcePath, fileName)
        # 拼接目标文件或者文件加的绝对路径
        abstargetPath = os.path.join(targetPath, fileName)
        # 判断原文件的绝对路径是目录还是文件
        if os.path.isdir(absourcePath):
            # 是目录就创建相应的目标目录
            if not os.path.exists(absourcePath):
                os.makedirs(abstargetPath)
            # 递归调用getDirAndCopyFile()函数
            _copy_dir(absourcePath, abstargetPath)
        # 是文件就进行复制
        if os.path.isfile(absourcePath) and not os.path.exists(abstargetPath):
            rbf = open(absourcePath, "rb")
            wbf = open(abstargetPath, "wb")
            while True:
                content = rbf.readline(1024 * 1024)
                if len(content) == 0:
                    break
                wbf.write(content)
                wbf.flush()
            rbf.close()
            wbf.close()


def _get_root_path():
    root_path = os.path.abspath(os.path.dirname(__file__)).replace('\\', '/')
    print(root_path)
    # if root_path.find('venv') > 0:
    #     root_path = root_path[:root_path.find('venv') - 1]
    return root_path + '/'


def _mkdir(path):
    is_exists = os.path.exists(path)
    if not is_exists:
        os.makedirs(path)


def _deldir(dir):
    if os.path.exists(dir):
        for file in os.listdir(dir):
            file = os.path.join(dir, file)
            if os.path.isdir(file):
                print("remove dir", file)
                os.chmod(file, stat.S_IWRITE | stat.S_IWOTH)
                _deldir(file)
            elif os.path.isfile(file):
                print("remove file", file)
                os.chmod(file, stat.S_IWRITE | stat.S_IWOTH)
                os.remove(file)
        shutil.rmtree(dir, True)


def _copy_file(src_file, target_dir):
    shutil.copy(src_file, target_dir)


def _down_big_file(srcUrl, localFile):
    print('%s\n --->>>\n  %s' % (srcUrl, localFile))
    startTime = time.time()
    with requests.get(srcUrl, stream=True) as r:
        contentLength = int(r.headers['content-length'])
        line = 'content-length: %dB/ %.2fKB/ %.2fMB'
        line = line % (contentLength, contentLength / 1024, contentLength / 1024 / 1024)
        print(line)
        print('正在下载中..............')
        downSize = 0
        with open(localFile, 'wb') as f:
            for chunk in r.iter_content(8192):
                if chunk:
                    f.write(chunk)
                downSize += len(chunk)
                line = '%d KB/s - %.2f MB， 共 %.2f MB'
                line = line % (
                    downSize / 1024 / (time.time() - startTime), downSize / 1024 / 1024, contentLength / 1024 / 1024)
                print(line, end='\r')
                if downSize >= contentLength:
                    break
        timeCost = time.time() - startTime
        line = '共耗时: %.2f s, 平均速度: %.2f KB/s'
        line = line % (timeCost, downSize / 1024 / timeCost)
        print(line)


def _init(prj_name):
    print('---------开始初始化-------------')
    root_path = _get_root_path()
    print('获取工程根目录：%s' % root_path)

    prj_dir = root_path+'/.temp/' + prj_name
    print('删除并重建临时文件夹: %s ' % prj_dir)
    _deldir(prj_dir)
    _mkdir(prj_dir)

    cmd = 'git clone https://gitee.com/guoyasoft_wuling/' + prj_name + '.git ' + prj_dir
    print(cmd)
    print('框架下载中，请耐心等候......... ')
    _invoke(cmd)

    ## 读取ui初始化配置文件
    y = _get_yaml(prj_dir + '/init_project.yaml')
    ## 复制文件夹
    dirs = y['dirs']
    for dir in dirs:
        _copy_dir(prj_dir + '/' + dir, root_path + dir)
    ## 复制文件
    files = y['files']
    for file in files:
        _copy_file(prj_dir + '/' + file, root_path)

    _deldir(root_path+'.temp/')

def init_tools_prj():
    _init('guoya-tools-test')


def init_api_prj():
    _init('guoya-api-test')


def init_ui_prj():
    # url = 'http://chromedriver.storage.googleapis.com/75.0.3770.90/chromedriver_win32.zip'
    # _mkdir(root_path + 'chrome_driver')
    # _down_big_file(url,root_path+'chrome_driver/chromedriver.exe')
    _init('guoya-ui-test')


def init_app_prj():
    _init('guoya-app-test')

def init_tools_demo():
    _init('guoya-tools-demo')

def init_api_demo():
    _init('guoya-api-demo')

def init_ui_demo():
    _init('guoya-ui-demo')

def init_app_demo():
    _init('guoya-app-demo')


if __name__=='__main__':
    _init('guoya-api-test')