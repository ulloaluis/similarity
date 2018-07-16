#!/usr/bin/env python3
# Python Version 3.7.0
import os                     # for file pathing
import re                     # regex for getting words
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm
from numpy import sin, cos, arccos, degrees

# Calculate the similarity between the texts of three writers and an
# unknown text in order to determine the most likely writer of that text.
def main():
    featureVec = createFeatureVec()

    f_mad = fileToString('madison.txt')
    f_jj = fileToString('jj.txt')
    f_ham = fileToString('hamilton.txt')
    f_unk = fileToString('unknown.txt') # unknown.txt file was written by hamilton

    madisonSim = getSimilarity(f_mad, f_unk, featureVec)
    jjSim = getSimilarity(f_jj, f_unk, featureVec)
    hamSim = getSimilarity(f_ham, f_unk, featureVec)

    plotSimilarity(madisonSim, jjSim, hamSim)

# Uses numpy and matplotlib to plot four vectors based on their cosine angles (similarity).
# The unknown vector is defined as the positive x-axis [0, 1] and the other vectors are
# plotted with respect to that vector. Vector lengths are the same.
def plotSimilarity(madisonSim, jjSim, hamSim):
    origin = [0, 0, 0, 0]
    vecXs = [1, madisonSim, jjSim, hamSim]     # x = rcos(theta) = 1*similarity
    vecYs = [0, sin(arccos(madisonSim)), sin(arccos(jjSim)), sin(arccos(hamSim))] # y=rsin(theta)=1*sin(cos^-1(similarity))
    vecColors = ['r', 'y', 'g', 'b']
    vecNames = ['Unknown Author', 'Madison', 'John Jay', 'Hamilton']

    # plot each individual vector, for loop necessary since label can only take one argument
    for origin, x, y, color, label in zip(origin, vecXs, vecYs, vecColors, vecNames):
        if vecNames[0] not in label:
            label = label + " with %.2f%% similarity and %.2f$^\circ$ angle difference" % (x*100, degrees(arccos(x)))
        plt.quiver(origin, origin, x, y, color=color,
                    label=label, angles='xy', scale_units='xy', scale=1)
    plt.title('Cosine Similarity to ' + vecNames[0])
    plt.legend(loc='upper left')
    plt.xlim(0, 1.5) # only [0, 1.0] is used, but need padding for labels
    plt.ylim(0, 1.5)
    plt.show()

# Count occurrences of a feature in text string by using the regex
# findall function to isolate each word, which we compare to the feature
def count_occurrences(text, feature):
    counter = 0
    for word in re.findall(r'\w+', text):
        if word == feature:
            counter += 1
    return counter

# return a Vector (list) with the number of occurrences for each
# feature in the corresponding index
def createDocVec(text, featureVec):
    result = []
    for feature in featureVec:
        result.append(count_occurrences(text, feature))
    return result

# Cosine Similarity, ternary used to catch divide by zero error
def getSimilarity(text1, text2, featureVec):
    docVec1 = createDocVec(text1, featureVec)
    docVec2 = createDocVec(text2, featureVec)
    dotP = np.dot(docVec1, docVec2)
    return 0 if dotP == 0 else dotP / (norm(docVec1)*norm(docVec2))

# Features that we are using to differentiate texts
def createFeatureVec():
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

# open: opens absolute path to filename, .join connects the following strings into a valid
# dir path, __file__ is absolute path to sim.py, .dirname(__file__) removes /sim.py part
# read caveat: have to remove \n's by replacing in order to properly read file to string
def fileToString(filename):
    text = ""
    with open(os.path.join(os.path.dirname(__file__), 'texts', filename), 'r') as file:
        text=file.read().replace('\n', '')
    return text

# Keeps program from running when imported as a module in another program
# Allows us to define main above the functions it requires, no function prototypes
if __name__ == "__main__":
    main()
