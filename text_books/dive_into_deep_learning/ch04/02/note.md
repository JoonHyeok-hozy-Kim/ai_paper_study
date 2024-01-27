* [Back to Dive into Deep Learning](../../main.md)

# 4.2 The Image Classification Dataset

#### Tech.) MNIST  (LeCun et al., 1998)
- Desc.)
  - A widely used dataset for image classification is the MNIST dataset of handwritten digits.
    - $28 \times 28$
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

Implement the module for the Fashion-MNIST.
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

Instantiate the module, upscaling to $32 \times 32$ pixels.
```python
data = FashionMNIST(resize=(32, 32))
len(data.train), len(data.val)
```









<br>

* [Back to Dive into Deep Learning](../../main.md)