"""

公有文件和私有文件 allow语句转换

"""
from dataStruct import AppPolicyInfo
import seProcess

"""
(已实现)可以使用seProcess.findInDefault寻找默认type和判断公有私有
seProcess.findInDefault有两个返回值：type 和 ok。
当搜索到默认type时，type 为默认type，ok 为True
当未搜索到默认type时，type 为None，ok 为False
"""
def InitAppFilePolicy(app_policy_info : AppPolicyInfo):
    pass