import tensorflow_datasets as tfds
import gzip as gz
from utils import *

ds = tfds.load('wikipedia/20201201.en', split='train', shuffle_files=True)

output = "split_wiki_20201201.dat.gz"
count = 0
with gz.open(output, "w") as f:
    for example in ds:
        count += 1
        if count % 1000000 == 0: print("%s M articles have been processed." % (count // 1000000))
        data = example['text'].numpy().decode('UTF-8')
        sentences = split_to_sentences(data)
        sentences = [s for s in sentences if ascii_or_emoji_only(s)]
        for s in sentences:
            f.write((s + "\n").encode('UTF-8'))
