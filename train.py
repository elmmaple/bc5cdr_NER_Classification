import torch
def train(model,optimizer, tqdm):
    model.train()
    for inputs, labels in tqdm:
        labels = torch.tensor(labels)
        # inputs = inputs.to("cuda:0")
        # labels = labels.to("cuda:0")
        optimizer.zero_grad()
        outputs = model(**inputs, labels = labels)
        loss = outputs.loss
        #記得加loss.item
        loss.backward()
        optimizer.step()