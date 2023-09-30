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
- rich

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
```
python main.py
```
## 訓練模型
訓練模型，使用 DistilBERT 的預訓練模型
```
model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name, num_labels=NUM_LABELS)
```
## `collate_fn` 函數

`collate_fn` 函數是一個用於在 PyTorch DataLoader 中處理批次資料的自訂函數。 在這個特定的範例中，使用 `collate_fn` 函數來處理文字和標籤數據，以便它們可以傳遞給模型進行訓練。

### 輸入

`collate_fn` 函數接收一個批次（batch）的樣本作為輸入，其中每個樣本由兩部分組成：文字和標籤。 文字是一個文字序列，而標籤是與文字對應的命名實體識別標籤序列。

### 處理過程

1. **文字編碼**: 首先遍歷批次中的每個樣本，提取文字資料。 然後使用 Hugging Face Transformers 庫的 `tokenizer` 對文字進行編碼，將其轉換為模型可以理解的格式。 編碼後的文字會包括標記（tokens）、注意力掩碼（attention mask）等資訊。

2. **標籤對齊**: 在命名實體辨識任務中，文字通常會被分割成多個標記（tokens），而每個標記可能對應一個標籤（NER 標籤）。 為了確保標籤與編碼後的文字對齊，需要執行標籤對齊操作。 具體而言，使用 `align_labels_with_tokens` 函數，將原始的標籤序列與編碼後的文字標記進行對齊。 為每個標記分配一個對應的標籤，同時在特殊標記或跨越多個標記的實體上添加適當的標籤。 最終，獲得與編碼後的文字對齊的標籤序列。

3. **傳回結果**: 最後，`collate_fn` 函數傳回一個包含編碼後的文字和對齊後的標籤的資料結構，以便傳遞給模型進行訓練。 

## `align_labels_with_tokens` 函數

`align_labels_with_tokens` 函數是用於將原始標籤序列與文字標記對齊的輔助函數。 在命名實體辨識任務中，原始標籤序列通常以一種方式與文字標記對應，而模型需要一個對齊後的標籤序列，以便進行訓練和評估。

### 輸入

- `labels`: 原始的標籤序列，其中每個元素對應於一個標記的標籤。
- `word_ids`: 編碼後的文字標記（token）的索引序列，用來表示哪些標記屬於同一個字（word）。

### 處理過程

- 遍歷 `word_ids` 序列，這表示文字標記中的每個標記。
- 對於每個 `word_id`，檢查它是否與前一個標記不同（即是否表示一個新詞的開始）。
- 如果 `word_id` 不同於前一個標記，將對應位置的原始標籤新增到新的標籤序列中。 如果 `word_id` 為 `None`（表示特殊標記或跨越多個標記的實體），則將 `-100` 加入新的標籤序列中，以確保該位置處的標籤不參與模型的訓練。
- 如果 `word_id` 與前一個標記相同，表示它與前一個標記屬於同一個字，因此將相應位置的原始標籤新增至新的標籤序列中，以確保標籤對齊。

### 傳回結果

- 函數傳回一個與文字標記對齊的新標籤序列，該序列可以傳遞給模型進行訓練和評估。

這兩個函數的組合能夠有效地處理命名實體識別任務的數據，確保文字和標籤的正確對齊
## 訓練和評估
DataLoader 載入資料並進行訓練，然後評估模型的效能。使用 seqeval 函式庫來計算模型的Precision、recall和 F1 scores