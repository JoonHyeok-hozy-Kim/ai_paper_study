* [Back to Dive into Deep Learning](../../main.md)

# 4.3 The Base Classification Model
A base class for classification models to simplify future code.

#### Import libraries.
```python
import torch
from d2l import torch as d2l
```

## 4.3.1 The Classifier Class
Defining the ```Classifier``` class.
```python
class Classifier(d2l.Module):  #@save
    """The base class of classification models."""
    def validation_step(self, batch):
        Y_hat = self(*batch[:-1])
        self.plot('loss', self.loss(Y_hat, batch[-1]), train=False)
        self.plot('acc', self.accuracy(Y_hat, batch[-1]), train=False)
```
- Desc.)
  - In the ```validation_step``` we report both the loss value and the classification accuracy on a validation batch.

<br>

By default we use a stochastic gradient descent (SGD) optimizer, operating on minibatches, just as we did in the context of linear regression.
```python
@d2l.add_to_class(d2l.Module)  #@save
def configure_optimizers(self):
    return torch.optim.SGD(self.parameters(), lr=self.lr)
```

<br><br>

## 4.3.2 Accuracy
Given the predicted probability distribution y_hat, we typically choose the class with the highest predicted probability whenever we must output a hard prediction.   

When predictions are consistent with the label class y, they are correct.

- Def.) Accuracy
  - The classification accuracy is the fraction of all predictions that are correct.

<br>

### Tech.) How to calculate accuracy
```python
@d2l.add_to_class(Classifier)  #@save
def accuracy(self, Y_hat, Y, averaged=True):
    """Compute the number of correct predictions."""
    Y_hat = Y_hat.reshape((-1, Y_hat.shape[-1]))
    preds = Y_hat.argmax(axis=1).type(Y.dtype)
    compare = (preds == Y.reshape(-1)).type(torch.float32)
    return compare.mean() if averaged else compare
```
- Desc.)
  - If ```y_hat``` is a matrix, we assume that the second dimension stores prediction scores for each class.
  - We use ```argmax``` to obtain the predicted class by the index for the largest entry in each row. 
  - Then we compare the predicted class with the ground truth ```y``` elementwise.
    - cf.) Since the equality operator ```==``` is sensitive to data types, we convert ```y_hat```’s data type to match that of ```y```.
    - The result is a tensor containing entries of 0 (false) and 1 (true). Taking the sum yields the number of correct predictions.



<br>

* [Back to Dive into Deep Learning](../../main.md)