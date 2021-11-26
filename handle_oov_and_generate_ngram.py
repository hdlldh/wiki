import pandas as pd
import gzip as gz
from utils import *

date_str = "20201201"
token_file = f"wiki_all_tokens_{date_str}.csv.gz"
subject_file = f"split_wiki_{date_str}.dat.gz"
unigram_file = f"wiki_unigram_{date_str}.csv.gz"
bigram_file = f"wiki_bigram_{date_str}.csv.gz"
trigram_file = f"wiki_trigram_{date_str}.csv.gz"

start_token = '<s>'
end_token = '<e>'
unknown_token = '<unk>'

all_tokens = pd.read_csv(token_file)
all_tokens = all_tokens[~all_tokens['token'].isnull()]
min_freq = 10
vocab = set(all_tokens[all_tokens['count'] >= min_freq]['token'])

print(len(vocab))

replaced_tokenized_sentences = []
count = 0
with gz.open(subject_file) as f:
    for line in f:
        count += 1
        tokenized_sentence = tokenize_sentence(line.decode('UTF-8').strip())
        replaced_tokenized_sentence = replace_oov_words_by_unk(tokenized_sentence, vocab, unknown_token)
        replaced_tokenized_sentences.append(replaced_tokenized_sentence)

unigram_count = count_n_grams(replaced_tokenized_sentences, 1, start_token, end_token)
with gz.open(unigram_file, 'w') as f:
    for k, v in unigram_count.items():
        w1 = k[0]
        f.write(f"{w1},{v}\n".encode('UTF-8'))

bigram_count = count_n_grams(replaced_tokenized_sentences, 2, start_token, end_token)
with gz.open(bigram_file, 'w') as f:
    for k, v in bigram_count.items():
        w1, w2 = k
        f.write(f"{w1},{w2},{v}\n".encode('UTF-8'))

trigram_count = count_n_grams(replaced_tokenized_sentences, 3, start_token, end_token)
with gz.open(trigram_file, 'w') as f:
    for k, v in trigram_count.items():
        w1, w2, w3 = k
        f.write(f"{w1},{w2},{w3},{v}\n".encode('UTF-8'))
