# TwitterGenderPredictor

__JT Wolohan__

_jwolohan@indiana.edu_

#### Description
This is a Python implementation of Sap et al.'s gender prediction algorithm for Twitter.

_Sap, M., Park, G., Eichstaedt, J., Kern, M., Stillwell, D., Kosinski, M., ... & Schwartz, H. A. (2014). Developing age and gender predictive lexica over social media. In Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP) (pp. 1146-1151)._

## Use 

1. Clone the repository.
2. Import SapGenderPrediction.
3. Initiate a `GndrPrdct` class object.
4. Call the `predict_gender` method on a string collection of tweets.

#### Example

```python
# Step 2
from SapGenderPrediction import GndrPrdct

# Step 3
Classifier  = GndrPrdct()
tweets = ["This is a tweet.", "I'm another tweet!", "Hey, @realDonaldTrump, I'm yet another tweet!"]

# Step 4
Classifier.predict_gender(" ".join(tweets))
```



