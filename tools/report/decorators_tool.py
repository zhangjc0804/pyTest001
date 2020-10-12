import allure
from tools.report import log_tool
from tools.data import string_tool


# log decorator
def logs(func):
    def _func(*args, **kwargs):
        r= func(*args, **kwargs)
        request = "-------------------request-------------" \
                  "\n{0}\n{1}\n{2}".format(r.url, string_tool.dic_to_str(r.request.headers), r.request.body)
        log_tool.info(request)
        response = "---------------response----------------" \
                   "\n{0}\n{1}\n{2}".format(r.status_code, string_tool.dic_to_str(r.headers), r.text)
        log_tool.info(response)
        allure.attach(request,'request',allure.attachment_type.TEXT)
        allure.attach(response, 'response', allure.attachment_type.TEXT)
        return r
    return _func

# screenshot decorator
def shot(func):
    def function(*args, **kwargs):
        allure.attach(args[0].driver.get_screenshot_as_png(), args[1] + '之前', allure.attachment_type.PNG)
        i = 1
        res = None
        while(i <= 3):
            try:
                res = func(*args, **kwargs)
                break
            except :
                if i == 3:
                    allure.attach(args[0].driver.get_screenshot_as_png(), args[1] + '之后', allure.attachment_type.PNG)
                    raise
                i += 1
        allure.attach(args[0].driver.get_screenshot_as_png(), args[1] + '之后', allure.attachment_type.PNG)
        return res
    return function

