# 項目名稱：BC5CDR NER 分類

這是用於執行生物醫學文本命名實體識別（NER）分類的項目。使用了Hugging Face Transformers庫中的DistilBERT模型來進行訓練和評估。

## 快速入門

### 環境設定

確保你的Python環境已經設定並包含了以下相依性：

- Python 3.x
- PyTorch
- Transformers庫
- pandas
- tqdm
- seqeval

你可以使用以下指令安裝所需的Python函式庫：

```
bash
pipenv install torch transformers pandas tqdm scikit-learn seqeval 
```
## 資料準備
本計畫使用JSON格式的訓練和測試數據，以及一個JSON格式的標籤映射檔（mapping.json）。請確保你已經準備了這些文件，並將它們放在相應的資料夾中。

- data/
    - train.json
    - test.json
    - mapping.json
## 運行程式
python main.py