# Concept Similarity (Exercise 1)

## Requirement

1. Loading definition data
2. Preprocessing (cleaning data)
3. Similarity between definitions (count intersection element normalized on the minimum length between them)
4. Aggregation on dimension (concretezza / specificità)

## Loading data & Preprocessing

The first step is to load the *definition.xlsx* file using the panda library.
After that the ```rm_stopwords_punctuation``` function takes care of removing the non-significant words and punctuation, 
the words are also inflected using one of the following alternatives:
- ```stemming```: truncate words and extract the root;
- ```lemming```: extracts the lemma of the given words in a slower but more precise way.
A dictionary holds the result of the processing, which has four elements. Each value is the list of definitions
extracted and processed.

## Similarity & Aggregation

Now the similarity between all the definitions in pairs of two is calculated using the set intersection. 
The mean for each type is then extracted for these values:
- generic_concrete
- generic_abstract
- specific_concrete
- specific_abstract

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

## Results

Recall that the scores are the result of a tiny corpus and therefore the similarity values are not very high.
In the end the result aggregate on two dimensions:

Lemmer alternative:

|  | Concrete | Abstract |
| ---------| -------- | -------- |
| Generic  |   0.26   |   0.13   |
| Specific |   0.19   |   0.12   |

Stemmer alternative:

|  | Concrete | Abstract |
| ---------| -------- | --------|
| Generic  |   0.29   |   0.14  |
| Specific |   0.20   |   0.19  |

The table shows how words concerning concrete concepts have a higher score for the generic than the specific ones. 
Where a high score indicates greater similarity.
For abstract concepts, however, the trend is reversed and specific terms obtain greater similarity.
Summing up concrete words have a more similar definition when we talk about generic, but abstracts are higher when we look at specific words.
