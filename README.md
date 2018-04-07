# TwitterGenderPredictor

__JT Wolohan__

_jwolohan@indiana.edu_

#### Description
This is a Python implementation of Sap et al.'s gender prediction algorithm for Twitter.

    Sap, M., Park, G., Eichstaedt, J., Kern, M., Stillwell, D., Kosinski, M., ... & Schwartz, H. A. (2014). Developing age and gender predictive lexica over social media. In Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP) (pp. 1146-1151).

## Use 

1. Clone the repository.
2. Import SapGenderPrediction.
3. Initiate a `GndrPrdct` class object.
4. Call the `predict_gender` method on a string collection of tweets.

#### Example

```python
from SapGEnderPrediction import GndrPrdct

Classifier  = GndrPrdct()
tweets = ["This is a tweet.", "I'm another tweet!", "Hey, @realDonaldTrump, I'm yet another tweet!"]

Classifier.predict_gender(" ".join(tweets))
```



