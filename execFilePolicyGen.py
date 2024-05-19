"""

可执行文件 allow语句转换

"""

from dataStruct import AppPolicyInfo
from seProcess import findInDefault
import os

def InitAppExcFilePolicy(app_policy_info : AppPolicyInfo):
    if not os.path.exists(app_policy_info.path):
        return False
    # 转换为绝对路径
    absolute_path = os.path.abspath(app_policy_info.path)
    # 判断是否为可执行文件
    if os.access(absolute_path, os.X_OK):
        type_default, ok = findInDefault(app_policy_info.path)
        str_param = " "
        if os.path.isdir(absolute_path):
            str_param = " -d "
        else:
            str_param = " -- "
        # 判断是否有默认type
        if ok:
            app_policy_info.policy_exec_file += absolute_path + str_param + f"gen_context(system_u: object_r: {type_default}, s0)\n"
        else:
            app_policy_info.policy_exec_file += absolute_path + str_param + f"gen_context(system_u: object_r: {app_policy_info.security_exec_label}, s0)\n"
    return  True

"""
测试
def InitAppExcFilePolicy1(app_policy_info : AppPolicyInfo):
    type_default, ok = findInDefault(app_policy_info.path)
    # 判断是否有默认type
    if ok:
        app_policy_info.policy_exec_file += f"gen_context(system_u: object_r: {type_default}, s0)"
    else:
        app_policy_info.policy_exec_file += f"gen_context(system_u: object_r: {app_policy_info.security_exec_label}, s0)"
    return True

test = AppPolicyInfo(name= "test")
test.path = "/var/log/messsages"
test.security_exec_label = "test_exec_t"

ok = InitAppExcFilePolicy1(test)
if ok:
    print(test.policy_exec_file)
    
"""