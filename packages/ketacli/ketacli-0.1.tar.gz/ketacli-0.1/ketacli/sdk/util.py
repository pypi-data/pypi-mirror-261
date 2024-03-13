

def is_fuzzy_key(key, value_map={}):
    """
    检查key或者key的复数形式在map中，并返回最终map中的key
    """
    newkey = key.lower() 
    if newkey in value_map:
        return newkey
    if newkey.endswith('s'):
        newkey = newkey[:-1]
    else:
        newkey = newkey + 's'
    if newkey in value_map:
        return newkey
    return None