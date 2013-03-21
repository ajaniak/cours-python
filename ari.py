import os
import sys

from pattern.en import tokenize


def ARI(n_chars, n_words, n_sents):
    "Compute the Automated Readability Index."
    return 4.71 * (n_chars / n_words) + 0.5 * (n_words / n_sents) - 21.43

def read_text(filename):
    with open(filename) as infile:
        return tokenize(infile.read())

def extract_counts(text):
    n_chars, n_words, n_sents = 0, 0, 0
    for sentence in text:
        n_sents += 1
        words = sentence.split()
        for word in words:
            n_words += 1
            n_chars += len(word)
    return n_chars, n_words, n_sents

def compute_ARI(text):
    n_chars, n_words, n_sents = extract_counts(text)
    return ARI(n_chars, n_words, n_sents)

if __name__ == '__main__':
    for filename in os.listdir('data/gutenberg'):
        print 'ARI %s: %.3f' % (
            filename, compute_ARI(read_text(os.path.join('data/gutenberg', filename))))
    