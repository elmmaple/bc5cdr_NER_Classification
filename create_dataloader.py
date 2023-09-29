from torch.utils.data import DataLoader

def create_dataloader(train_dataset, batch_size, shuffle, collate_fn):
    return DataLoader(train_dataset, batch_size = batch_size, shuffle = shuffle, collate_fn=collate_fn)