"""
封装request
"""

import requests
from tools.report import log_tool
from tools.report.decorators_tool import logs
import time


@logs
def get(url, params=None, headers=None, cookies=None):
    if not (url.startswith('http://') or url.startswith('https://')):
        url = '%s%s' % ('http://', url)
        print(url)
    try:
        response = requests.get(url=url, params=params, headers=headers, cookies=cookies)
    except Exception as e:
        log_tool.error('%s%s' % ('Exception url: ', url))
        log_tool.error(e)
        return ()
    time_consuming = response.elapsed.microseconds / 1000
    log_tool.info('----请求用时: %s 秒数' % time_consuming)
    return response


@logs
def post(url, params=None,data=None, files=None,json=None,  headers=None,  cookies=None):
    if not (url.startswith('http://') or url.startswith('https://')):
        url = '%s%s' % ('http://', url)
        print(url)
    try:
        response = requests.post(url, data=data, files=files, params=params, headers=headers, json=json,
                                 cookies=cookies)
    except Exception as e:
        log_tool.error('%s%s' % ('Exception url: ', url))
        log_tool.error(e)
        return ()
    # time_consuming为响应时间，单位为毫秒
    time_consuming = response.elapsed.microseconds / 1000
    log_tool.info('----请求用时: %s 秒数' % time_consuming)
    return response


@logs
def post_data(url, data=None, headers=None, cookies=None):
    if not (url.startswith('http://') or url.startswith('https://')):
        url = '%s%s' % ('http://', url)
        print(url)
    try:
        response = requests.post(url, data=data, headers=headers, cookies=cookies)
    except Exception as e:
        log_tool.error('%s%s' % ('Exception url: ', url))
        log_tool.error(e)
        return ()
    # time_consuming为响应时间，单位为毫秒
    time_consuming = response.elapsed.microseconds / 1000
    log_tool.info('----请求用时: %s 秒数' % time_consuming)
    return response


@logs
def post_params(url, params=None, headers=None, cookies=None):
    headers={}
    if not (url.startswith('http://') or url.startswith('https://')):
        url = '%s%s' % ('http://', url)
        print(url)
    try:
        response = requests.post(url, params=params, headers=headers, cookies=cookies)
    except Exception as e:
        log_tool.error('%s%s' % ('Exception url: ', url))
        log_tool.error(e)
        return ()
    # time_consuming为响应时间，单位为毫秒
    time_consuming = response.elapsed.microseconds / 1000
    log_tool.info('----请求用时: %s 秒数' % time_consuming)
    return response

@logs
def post_json(url, json=None, headers=None, cookies=None):
    if headers == None:
        headers={}
    headers['content-type']='application/json;;charset=UTF-8'
    if not (url.startswith('http://') or url.startswith('https://')):
        url = '%s%s' % ('http://', url)
        print(url)
    try:
        response = requests.post(url, headers=headers, json=json,cookies=cookies)
    except Exception as e:
        log_tool.error('%s%s' % ('Exception url: ', url))
        log_tool.error(e)
        return ()
    # time_consuming为响应时间，单位为毫秒
    time_consuming = response.elapsed.microseconds / 1000
    log_tool.info('----请求用时: %s 秒数' % time_consuming)
    return response


@logs
def post_file(url, files=None, headers=None, cookies=None):
    if not (url.startswith('http://') or url.startswith('https://')):
        url = '%s%s' % ('http://', url)
        print(url)
    try:
        response = requests.post(url=url, files=files, headers=headers, cookies=cookies)
    except Exception as e:
        log_tool.error('%s%s' % ('Exception url: ', url))
        log_tool.error(e)
        return ()
    # time_consuming为响应时间，单位为毫秒
    time_consuming = response.elapsed.microseconds / 1000
    log_tool.info('----请求用时: %s 秒数' % time_consuming)

    return response



@logs
def put(url, data, header=None, cookies=None):
    if not (url.startswith('http://') or url.startswith('https://')):
        url = '%s%s' % ('http://', url)
        log_tool.debug(url)

    try:
        if data is None:
            response = requests.put(url=url, headers=header, cookies=cookies)
        else:
            response = requests.put(url=url, params=data, headers=header, cookies=cookies)

    except Exception as e:
        log_tool.error('%s%s' % ('RequestException url: ', url))
        log_tool.error(e)
        return ()
    time_consuming = response.elapsed.microseconds / 1000
    log_tool.info('----请求用时: %s 秒数' % time_consuming)

    return response


def down_big_file(src_url, local_file):
    print('%s\n --->>>\n  %s' % (src_url, local_file))
    start_time = time.time()

    with requests.get(src_url, stream=True) as r:
        contentLength = int(r.headers['content-length'])
        line = 'content-length: %dB/ %.2fKB/ %.2fMB'
        line = line % (contentLength, contentLength / 1024, contentLength / 1024 / 1024)
        print(line)
        print('正在下载中..............')
        downSize = 0
        with open(local_file, 'wb') as f:
            for chunk in r.iter_content(8192):
                if chunk:
                    f.write(chunk)
                downSize += len(chunk)
                line = '%d KB/s - %.2f MB， 共 %.2f MB'
                line = line % (
                    downSize / 1024 / (time.time() - start_time), downSize / 1024 / 1024, contentLength / 1024 / 1024)
                print(line, end='\r')
                if downSize >= contentLength:
                    break
        timeCost = time.time() - start_time
        line = '共耗时: %.2f s, 平均速度: %.2f KB/s'
        line = line % (timeCost, downSize / 1024 / timeCost)
        print(line)


def copy_github_file(url, save_name):
    resp = get(url)
    body = resp.text
    with open(save_name, 'w', encoding='utf-8') as file:
        file.write(body)
