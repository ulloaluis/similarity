# similarity
Using cosine similarity to determine text author

The purpose of this program is to use cosine similarity (dot product of A and B / product of magnitudes) to determine the author of a Federalist Paper. A vector (list) is created for each of Alexander Hamilton, James Madison, and John Jay, in which each index contains an integer indicating the number of occurrences for a specific word (which corresponds to the index of a different vector, featureVec). The number of occurrences are counted from corresponding files that contain writing done by that particular author. A vector is also created for a text with an unknown author, and cosine similarity is then determined between each 'known author vector' and the 'unknown author vector.' The higher the similarity (~1.0 is exact), the higher the chance that both texts have the same author. In the case of the Federalist Papers example this program exhibits, the highest similarity is Hamilton with ~98%, who did indeed write the other text.


This project is based on a standard C++ assignment (Stylometry) from CS 106L. 

This rendition is done in Python and contains added features both for visualization and functionality. Program uses Numpy for linear algebra functionality (but does not use the ndarray class since the normal list proved to be more efficient here) and the regex library is used to refine the file parsing.

In-progress additions:
1) Adding a graphing function for visualizing the data

Potential additions:
1) Other natural language processing techniques to refine program functionality
2) Other cosine similarity applications
