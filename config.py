from transformers import AutoTokenizer,AutoModelForTokenClassification
import datetime

PATH_CONFIG = {}
PATH_CONFIG['TRAIN_PATH'] = 'data/train.json'
PATH_CONFIG['TEST_PATH'] = 'data/test.json'
PATH_CONFIG['MAPPING'] = 'data/mapping.json'
PATH_CONFIG['RESULT_HTML'] = 'demo/result'

MODEL_CONFIG = {}
MODEL_CONFIG['SEED_NUMBER'] = 42
MODEL_CONFIG['MODEL_NAME'] = "distilbert-base-uncased"
MODEL_CONFIG['TOKENIZER'] = AutoTokenizer.from_pretrained(MODEL_CONFIG['MODEL_NAME'])
MODEL_CONFIG['MODEL'] = AutoModelForTokenClassification.from_pretrained
MODEL_CONFIG['TRAIN_BATCH_SIZE'] = 16
MODEL_CONFIG['TEST_BATCH_SIZE'] = 4
MODEL_CONFIG['LEARNING_RATE'] = 2e-5
MODEL_CONFIG['NUM_EPOCHS'] = 3
MODEL_CONFIG['NONE_NUMBER'] = -100
MODEL_CONFIG['MAX_LENGTH'] = 512

#rich樣式
RICH_CONFIG = {}
RICH_CONFIG['CUSTOM_THEME'] = {
        "good": 'green',
        "bad": 'red'
}
RICH_CONFIG['THUMBS_UP'] = ':thumbs_up: ' 
RICH_CONFIG['THUMBS_DOWN'] = ':thumbs_down: ' 
RICH_CONFIG['DATE_TIME'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def update_config(which_confug, title, content):
    which_confug[title] = content