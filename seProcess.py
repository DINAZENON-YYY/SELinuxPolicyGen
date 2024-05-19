"""

相关数据处理

"""


from dataStruct import AppPolicyInfo
import json
import re

type_default_path = r"save_default"
def simpleGenerateSecurityLabel(appPolicyInfo: AppPolicyInfo):
    appPolicyInfo.security_label = appPolicyInfo.name + "_t"

def SimpleGenerateExecSecurityLabel(appPolicyInfo: AppPolicyInfo):
    appPolicyInfo.security_exec_label = appPolicyInfo.name + "_exe_t"

def simpleGenerateDataSecurityLabel(appPolicyInfo: AppPolicyInfo):
    appPolicyInfo.security_data_label = appPolicyInfo.name + "_data_t"

"""寻找默认type也可以判断是否为公有还是私有，待完善"""
def findInDefault(fileName : str):
    # 加载json文件
    with open(type_default_path, 'r', encoding="UTF-8") as f:
        file_data = json.load(f)
    # 分割，寻找默认簇
    file_name_split = fileName.split('/')
    file_class = file_name_split[1]
    # 判断是否为默认type
    if file_class not in file_data:
        return None, False
    file_type_set = file_data[file_class]
    res_type = None
    res_ok = False
    # 通过正则表达式匹配默认type
    for k,v in file_type_set.items():
        pattern = k
        match = re.search(pattern, fileName)
        if match:
            res_type = v
            res_ok = True
            break
    return res_type, res_ok

"""
测试
type, ok = findInDefault("/var/log/messsages")
print(type)
"""