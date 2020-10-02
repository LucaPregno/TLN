# Content to form (Exercise 2)

## Requirement
1. Loading content_to_form file
2. Preprocessing
3. Using WordNet to infer the concept from the descriptions
4. Define an algorithm to scan WordNet synsets using concept similarity

## Intro
The purpose of this exercise is to take different definition of the same concept and extract the meaning more appropriate.
This should be achieved retrieving the definitions inside the file *content_to_form* that are grouped by column and then
searching the WordNet synset which is more similar to the definitions.

## Loading data & Preprocessing
Similar to the first exercise the first phase consist on loading the file content_to_form.xlsx using panda. 
The second phase consist on preprocessing and is implemented by the function ```cleaning``` :
- removing stopwords and punctuation;
- removing words with low frequency (as we will see later on this function provide different options);
- lemming.
This function is applied on the union of the definitions related to a single concept.

## Inference by WordNet
In the third phase I followed the advice to implement a kind of *genus-differentia* approach.
For each definition I create a set.
For every word obtained from preprocessing I took the WN synsets and add them to the set with their:
- hypernyms
- hyponyms of the hypernyms.
Then, since there is a close relation to hyponyms of the synset, I added them to the set too.
Finally the fourth phase:
for each synset in the related set (hypernyms, hyponyms and siblings(hyponyms of hypernyms)) I extracted the context.
The context is obtained merging and then cleaning definition and examples of the synset.
Then the best synset is calculated using the bag of words approach:
finding the maximum intersection length between definition words and synset context.

```
def bag_of_words_weighted(synset, term_dictionary: Counter) -> tuple:
    score = 0
    synset_context = set(parser.cleaning(get_context(synset), parser.LEMMER).keys())
    for word in synset_context:
        if term_dictionary[word] >= 0:
            score += term_dictionary[word]
    return synset, score
```

In order to improve the importance of the repeated words in definitions I decided to implement a little variation of the bag of words:
the score is not simply based on the length of the intersection, but each time a word is present in the synset context 
the score is incremented by the word frequency. In this way words that have a lot of repetitions have more impact in the
choice of the synset.

## Results
As mentioned before cleaning method provide different options:
- filter based on words occurrence;
- filter based on most common term;
- alternative use of lemming or stemming.

The best result was obtained with the first 40% of the most frequent words:

Concept | Synset found | Definition | Score |
| ---------| -------- | -------- | -------- |
| justice | Synset('non-discrimination.n.01') | fairness in treating people without prejudice  | 4 |
| patience | Synset('digest.v.03') | put up with something or somebody unpleasant | 5 |
| greed | Synset('greed.n.01') | excessive desire to acquire or possess more (especially more material wealth) than one needs or deserves | 7 |
| politics  | Synset('territorial.a.01') | of or relating to a territory | 3 |
| food | Synset('commensal.n.01') | either of two different animal or plant species living in close association but not interdependent | 8 |
| radiator | Synset('hot.a.01') | used of physical heat; having a high or higher than desirable temperature or giving off heat or feeling or causing a sensation of heat or burning | 12 |
| vehicle | Synset('wheeled_vehicle.n.01') | a vehicle that moves on wheels and usually has a container for transporting things or people | 12 |
| screw | Synset('solder.n.01') | an alloy (usually of lead and tin) used when melted to join two metal surfaces | 15 |

The table shows the target meanings of the definitions and what obtained in the best configuration, 
moreover, inside the *output.txt* file there are results obtained with different configurations.
In addition to the target concept is present the best synset found, and his description with the score retrieved.
From the result we can see how the algorithm take the perfect synset only one time (Synset('greed.n.01')), 
but descriptions show how meaning are close to the original concept.
