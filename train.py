import torch
from lib.rich_lib import save_and_print
def train(model,optimizer, tqdm):
    model.train()
    for inputs, labels in tqdm:
        labels = torch.tensor(labels)
        # inputs = inputs.to("cuda:0")
        # labels = labels.to("cuda:0")
        optimizer.zero_grad()
        outputs = model(**inputs, labels = labels)
        loss = outputs.loss
        save_and_print('loss : ' + str(loss) , 'bold red')
        #記得加loss.item
        loss.backward()
        optimizer.step()