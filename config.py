from transformers import AutoTokenizer,AutoModelForTokenClassification

CONFIG = {}
CONFIG['TRAIN_PATH'] = 'data/train.json'
CONFIG['TEST_PATH'] = 'data/test.json'
CONFIG['MAPPING'] = 'data/mapping.json'
CONFIG['SEED_NUMBER'] = 42
CONFIG['MODEL_NAME'] = "distilbert-base-uncased"
CONFIG['TOKENIZER'] = AutoTokenizer.from_pretrained(CONFIG['MODEL_NAME'])
CONFIG['MODEL'] = AutoModelForTokenClassification.from_pretrained
def update_config(title, content):
    CONFIG[title] = content