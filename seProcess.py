"""

相关数据处理

"""


import json
import re

type_default_path = r"save_default"

"""寻找默认type也可以判断是否为公有还是私有，待完善"""
def findInDefault(fileName : str):
    # 加载json文件
    with open(type_default_path, 'r', encoding="UTF-8") as f:
        file_data = json.load(f)
    # 分割，寻找默认簇
    file_name_split = fileName.split('/')
    if len(file_name_split) > 1:
        file_class = file_name_split[1]
    else:
        file_class = file_name_split[0]
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