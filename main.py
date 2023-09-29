from config import CONFIG, update_config
from load_data import pd_read_json, read_json
TRAIN_PATH = CONFIG['TRAIN_PATH']
TEST_PATH = CONFIG['TEST_PATH']
MAPPING = CONFIG['MAPPING']
#讀取資料
train_data = pd_read_json(TRAIN_PATH)
test_data = pd_read_json(TEST_PATH)
mapping = read_json(MAPPING)
