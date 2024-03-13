import json

from prettytable import PrettyTable
from datetime import datetime
from ..util import is_fuzzy_key

RESP_OUTPUT_KEY = {
    "bizsystems": "items",
    "target": "items",
    "targettype": "items",
}

def find_list_fields(resp={}):
    for k in resp:
        if isinstance(resp[k], list):
            return k
    return None


def list_output(asset_name, output_fields=[], resp={}):
    total = resp.get("total")
    if total is None:
        total = 0
    print(f"we have {total} {asset_name} in total")
    
    # 检查白名单有无这个字段的定义
    assetkey = is_fuzzy_key(asset_name, value_map=RESP_OUTPUT_KEY)
    key = None
    
    # 优先查看返回结果里是否有类似命名的字段
    if assetkey is None:
        key = is_fuzzy_key(asset_name, value_map=resp)
    else:
        key = RESP_OUTPUT_KEY[assetkey]
    
    # 如果最终没有找到类似的字段，则找一个list字段
    if key is None:
        key = find_list_fields(resp)

    # 如果返回结果为空
    if key is None or not isinstance(resp[key], list) or len(resp[key]) <= 0:
        return None
    
    fields = output_fields
    if len(fields) <= 0:
        for k in resp[key][0]:
            fields.append(k)
    table = PrettyTable(fields)
    for row in resp[key]:
        value = []
        for k in fields:
            if k in row:
                if k.lower().endswith("time"):
                    dt_object = datetime.fromtimestamp(row[k]/1000)
                    value.append(dt_object.strftime('%Y-%m-%d %H:%M:%S'))
                elif isinstance(row[k], str):
                    value.append(row[k])
                else:
                    value.append(json.dumps(row[k]))
            else:
                value.append(None)
        table.add_row(value)
    return table


def describe_output(asset_name, resp={}):
    total = resp.get("total")
    if total is None or total <= 0:
        return None

    # 检查白名单有无这个字段的定义
    assetkey = is_fuzzy_key(asset_name, value_map=RESP_OUTPUT_KEY)
    resultField = None

    # 优先查看返回结果里是否有类似命名的字段
    if assetkey is None:
        resultField = is_fuzzy_key(asset_name, value_map=resp)
    else:
        resultField = RESP_OUTPUT_KEY[assetkey]

    # 如果最终没有找到类似的字段，则找一个list字段
    if resultField is None:
        resultField = find_list_fields(resp)

    # 如果返回结果为空
    if resultField is None or not isinstance(resp[resultField], list) or len(resp[resultField]) <= 0:
        return None

    fields = []
    if len(fields) <= 0:
        for k in resp[resultField][0]:
            fields.append((k, type(resp[resultField][0][k])))
    table = PrettyTable(["fields", "type"])
    for f in fields:
        table.add_row([f[0], f[1]])
    return table
