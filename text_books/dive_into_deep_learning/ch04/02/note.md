* [Back to Dive into Deep Learning](../../main.md)

# 4.2 The Image Classification Dataset

#### Tech.) MNIST  (LeCun et al., 1998)
- Desc.)
  - A widely used dataset for image classification is the MNIST dataset of handwritten digits.
    - $28 \times 28$ pixel images
  - Today, MNIST serves as more of a sanity check than as a benchmark.
  - This article covers a smaller version of it : Fashion-MNIST dataset.
    - Xiao, H., Rasul, K., & Vollgraf, R. (2017). *Fashion-MNIST: a novel image dataset for benchmarking machine learning algorithms.*

#### Import Libraries
```python
import time
import torch
import torchvision
from torchvision import transforms
from d2l import torch as d2l

d2l.use_svg_display()
```

## 4.2.1 Loading the Dataset
- All major frameworks provide preprocessed versions of Fasion-MNIST.   
  - In PyTorch, ```torchvision.transforms.datasets.FasionMNIST```.
- Fashion-MNIST consists of images from 10 categories, each represented by 6000 images in the **training dataset** and by 1000 in the **test dataset**.

<br>

#### Implement a module for the Fashion-MNIST dataset.
```python
class FashionMNIST(d2l.DataModule):  #@save
    """The Fashion-MNIST dataset."""
    def __init__(self, batch_size=64, resize=(28, 28)):
        super().__init__()
        self.save_hyperparameters()
        trans = transforms.Compose([transforms.Resize(resize),
                                    transforms.ToTensor()])
        self.train = torchvision.datasets.FashionMNIST(
            root=self.root, train=True, transform=trans, download=True)
        self.val = torchvision.datasets.FashionMNIST(
            root=self.root, train=False, transform=trans, download=True)
```

<br>

Instantiate the module, upscaling to $32 \times 32$ pixels, which is similar to $28 \times 28$ of the original MNIST dataset.
```python
data = FashionMNIST(resize=(32, 32))
len(data.train), len(data.val)
```

<br>

#### Dataset description)
- $32 \times 32$ pixels
- Three channels stored in a tensor $`\left[\begin{array}{ccc}c&h&w\end{array}\right]`$  
  - color, height, and width
  - Check it.
    ```python
    data.train[0][0].shape
    ```

<br>

The categories of Fashion-MNIST have human-understandable names. The following convenience method converts between numeric labels and their names.
```python
@d2l.add_to_class(FashionMNIST)  #@save
def text_labels(self, indices):
    """Return text labels."""
    labels = ['t-shirt', 'trouser', 'pullover', 'dress', 'coat',
              'sandal', 'shirt', 'sneaker', 'bag', 'ankle boot']
    return [labels[int(i)] for i in indices]
```

<br><br>

## 4.2.2 Reading a Minibatch
- We use the built-in data iterator for convenience.
  - At each iteration, a data iterator reads a minibatch of data with size ```batch_size```. 
  - Randomly shuffled!
```python
@d2l.add_to_class(FashionMNIST)  #@save
def get_dataloader(self, train):
    data = self.train if train else self.val
    return torch.utils.data.DataLoader(data, self.batch_size, shuffle=train,
                                       num_workers=self.num_workers)
```

Load the data and check the data types.
```python
X, y = next(iter(data.train_dataloader()))
print(X.shape, X.dtype, y.shape, y.dtype)
```
- A minibatch contains 64 images as [we defined](#implement-a-module-for-the-fashion-mnist-dataset).

<br>

Check the time it takes to read all the images. Takes quite a while...
```python
tic = time.time()
for X, y in data.train_dataloader():
    continue
f'{time.time() - tic:.2f} sec'
```

<br><br>

## 4.2.3 Visualization
Declare the ```d2l.show_images``` function in the ```d2l``` module that visualize the images and the associated labels.
```python
def show_images(imgs, num_rows, num_cols, titles=None, scale=1.5):  #@save
    """Plot a list of images."""
    raise NotImplementedError
```

<br>

Use ```d2l.show_images``` to implement a function that visualizes every images.
```python
@d2l.add_to_class(FashionMNIST)  #@save
def visualize(self, batch, nrows=1, ncols=8, labels=[]):
    X, y = batch
    if not labels:
        labels = self.text_labels(y)
    d2l.show_images(X.squeeze(1), nrows, ncols, titles=labels)
batch = next(iter(data.val_dataloader()))
data.visualize(batch)
```



<br>

* [Back to Dive into Deep Learning](../../main.md)