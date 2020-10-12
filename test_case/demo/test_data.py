# -*- coding: utf-8 -*-
# @Project: guoya-api-test
# @Author: 小吴
# @Email: wuling@guoyasoft.com
# @Weichat: 875955899
# @Create time: 2019/11/24 9:50
import pytest

data = [("张国立", "邓婕"), ("邓超", "孙俪"), ("冯绍峰", "赵丽颖"), ("绿巨人", "黑寡妇")]


@pytest.mark.parametrize('a,b', data)
def test_one(a, b):
    print("--------- start ----------")
    print("男: %s —> 女: %s" % (a, b))
    print("------- end ---------")

@pytest.mark.parametrize('a,b', data,ids=['case1','case2','case3','case4'])
def test_two(a, b):
    print("--------- start ----------")
    print("男: %s —> 女: %s" % (a, b))
    print("------- end ---------")


