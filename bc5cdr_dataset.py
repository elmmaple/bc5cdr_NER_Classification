from torch.utils.data import Dataset

class Bc5cdrDataset(Dataset):
    def __init__(self, data, tokenizer):
        self.data = data
        self.tokenizer = tokenizer

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        text = self.data["tokens"].iloc[idx]
        label = self.data["tags"].iloc[idx]
        # print(text,'text',type(text))
        # print(label,'label',type(label),'\n')
        return text, label
