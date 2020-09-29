#Concept Similarity (Exercise 1)

## Requirement
1. Loading definition data
2. Preprocessing (cleaning data)
3. Similarity between definitions (count intersection element normalized on the minimum length between them)
4. Aggregation on dimension (concretezza / specificità)

## Loading data & Preprocessing
In the first step I just loaded definizioni.xlsx file using panda.
After that I just cleaned the definition retrieved using the methods ```rm_stopwords_punctuation``` 
(in order to remove stopwords and punctuation ) and ```lemmer```  (which extract the lemma of the given words).
The processing result are saved into a dictionary, which have four elements. Each element is the list of the definitions
extracted and processed.

##Similarity & Aggregation
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

##Results
Now we can see the result aggregate on two dimensions (generic/specific).

| -------- | Concrete | Abstract |
| ---------| -------- | -------- |
| Generic  |   0.23   |   0.13   |
| Specific |   0.18   |   0.13   |

We can notice how concrete words have higher score then abstract, this means that concrete words definitions are more similar.
Looking on other dimension generic seems to win, but there is a shorter gap (we can apply the same reasoning and
deduce generic words are more similar each other than specific ones).
