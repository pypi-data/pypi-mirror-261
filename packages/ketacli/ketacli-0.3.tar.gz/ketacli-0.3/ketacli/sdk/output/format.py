import json

from prettytable import PrettyTable
from datetime import datetime

def to_string(key, value):
    if value is None:
        return "None"
    if key.lower().endswith("time") and isinstance(value, int):
        dt_object = datetime.fromtimestamp(value/1000)
        return dt_object.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(value, str):
        return value
    elif isinstance(value, int):
        return value
    elif isinstance(value, bool):
        return value
    else:
        return json.dumps(value, ensure_ascii=False)

def records_to_table(records=[], fields=[]):
    if len(fields) <= 0:
        for k in records[0]:
            fields.append(k)
    table = PrettyTable(fields)
    for row in records:
        value = []
        for k in fields:
            if k in row:
                value.append(to_string(k, row[k]))
            else:
                value.append(None)
        table.add_row(value)
    return table


def make_table(header=[], rows=[]):
    table = PrettyTable(header)
    table.add_rows(rows)
    return table
    