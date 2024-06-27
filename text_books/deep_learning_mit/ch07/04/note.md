* [Back to Deep Learning MIT](../../main.md)

# 7.4 Dataset Augmentation
#### Why Doing This?)
- The best way to make a machine learning model generalize better is to train it on more data.
- In practice, the amount of data we have is **limited**.
- One way to get around this problem is to **create fake data** and add it to the training set.
- For some machine learning tasks, it is reasonably **straightforward** to create new fake data.

#### Warnings)
- When comparing machine learning benchmark results, it is important to take the effect of dataset augmentation into account. 
  - Often, hand-designed dataset augmentation schemes can dramatically reduce the generalization error of a machine learning technique.
  - To compare the performance of one machine learning algorithm to another, it is necessary to perform controlled experiments.
    - e.g.) 
      - When comparing machine learning algorithm A and machine learning algorithm B, it is necessary to make sure that both algorithms were evaluated using the same hand-designed dataset augmentation schemes.
      - Suppose that algorithm A performs poorly with no dataset augmentation and algorithm B performs well when **combined with numerous synthetic transformations** of the input.
      - In such a case it is likely the **synthetic transformations** caused the improved performance, rather than the use of machine learning algorithm B.
  - Sometimes deciding whether an experiment has been properly controlled requires subjective judgment.
    - ML algorithms that inject noise into the input are performing a form of dataset augmentation.
    - Usually, operations that are generally applicable are considered part of the machine learning algorithm.
      - e.g.) Gaussian noise to the input
    - On the other hand, operations that are specific to one application domain are considered to be separate pre-processing steps.
      - e.g.) Randomly cropping an image.


<br>

### E.g.) Dataset Augmentation for Classification Problem
- Desc.)
  - A classifier needs to take a complicated, high dimensional input $`x`$ and summarize it with a single category identity $`y`$.
    - This means that the main task facing a classifier is to be invariant to a wide variety of transformations.
    - Thus, we can generate new $`(x, y)`$ pairs easily just by transforming the $`x`$ inputs in our training set.
- Usages)
  - Particularly effective for the object recognition problem.
    - Why?) 
      - Images are high dimensional and include an enormous variety of factors of variation, many of which can be easily simulated.
      - Operations like translating the training images a few pixels in each direction can often greatly improve generalization, even if the model has already been designed to be partially translation invariant by using the convolution and pooling techniques.
      - Many other operations such as rotating the image or scaling the image have also proven quite effective.
  - Effective for speech recognition tasks as well.
    - How?)
      - Injecting noise in the input to a neural network
        - However, neural networks prove not to be very robust to noise.
        - One way to improve the robustness of neural networks is simply to train them with random noise applied to their inputs.
          - Input noise injection is part of some unsupervised learning algorithms such as the denoising autoencoder.
        - Noise injection also works when the noise is applied to the hidden units, which can be seen as doing dataset augmentation at multiple levels of abstraction.












<br>

* [Back to Deep Learning MIT](../../main.md)