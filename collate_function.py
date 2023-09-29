from align_labels_with_tokens import align_labels_with_tokens

def collate_fn(batch, tokenizer, NONE_NUMBER, MAX_LENGTH):
    tokens = [item[0] for item in batch]
    tags = [item[1] for item in batch]
    tokens = tokenizer.batch_encode_plus(tokens, padding = True, truncation = True, max_length = MAX_LENGTH, return_tensors = "pt", is_split_into_words = True)
    padded_tags = []
    for i, labels in enumerate(tags):
        word_ids = tokens.word_ids(i)
        padded_tags.append(align_labels_with_tokens(labels, word_ids, NONE_NUMBER))
    return tokens, padded_tags