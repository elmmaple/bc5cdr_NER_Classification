CONFIG = {}
CONFIG['TRAIN_PATH'] = 'data/train.json'
CONFIG['TEST_PATH'] = 'data/test.json'
CONFIG['MAPPING'] = 'data/mapping.json'
def update_config(title, content):
    CONFIG[title] = content