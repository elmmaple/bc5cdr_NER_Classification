def align_labels_with_tokens(labels, word_ids, NONE_NUMBER):
    new_labels = []
    current_word = None
    for word_id in word_ids:
        if word_id != current_word:
            current_word = word_id
            label = NONE_NUMBER if word_id is None else labels[word_id]
            new_labels.append(label)
        elif word_id is None:
            new_labels.append(NONE_NUMBER)
        else:
            label = labels[word_id]
            new_labels.append(label)
    return new_labels
