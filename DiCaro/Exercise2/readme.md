# Content to form (Exercise 2)

## Requirement
1. Loading content_to_form file
2. Preprocessing
3. Using WordNet to infer the concept from the descriptions
4. Define an algorithm to scan WordNet synsets using concept similarity

## Intro
The purpose of this exercise is to take different definition of the same concept and extract the more appropriate meaning.
This is achieved by retrieving the definitions, grouped by columns, within the * content_to_form * file,
then look for the WordNet synset closest to the definitions.

## Loading data & Preprocessing
Similar to the first exercise the first phase consist on loading *content_to_form.xlsx* file using panda. 
The second phase consist on preprocessing and is implemented by the function ```cleaning``` :
- removing stopwords and punctuation;
- removing words with low frequency (as we will see later on this function provide different options);
- lemming.
This function applies to the union of definitions relating to a single concept.

## WordNet inference
In the third phase exploit a **genus-differentia** approach.
In every single sentence for every word obtained by preprocessing, the ``wordnet.synsets()`` function extracts the corresponding WN synsets.
Later from each synset are extracted their hypernyms (genus) and from these all their hyponyms.
Then we move on to the *differentia*: look for the differences between the set of hyponyms found.
This is achieved through a *bag of words* approach which assigns a score based on the length of the intersection
between the definitions and the synset context. Context is achieved by cleaning and merging synset definition and examples.

```
def bag_of_words_weighted(synset, term_dictionary: Counter) -> tuple:
    score = 0
    synset_context = set(parser.cleaning(get_context(synset), parser.LEMMER).keys())
    for word in synset_context:
        if term_dictionary[word] >= 0:
            score += term_dictionary[word]
    return synset, score
```

To improve the importance of repeated words in the definitions, was implemented a bag of words variation:
it is not simply based on the intersection length, but the score is weighted by the frequency of the words in the definitions. 
Using this approach repeated words have a greater impact on the synset choice.

## Results
In the final stage it is possible to observe the results obtained through different cleaning methods.
As mentioned before cleaning method provide different options:
- filter based on words occurrence;
- filter based on most common term;
- alternative use of lemming or stemming.


The algorithm was tested with different configurations of minimum frequency and percentages of most repeated words.
Clearly there is no best solution overall, but every different preprocessing may create a better solution for a single concept.
In my opinion the best result was obtained using 40% of the most repeated words:

Concept | Synset found | Definition | Score |
| ---------| -------- | -------- | -------- |
| justice | Synset('non-discrimination.n.01') | fairness in treating people without prejudice  | 4 |
| patience | Synset('accept.v.07') | tolerate or accommodate oneself to | 5 |
| greed | Synset('greed.n.01') | excessive desire to acquire or possess more (especially more material wealth) than one needs or deserves | 7 |
| politics  | Synset('territorial.a.01') | of or relating to a territory | 3 |
| food | Synset('commensal.n.01') | either of two different animal or plant species living in close association but not interdependent | 8 |
| radiator | Synset('hot.a.01') | used of physical heat; having a high or higher than desirable temperature or giving off heat or feeling or causing a sensation of heat or burning | 12 |
| vehicle | Synset('container.n.01') | any object that can be used to hold things (especially a large metal boxlike object of standardized dimensions that can be loaded from one form of transport to another) | 14 |
| screw | Synset('solder.n.01') | an alloy (usually of lead and tin) used when melted to join two metal surfaces | 15 |

The table shows the target meanings of the definitions and what obtained in the best configuration, 
moreover, inside the file *output.txt* there are the results obtained with different configurations.
In addition to the target concept is present the best synset found, and his description with the score retrieved.
From the result we can see how the algorithm take the perfect synset only one time (Synset('greed.n.01')), 
but descriptions show how meaning are close to the original concept.
