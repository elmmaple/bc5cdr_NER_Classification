from transformers import AutoTokenizer,AutoModelForTokenClassification

CONFIG = {}
CONFIG['TRAIN_PATH'] = 'data/train.json'
CONFIG['TEST_PATH'] = 'data/test.json'
CONFIG['MAPPING'] = 'data/mapping.json'
CONFIG['SEED_NUMBER'] = 42
CONFIG['MODEL_NAME'] = "distilbert-base-uncased"
CONFIG['TOKENIZER'] = AutoTokenizer.from_pretrained(CONFIG['MODEL_NAME'])
CONFIG['MODEL'] = AutoModelForTokenClassification.from_pretrained
CONFIG['TRAIN_BATCH_SIZE'] = 16
CONFIG['TEST_BATCH_SIZE'] = 4
CONFIG['LEARNING_RATE'] = 2e-5
CONFIG['NUM_EPOCHS'] = 20
CONFIG['NONE_NUMBER'] = -100
CONFIG['MAX_LENGTH'] = 512

#rich樣式
CONFIG['CUSTOM_THEME'] = {
        "good": 'green',
        "bad": 'red'
    }
CONFIG['THUMBS_UP'] = ':thumbs_up: ' 

def update_config(title, content):
    CONFIG[title] = content