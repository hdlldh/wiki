import gzip as gz
from utils import *
from collections import Counter

input_file = 'split_wiki_20201201.dat.gz'
output_file = 'wiki_all_tokens_20201201.csv.gz'

count = 0
vocab = Counter()

with gz.open(input_file) as f:
    for line in f:
        count += 1
        tokenized = tokenize_sentence(line.decode('UTF-8').strip(), 3)
        for token in tokenized:
            if token.isdigit(): continue
            vocab[token] += 1
        if count % 1000000 == 0: print("%s M sentences have been processed." % (count // 1000000))

with gz.open(output_file, 'w') as f:
    f.write("token,count\n".encode('UTF-8'))
    for token, cnt in vocab.most_common():
        f.write(("%s,%s\n" % (token, cnt)).encode('UTF-8'))
