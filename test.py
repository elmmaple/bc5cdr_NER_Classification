import torch
from seqeval.metrics import classification_report
from lib.rich_lib import save_and_print
from config import RICH_CONFIG

def test(model, tqdm, NUM_LABELS, NONE_NUMBER, mapping):
    all_predictions = []
    all_labels = []
    model.eval()
    # torch.no_grad 確保不會因為不必要的計算而增加計算和記憶體負擔，減少內存使用，提高效率
    with torch.no_grad():
        for inputs, labels in tqdm:
            # inputs = inputs.to("cuda:0")
            labels = torch.tensor(labels).view(-1)
            # labels = labels.to("cuda:0")
            outputs = model(**inputs, labels = labels)
            predictions = torch.argmax(outputs.logits.view(-1, NUM_LABELS), dim = 1)
            labels = torch.tensor(labels)
            new_labels, new_predictions = zip(*[(label, prediction) for label, prediction in zip(labels, predictions) if label != NONE_NUMBER])
            all_predictions.extend(torch.tensor(new_predictions).cpu().numpy())
            all_labels.extend(torch.tensor(new_labels).cpu().numpy())
        new_all_predictions = [mapping[str(num)] for num in all_predictions]
        new_all_labels = [mapping[str(num)] for num in all_labels]
        save_and_print(classification_report([new_all_predictions], [new_all_labels]), 'bold black on dark_sea_green1')
    