* [Back to Dive into Deep Learning](../../main.md)

# 5.7 Project: Predicting House Prices on Kaggle

#### Import Packages
```python
import pandas as pd
import torch
from torch import nn
from d2l import torch as d2l
```

## 5.7.1 Downloading Data
- The ```download()``` and ```extract()``` function implemented below will be used in the rest of the session.
```python
def download(url, folder, sha1_hash=None):
    """Download a file to folder and return the local filepath."""

def extract(filename, folder):
    """Extract a zip/tar file into folder."""
```

<br>

## 5.7.2 Kaggle
- [URL](https://www.kaggle.com/)
- [House Price Data](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)

<br>

## 5.7.3 Accessing and Reading the Dataset
- Create an object that downloads and save the dataset using pandas.
    ```python
    class KaggleHouse(d2l.DataModule):
        def __init__(self, batch_size, train=None, val=None):
            super().__init__()
            self.save_hyperparameters()
            if self.train is None:
                self.raw_train = pd.read_csv(d2l.download(
                    d2l.DATA_URL + 'kaggle_house_pred_train.csv', 
                    self.root,
                    sha1_hash='585e9cc93e70b39160e7921475f9bcd7d31219ce'
                ))

                self.raw_val = pd.read_csv(d2l.download(
                    d2l.DATA_URL + 'kaggle_house_pred_test.csv', 
                    self.root,
                    sha1_hash='fa19780a7b011d9b009e8bff8e99922a8ee2eb90'
                ))
    ```
  - Desc.)
    - If a file corresponding to this dataset already exists in the cache directory and its SHA-1 matches ```sha1_hash```, our code will use the cached file to avoid clogging up your Internet with redundant downloads.

- Instantiate the ```KaggleHouse``` object and check the data format.
  ```python
  data = KaggleHouse(batch_size=64)
  print(data.raw_train.shape)
  print(data.raw_val.shape)
  ```
    ![](images/001.png)

<br>

## 5.7.4 Data Processing
- Let's check **ten rows** of data for **the starting four and the last three columns**.
    ```python
    print(data.raw_train.iloc[:10, [0, 1, 2, 3, -3, -2, -1]])    # 0~3 Rows / 0~3, -3~-1 Columns
    ```
    ![](images/002.png)

- Data Processing
  - Drop columns that are not needed.
    - The first feature ```Id``` is the identifier which is not needed for the learning.
    - The ```SalePrice``` feature, which is the label in this dataset, should be dropped from the training set for the training.
      - This column will not be provided in the test set.
  - Fill in the feature's mean for the missing values.
  - Standardize every features on common scale with $\displaystyle x\leftarrow \frac{x-\mu}{\sigma}$.
  - Use One-hot encoding for the discrete values.
    - e.g.) ```MSZoning``` feature.
      - ```pandas.get_dummies()``` will automatically do this for us.

- Add the ```preprocess()``` method to the ```KaggleHouse``` class and implement all the processing algorithms as follows.
    ```python
    @d2l.add_to_class(KaggleHouse)
    def preprocess(self):
        # Remove the ID and label columns
        label = 'SalePrice'
        features = pd.concat(
            (self.raw_train.drop(columns=['Id', label]),        # Drop Id and label column from the training data.
            self.raw_val.drop(columns=['Id'])))
        # Standardize numerical columns
        numeric_features = features.dtypes[features.dtypes!='object'].index
        features[numeric_features] = features[numeric_features].apply(
            lambda x: (x - x.mean()) / (x.std()))
        # Replace NAN numerical features by 0
        features[numeric_features] = features[numeric_features].fillna(0)
        # Replace discrete features by one-hot encoding
        features = pd.get_dummies(features, dummy_na=True)
        # Save preprocessed features
        self.train = features[:self.raw_train.shape[0]].copy()
        self.train[label] = self.raw_train[label]
        self.val = features[self.raw_train.shape[0]:].copy()
    ```
- Call the ```preprocess()``` method and check the data shape.
    ```python
    data.preprocess()
    data.train.shape
    data.val.shape
    ```
    ![](images/003.png)


<br>

* [Back to Dive into Deep Learning](../../main.md)