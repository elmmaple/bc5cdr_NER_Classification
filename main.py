from config import MODEL_CONFIG, PATH_CONFIG, RICH_CONFIG, update_config
from load_data import pd_read_json, read_json
from random_seed import update_seed_number
from check_cuda import check_cuda
from create_model import Create_Model
from bc5cdr_dataset import Bc5cdrDataset
from create_dataloader import create_dataloader
import torch
from collate_function import collate_fn
from tqdm.auto import tqdm  # 引入tqdm庫
from train import train
from test import test
from lib.rich_lib import save_and_print, console

TRAIN_PATH = PATH_CONFIG['TRAIN_PATH']
TEST_PATH = PATH_CONFIG['TEST_PATH']
MAPPING = PATH_CONFIG['MAPPING']
RESULT_HTML = PATH_CONFIG['RESULT_HTML']

SEED_NUMBER = MODEL_CONFIG['SEED_NUMBER']
TOKENIZER = MODEL_CONFIG['TOKENIZER']
MODEL = MODEL_CONFIG['MODEL']
MODEL_NAME = MODEL_CONFIG['MODEL_NAME']
TRAIN_BATCH_SIZE = MODEL_CONFIG['TRAIN_BATCH_SIZE']
TEST_BATCH_SIZE = MODEL_CONFIG['TEST_BATCH_SIZE']
LEARNING_RATE = MODEL_CONFIG['LEARNING_RATE']
NUM_EPOCHS = MODEL_CONFIG['NUM_EPOCHS']
NONE_NUMBER = MODEL_CONFIG['NONE_NUMBER']
MAX_LENGTH = MODEL_CONFIG['MAX_LENGTH']

# 日期和时间
CURRENT_DATE_TIME = RICH_CONFIG['DATE_TIME']
CUSTOM_THEME = RICH_CONFIG['CUSTOM_THEME']
THUMBS_UP = RICH_CONFIG['THUMBS_UP']    
#讀取資料
train_data = pd_read_json(TRAIN_PATH)
test_data = pd_read_json(TEST_PATH)
mapping = read_json(MAPPING)
#更新CONFIG參數
update_config(MODEL_CONFIG, 'NUM_LABELS', len(mapping))
NUM_LABELS = MODEL_CONFIG['NUM_LABELS']
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
my_collate_funtion = lambda batch: collate_fn(batch, tokenizer, NONE_NUMBER, MAX_LENGTH)
# 創建包裝函數，將 extra_variable 傳遞給 collate_fn
train_loader = create_dataloader(train_dataset, TRAIN_BATCH_SIZE, shuffle = True, collate_fn = my_collate_funtion)

# 進行評估
test_dataset = Bc5cdrDataset(test_data, tokenizer)
test_loader = create_dataloader(test_dataset,TEST_BATCH_SIZE, shuffle = False ,collate_fn = my_collate_funtion)

optimizer = torch.optim.AdamW(model.parameters(), lr = LEARNING_RATE)
for epoch in tqdm(range(NUM_EPOCHS)):
    train_loader_tqdm = tqdm(train_loader, desc = f"Epoch {epoch + 1}")
    if epoch == 1 :
        console(THUMBS_UP + '測試結果如下')
        console(str(CURRENT_DATE_TIME))
    save_and_print('Epoch: ' + str(epoch), 'bold red')
    train(model, optimizer, train_loader_tqdm)
    #模型切換到評估模式
    test_loader_tqdm = tqdm(test_loader, desc = f"Evaluation{epoch + 1}")
    test(model, test_loader_tqdm, NUM_LABELS, NONE_NUMBER, mapping)
# add_style()
content_to_append = '<style> .r1 {color: red} .r2 {color: green} </style>'
with open(RESULT_HTML + str(CURRENT_DATE_TIME) +'.html', "a", encoding="utf-8") as html_file:
    html_file.write(content_to_append)
print('-'*100)
    