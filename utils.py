import re
import nltk
from collections import Counter

nltk.download('punkt')


def split_to_sentences(data):
    """
    Split data by linebreak "\n"

    Args:
        data: str

    Returns:
        A list of sentences
    """

    sentences = data.split('\n')
    sentences = [s.strip() for s in sentences]
    sentences = [s for s in sentences if len(s) > 0]
    return sentences


def tokenize_sentence(sentence, min_tokens=1):
    """
    Tokenize sentences into tokens (words)

    Args:
        sentence: List of strings
        min_tokens: Minimum number of tokens

    Returns:
        List of tokens
    """

    sentence = sentence.lower()
    sentence = re.sub(r"[^a-zA-Z0-9.?! ]+", " ", sentence)
    if not sentence.strip(): return []
    tokenized = nltk.word_tokenize(sentence)
    if len(tokenized) >= min_tokens: return tokenized
    return []


def ascii_or_emoji_only(sentence):
    if sentence.isascii() or re.search(r"([^\u0000-\uFFFF])+", sentence):
        return True
    else:
        return False


def remove_dynamic_symobl(sentence):
    sentence = re.sub(r"^{{dynamic}}\W*|\W*{{dynamic}}$", "", sentence)
    sentence = re.sub(r"\W*{{dynamic}}\W*", " ", sentence)
    return sentence


def replace_oov_words_by_unk(tokenized_sentence, vocabulary, unknown_token="<unk>"):
    """
    Replace words not in the given vocabulary with '<unk>' token.

    Args:
        tokenized_sentence: List of strings
        vocabulary: List of strings that we will use
        unknown_token: A string representing unknown (out-of-vocabulary) words

    Returns:
        List of strings, with words not in the vocabulary replaced
    """

    vocabulary = set(vocabulary)

    replaced_sentence = []
    for token in tokenized_sentence:
        if token in vocabulary:
            replaced_sentence.append(token)
        else:
            replaced_sentence.append(unknown_token)

    return replaced_sentence


def count_n_grams(data, n, start_token='<s>', end_token='<e>'):
    """
    Count all n-grams in the data

    Args:
        data: List of lists of words
        n: number of words in a sequence

    Returns:
        A dictionary that maps a tuple of n-words to its frequency
    """

    n_grams = {}

    for sentence in data:
        sentence = [start_token] * (n-1) + sentence + [end_token] * (n-1)
        sentence = tuple(sentence)

        for i in range(len(sentence) - n + 1):  # complete this line
            n_gram = sentence[i:i + n]
            if n_gram in n_grams:
                n_grams[n_gram] += 1
            else:
                n_grams[n_gram] = 1

    return n_grams
