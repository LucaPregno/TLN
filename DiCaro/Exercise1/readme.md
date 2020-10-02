# Concept Similarity (Exercise 1)

## Requirement
1. Loading definition data
2. Preprocessing (cleaning data)
3. Similarity between definitions (count intersection element normalized on the minimum length between them)
4. Aggregation on dimension (concretezza / specificità)

## Loading data & Preprocessing
In the first step I just loaded definizioni.xlsx file using panda.
After that I just cleaned the definition retrieved using the methods ```rm_stopwords_punctuation``` 
(in order to remove stopwords and punctuation ) and then used two alternatives: 
- ```stemmer```: process in order to crop words and extract their root;
- ```lemmer```: which extract the lemma of the given words using a slower but more precise way.
The processing result are saved into a dictionary, which have four elements. Each element is the list of the definitions
extracted and processed.

## Similarity & Aggregation
In order to compute the similarity between each set of every processed definitions I simply used the 
intersection normalized between minimum of the set cardinality.
```
for i, definition1 in enumerate(value_table[elem]):
    for j, definition2 in enumerate(value_table[elem], start=i+1):
        min_len = min(len(definition1), len(definition2))
        intersection_len = len(definition1.intersection(definition2))
        similarity = intersection_len/min_len
        n_elem += 1
        average += similarity
    average /= n_elem
```
After that compute the average of every column definition.

## Results
Now we can see the result aggregate on two dimensions (generic/specific).

For the Lemmer alternative:

|  | Concrete | Abstract |
| ---------| -------- | -------- |
| Generic  |   0.26   |   0.13   |
| Specific |   0.19   |   0.12   |

For the Stemmer alternative:

|  | Concrete | Abstract |
| ---------| -------- | -------- |
| Generic  |   0.29   |   0.14   |
| Specific |   0.20   |   0.19   |

We can notice how concrete words have higher score then abstract, this means that concrete words definitions are more similar.
About concrete dimension we can notice generic words are more similar each other than specific ones, but this trend seems
to invert when we look to abstract words.
Summing up concrete words have more similar definition when we talk about generic, but abstract have higher similar score
when we look on specific words.
