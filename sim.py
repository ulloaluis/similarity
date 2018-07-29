#!/usr/bin/env python3
# Python Version 3.7.0
import os                     # for file pathing
import re                     # regex for getting words
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm
from numpy import sin, cos, arccos, degrees

def main():
    """
    Calculate the similarity between the texts of three writers and an
    unknown text in order to determine the most likely writer of that text.
    """
    feature_vec = create_feature_vec()

    f_mad = file_to_string('madison.txt')
    f_jj = file_to_string('jj.txt')
    f_ham = file_to_string('hamilton.txt')
    f_unk = file_to_string('unknown.txt') # unknown.txt file was written by hamilton

    mad_sim = get_similarity(f_mad, f_unk, feature_vec)
    jj_sim = get_similarity(f_jj, f_unk, feature_vec)
    ham_sim = get_similarity(f_ham, f_unk, feature_vec)

    plot_similarity(mad_sim, jj_sim, ham_sim)

def plot_similarity(mad_sim, jj_sim, ham_sim):
    """
    inputs: similarity values for madison, john jay, and hamilton
    
    Uses numpy and matplotlib to plot four vectors based on their cosine angles (similarity).
    The unknown vector is defined as the positive x-axis [0, 1] and the other vectors are
    plotted with respect to that vector. Vector lengths are the same.
    """
    origin = [0, 0, 0, 0]
    vecs_x = [1, mad_sim, jj_sim, ham_sim]     # x = rcos(theta) = 1*similarity
    vecs_y = [0, sin(arccos(mad_sim)), sin(arccos(jj_sim)), sin(arccos(ham_sim))] # y=rsin(theta)=1*sin(cos^-1(similarity))
    vec_colors = ['r', 'y', 'g', 'b']
    vec_names = ['Unknown Author', 'Madison', 'John Jay', 'Hamilton']

    # plot each individual vector, for loop necessary since label can only take one argument
    for origin, x, y, color, label in zip(origin, vecs_x, vecs_y, vec_colors, vec_names):
        if vec_names[0] not in label:
            label = label + " with %.2f%% similarity and %.2f$^\circ$ angle difference" % (x*100, degrees(arccos(x)))
        plt.quiver(origin, origin, x, y, color=color,
                    label=label, angles='xy', scale_units='xy', scale=1)
    plt.title('Cosine Similarity to ' + vec_names[0])
    plt.legend(loc='upper left')
    plt.xlim(0, 1.5) # only [0, 1.0] is used, but need padding for labels
    plt.ylim(0, 1.5)
    plt.show()

def count_occurrences(text, feature):
    """
    inputs: feature that is searched for inside text
    
    Count occurrences of a feature in text string by using the regex
    findall function to isolate each word, which we compare to the feature
    """
    found_occurrences = re.findall(r'\w+', text)
    return len([word for word in found_occurrences if word == feature])

def create_doc_vec(text, feature_vec):
    """ 
    inputs: feature_vec, which is the features to be searched for, 
            and text, which is the text being searched
            
    returns a vector (list) with the number of occurrences for each
    feature in the corresponding index
    """
    return [count_occurrences(text, feature) for feature in feature_vec]

# Cosine Similarity
def get_similarity(text_1, text_2, feature_vec):
    """ 
    inputs: two texts that are compared and the features used in comparison
    
    returns a similarity value between two texts by creating
    vectors that document the occurrence of features in feature_vec
    and then taking the dot products (ternary catches divide by zero)
    """
    doc_vec_1 = create_doc_vec(text_1, feature_vec)
    doc_vec_2 = create_doc_vec(text_2, feature_vec)
    dot_p = np.dot(doc_vec_1, doc_vec_2)
    return 0 if dot_p == 0 else dot_p / (norm(doc_vec_1)*norm(doc_vec_2))

def create_feature_vec():
    """ Features that we are using to differentiate texts """
    return ["a", "about", "above", "after", "again", "against", "all",
                "am", "an", "and", "any", "are", "aren't", "as", "at", "be",
                "because", "been", "before", "being", "below", "between", "both",
                "but", "by", "can't", "cannot", "could", "couldn't", "did", "didn't",
                "do", "does", "doesn't", "doing", "don't", "down", "during", "each",
                "few", "for", "from", "further", "had", "hadn't", "has", "hasn't",
                "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her",
                "here", "here's", "hers", "herself", "him", "himself", "his", "how",
                "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is",
                "isn't", "it", "it's", "its", "itself", "let's", "me", "more", "most",
                "mustn't", "my", "myself", "no", "nor", "not", "of", "off", "on", "once",
                "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over",
                "own", "same", "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't",
                "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them",
                "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're",
                "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was",
                "wasn't", "we", "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when",
                "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with",
                "won't", "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours",
                "yourself", "yourselves", "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".",
                "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]

def file_to_string(filename):
    """
    inputs: file to be converted to string
    
    open: opens absolute path to filename, .join connects the following strings into a valid
    dir path, __file__ is absolute path to sim.py, .dirname(__file__) removes /sim.py part
    read caveat: have to remove \n's by replacing in order to properly read file to string
    """
    text = ""
    with open(os.path.join(os.path.dirname(__file__), 'texts', filename), 'r') as file:
        text=file.read().replace('\n', '')
    return text

# Keeps program from running when imported as a module in another program
# Allows us to define main above the functions it requires, no function prototypes
if __name__ == "__main__":
    """
    Keeps program from running when imported as a module in another program
    Allows us to define main above the functions it requires, no function prototypes
    """
    main()
