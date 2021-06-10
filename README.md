## Idea to create the Job skills extraction coding part:
(This is basically a copied answer from stackexchange, here you can see the original answer: [StackExchange - answer](https://datascience.stackexchange.com/a/30066/119113))
___
Assuming you already have the raw text, you can do the followings.

Create train data:

You need to create set words and bigrams labeled as skills. There might be some available lists to help you out. Otherwise, generate your list using resources such as wordnet and thesaurus. You can also start with a short list based on the data you have and then expand it using word2vec or similar word embedding techniques. For example, we start with a list that contains coding as one of the skills. Then, we query the word2vec pretrained model for closest words/bigrams. There is a fair chance you will end up with programming, software coding, and computer programming.

Another approach would be to cluster the words and bigrams in your dataset using word embedding techniques. Then, look into your clusters to see which ones contain the skill set.

Note that any word/expression not on your list will not be considered as required skills. Therefore, you may need to expand your list after a few trials.


**Detecting the Skills:**

- Tokenize your raw text into words and expressions
- Remove stop words
- Encode your tokens using an embedding (Word2Vec, FastText, etc)
- Use the list from the previous step to add labels to your data (anything on the list is True, other as False)
- Train a binary classifier (Naive Bayes classifier should be good enough)
- Evaluate your model, feature set, and labels. If needed, refine and repeat.

---
**Q. What's done so far?**

**Ans:**

- The Basic drag and drop GUI - where you can select some text from the web and drop to the GUI interface.
- The tokenization part is in progress. 
