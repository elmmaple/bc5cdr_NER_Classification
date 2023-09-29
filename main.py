from config import CONFIG, update_config
from load_data import pd_read_json, read_json
from random_seed import update_seed_number
TRAIN_PATH = CONFIG['TRAIN_PATH']
TEST_PATH = CONFIG['TEST_PATH']
MAPPING = CONFIG['MAPPING']
SEED_NUMBER = CONFIG['SEED_NUMBER']
#讀取資料
train_data = pd_read_json(TRAIN_PATH)
test_data = pd_read_json(TEST_PATH)
mapping = read_json(MAPPING)
#設定固定random_seed
update_seed_number(SEED_NUMBER)
