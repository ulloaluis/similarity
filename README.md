# similarity: application of cosine similarity in author identification

A Python script for determining the author of a federalist paper. Can also be used in general to see the similarity between multiple texts/authors.

## Details
The purpose of this program is to use [cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity) to determine the author of a Federalist Paper. A vector (list) is created for each of the writers (Alexander Hamilton, James Madison, and John Jay) and each index contains an integer indicating the number of occurrences for a specific word (which corresponds to the index of a different vector, featureVec). The number of occurrences are counted from corresponding files that contain writing done by that particular author. A vector is also created for a text with an unknown author and cosine similarity is then determined between each 'known author vector' and the 'unknown author vector.' The higher the similarity (~1.0 is exact), the higher the chance that both texts have the same author. In the case of the Federalist Papers example this program exhibits, the highest similarity is Hamilton with ~98%, who did indeed write the other text.

This project is based on a standard C++ assignment (Stylometry) from CS 106L (Stanford University). 

This rendition is done in Python and contains added features for visualization and functionality. Program uses Numpy for linear algebra functionality (but does not use the ndarray class since the normal list proved to be more efficient here) and the regex library is used to refine the file parsing. Matplotlib and Numpy are used to graph the vectors and their similarity relative to a specified text.

![alt text](https://raw.githubusercontent.com/ulloaluis/similarity/master/outputs/unk-author.png)

## Other outputs

The following image determines the similarity between each of the federalist author's writing and a [collection of 2000+ tweets written by Trump](https://data.world/briangriffey/trump-tweets/workspace/file?filename=trump_tweets.csv).

![alt text](https://raw.githubusercontent.com/ulloaluis/similarity/master/outputs/trump.png)

...between each of the federalist author's writing and some Lady Gaga lyrics:

![alt text](https://raw.githubusercontent.com/ulloaluis/similarity/master/outputs/lady-gaga.png)

...between each of the federalist author's writing and the full text of Moby Dick:

![alt text](https://raw.githubusercontent.com/ulloaluis/similarity/master/outputs/moby-dick.png)

...between each of the federalist author's writing and the Shakespearean play Romeo and Juliet:

![alt text](https://raw.githubusercontent.com/ulloaluis/similarity/master/outputs/romeo-juliet.png)

## Potential additions:
1) Other natural language processing techniques to refine program functionality
2) Experimenting with angular distance and similarity to see whether it yields better results than cosine similarity
3) Generalizing the file to an executable script that accepts a variable amount of 2+ filenames as arguments, with the first file being the file that the other files are compared to
4) Other cosine similarity applications
