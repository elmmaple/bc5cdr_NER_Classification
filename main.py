from config import CONFIG, update_config
from load_data import pd_read_json, read_json
from random_seed import update_seed_number
from check_cuda import check_cuda
from create_model import Create_Model
from bc5cdr_dataset import Bc5cdrDataset
from create_dataloader import create_dataloader
import torch
from collate_function import collate_fn
TRAIN_PATH = CONFIG['TRAIN_PATH']
TEST_PATH = CONFIG['TEST_PATH']
MAPPING = CONFIG['MAPPING']
SEED_NUMBER = CONFIG['SEED_NUMBER']
TOKENIZER = CONFIG['TOKENIZER']
MODEL = CONFIG['MODEL']
MODEL_NAME = CONFIG['MODEL_NAME']
TRAIN_BATCH_SIZE = CONFIG['TRAIN_BATCH_SIZE']
TEST_BATCH_SIZE = CONFIG['TEST_BATCH_SIZE']
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
device = torch.device("cuda:0" if torch.cuda.is_available() else 'cpu')
#建立模型
establish_model = Create_Model(TOKENIZER, MODEL(MODEL_NAME, num_labels = NUM_LABELS))
model = establish_model.get_model()
tokenizer = establish_model.get_tokenizer()
# model.to(device)
#建立dataset
train_dataset = Bc5cdrDataset(train_data, tokenizer)
my_collate_funtion = lambda batch: collate_fn(batch, tokenizer)
# 創建包裝函數，將 extra_variable 傳遞給 collate_fn
train_loader = create_dataloader(train_dataset, TRAIN_BATCH_SIZE, shuffle = True, collate_fn = my_collate_funtion)

# 進行評估
test_dataset = Bc5cdrDataset(test_data, tokenizer)
test_loader = create_dataloader(test_dataset,TEST_BATCH_SIZE, shuffle = False ,collate_fn = my_collate_funtion)
