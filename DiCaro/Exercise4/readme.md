# Text Tiling (Exercise 4)

## Requirement
Inspired by Text Tiling, implement an algorithm of text segmentation.
It is possibile to use any information preferred like frequency, lexical resources etc.
Which texts is your choice.
    
## Intro
Text tiling algorithms try to group sentences about the same topic. 
The general idea is to find through different characteristics (e.g. frequency or lexical resources) 
points where to divide the sentences.
The text used was taken from Wikipedia (at the following link [GAN]) and saved in the *input.txt* file. 
After having preprocessed it, an attempt is made to identify the cut-off frequencies using the frequencies, 
later, thanks to `genus_differentia` function of second exercise, 
it was possible to search for the most similar synsets to the phrases examined.
Let's see in more detail.

## Preprocessing & pretty table
As usual, the first step consists in cleaning the sentences read from the file. 
Also in this case it is possible to use different cleaning parameters, 
but since the words were not very frequent, first phase doesn't filter them by frequency.
At this point sentences have been merged depending on *step* parameter:

`
sentences = process_file(INPUT_PATH)
clustered_sentences = cluster_sentences(sentences, break_points=[*range(step, len(sentences), step)])
`

Then fifteen most common words have been printed across the pretty table.

CLUSTERING WITH STEP: 4
+--------------------------------------------------------------------------------------------------------------+
|     Words       0   1   2   3   4   5   6   7   8   9   10   11   12   13   14   15   16   17   18   19   20 |
+--------------------------------------------------------------------------------------------------------------+
|      GANs       1   1   0   0   0   0   4   2   2   1   1    2    4    1    3    1    0    0    0    1    0  |
|    network      2   2   5   0   3   1   0   0   0   0   0    1    1    4    0    1    2    1    0    0    0  |
|     image       0   1   0   0   2   0   2   0   3   2   1    3    2    1    0    0    2    0    0    0    0  |
|     model       1   1   0   0   0   0   2   1   0   0   0    2    0    1    0    2    1    0    0    7    0  |
|      used       0   0   0   0   0   0   2   1   0   1   0    3    4    1    1    1    2    1    0    0    0  |
| discriminator   0   2   2   2   3   0   0   0   0   0   0    0    0    0    0    0    0    0    0    6    0  |
|      GAN        2   0   0   0   0   1   1   0   1   0   0    1    0    1    0    1    1    2    0    2    0  |
|   generator     0   1   1   2   3   0   0   0   0   0   0    0    0    0    0    1    0    0    0    5    0  |
|    training     2   1   1   3   0   0   0   0   2   0   0    0    1    0    0    0    0    0    0    1    0  |
|      game       2   0   0   0   0   0   0   0   4   0   0    1    0    0    0    0    1    0    1    0    0  |
|      2019       0   0   0   0   0   0   1   1   0   0   2    0    0    0    1    0    0    1    3    0    0  |
|   generative    2   1   2   0   0   0   0   0   0   0   0    0    0    1    0    1    1    0    0    0    0  |
|    learning     5   0   0   0   0   0   0   0   0   0   0    0    0    0    0    0    2    0    0    0    1  |
|    generate     2   0   0   0   0   0   1   0   0   1   0    0    2    0    1    0    0    1    0    0    0  |
|      data       1   0   4   1   0   1   0   0   0   0   0    0    0    0    0    0    0    0    0    0    0  |
+--------------------------------------------------------------------------------------------------------------+

## Text tiling algorithm
In this phase for each group it was calculated the cohesion between next and previous group, then the average between this two choesions. 
The similarity between two groups is calculated as the weighted intersection of the words between the two groups examined.
Thanks to these data it was possible to identify the *local minima*:
points that are below global average and whose similarity is less than the previous and next group.
Local minima are important because they allow us to define the cut points, that is, 
those that divide the sentence into groups sharing the same topic.

## Result




[GAN]: <https://en.wikipedia.org/wiki/Generative_adversarial_network>