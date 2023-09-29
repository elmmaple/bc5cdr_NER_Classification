import pandas as pd
import json

def pd_read_json(path):
    return pd.read_json(path, lines = True)

def read_json(path):
    # 讀取 JSON 文件
    with open(path, 'r') as json_file:
        mapping = json.load(json_file)
    return mapping
