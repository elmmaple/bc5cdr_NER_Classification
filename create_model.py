class Create_Model():
    
    def __init__(self, tokenizer, model):
        self.tokenizer = tokenizer
        self.model = model
    
    def get_model(self):
        return self.model
    
    def get_tokenizer(self):
        return self.tokenizer
