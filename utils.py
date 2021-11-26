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
        sentence = [start_token] * n + sentence + [end_token] * n
        sentence = tuple(sentence)

        for i in range(len(sentence) - n + 1):  # complete this line
            n_gram = sentence[i:i + n]
            if n_gram in n_grams:
                n_grams[n_gram] += 1
            else:
                n_grams[n_gram] = 1

    return n_grams


def estimate_forward_probability(
        word,
        previous_n_gram,
        n_gram_counts,
        n_plus1_gram_counts,
        vocabulary_size,
        k=1.0):
    """
    Estimate the probabilities of a next word using the n-gram counts with k-smoothing

    Args:
        word: next word
        previous_n_gram: A sequence of words of length n
        n_gram_counts: Dictionary of counts of n-grams
        n_plus1_gram_counts: Dictionary of counts of (n+1)-grams
        vocabulary_size: number of words in the vocabulary
        k: positive constant, smoothing parameter

    Returns:
        A probability
    """
    previous_n_gram = tuple(previous_n_gram)
    previous_n_gram_count = n_gram_counts.get(previous_n_gram, 0)
    denominator = previous_n_gram_count + k * vocabulary_size
    n_plus1_gram = previous_n_gram + (word,)
    n_plus1_gram_count = n_plus1_gram_counts.get(n_plus1_gram, 0)
    numerator = n_plus1_gram_count + k
    probability = numerator / denominator

    return probability


def estimate_backward_probability(
        word,
        next_n_gram,
        n_gram_counts,
        n_plus1_gram_counts,
        vocabulary_size,
        k=1.0):
    """
    Estimate the probabilities of a previous word using the n-gram counts with k-smoothing

    Args:
        word: previous word
        next_n_gram: A sequence of words of length n
        n_gram_counts: Dictionary of counts of n-grams
        n_plus1_gram_counts: Dictionary of counts of (n+1)-grams
        vocabulary_size: number of words in the vocabulary
        k: positive constant, smoothing parameter

    Returns:
        A probability
    """
    next_n_gram = tuple(next_n_gram)
    next_n_gram_count = n_gram_counts.get(next_n_gram, 0)
    denominator = next_n_gram_count + k * vocabulary_size
    n_plus1_gram = (word,) + next_n_gram
    n_plus1_gram_count = n_plus1_gram_counts.get(n_plus1_gram, 0)
    numerator = n_plus1_gram_count + k
    probability = numerator / denominator

    return probability
