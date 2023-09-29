CONFIG = {}
CONFIG['TRAIN_PATH'] = 'data/train.json'
CONFIG['TEST_PATH'] = 'data/test.json'
CONFIG['MAPPING'] = 'data/mapping.json'
CONFIG['SEED_NUMBER'] = 42
def update_config(title, content):
    CONFIG[title] = content