"""

相关数据处理

"""


import json
import re

type_default_path = r"save_default_test"

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
    length = 0
    for k,v in file_type_set.items():
        pattern = k
        #if re.match(pattern, fileName) and re.match(pattern, fileName).group() == fileName:
        #    return v, True
        match = re.search(pattern, fileName)
        if match:
            non_regex_pattern = re.sub(r'\(.*\)', '', pattern)
            # print(non_regex_pattern, v)
            if len(non_regex_pattern) > length:
                length = len(non_regex_pattern)
                res_type = v
                res_ok = True
    return res_type, res_ok



# type, ok = findInDefault("/var/log/message")
# print(type)
