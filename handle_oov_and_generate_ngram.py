import pandas as pd
import gzip as gz
from utils import *

token_file = "wiki_all_tokens.csv.gz"
subject_file = "split_wiki_20201201.dat.gz"

all_tokens = pd.read_csv(token_file)
min_freq = 10
vocab = set(all_tokens[all_tokens['count'] >= min_freq]['token'])
print(len(vocab))

replaced_tokenized_sentences = []
with gz.open(subject_file) as f:
    for line in f:
        tokenized_sentence = tokenize_sentence(line.decode('UTF-8').strip())
        replaced_tokenized_sentence = replace_oov_words_by_unk(tokenized_sentence, vocab)
        replaced_tokenized_sentences.append(replaced_tokenized_sentence)

bigram = count_n_grams(replaced_tokenized_sentences, 2)
print(bigram.most_common(100))

trigram = count_n_grams(replaced_tokenized_sentences, 3)
print(trigram.most_common(100))