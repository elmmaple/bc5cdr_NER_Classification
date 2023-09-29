from config import CONFIG, update_config
from load_data import pd_read_json, read_json
from random_seed import update_seed_number
from check_cuda import check_cuda
TRAIN_PATH = CONFIG['TRAIN_PATH']
TEST_PATH = CONFIG['TEST_PATH']
MAPPING = CONFIG['MAPPING']
SEED_NUMBER = CONFIG['SEED_NUMBER']
#讀取資料
train_data = pd_read_json(TRAIN_PATH)
test_data = pd_read_json(TEST_PATH)
mapping = read_json(MAPPING)
#更新CONFIG參數
update_config('NUM_LABELS', len(mapping))
NUM_LABELS = CONFIG['NUM_LABELS']
#設定固定random_seed
update_seed_number(SEED_NUMBER)
#檢查cuda
check_cuda()
