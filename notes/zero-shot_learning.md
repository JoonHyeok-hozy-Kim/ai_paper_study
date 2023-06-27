# Zero-shot learning through cross-modal transfer
### Richard Socher, Milind Ganjoo, Christopher D. Manning, Andrew Y. Ng
* [Read Paper](https://file.notion.so/f/s/979ead36-2810-4500-93c7-9672bc249f12/5027-zero-shot-learning-through-cross-modal-transfer.pdf?id=248a03b3-531c-4cb5-96cd-1e0a88d08c19&table=block&spaceId=f4f04cc2-d7ba-4dd0-bec8-86c2393d0c27&expirationTimestamp=1687543511698&signature=E99oUS3_SO12-AgM4YdLDbNJQ9Xq8P40yiGThu11aNQ&downloadName=5027-zero-shot-learning-through-cross-modal-transfer.pdf)

---
## 0. Abstract
* Target : Introduce a model that can recognize objects in images even if no training data is available for the object class.
* The model can operate on a mixture of seen and unseen classes.
* Achieved by seeing the distributions of words in texts as a semantic space for understanding what objects look like.
  * Images are mapped to be close to semantic word vectors corresponding to their classes
  * Resulting image embeddings can be used to distinguish whether an image is of a seen or unseen class.
* 2 novelty detection strategies; 
  1. Gives high accuracy on unseen classes
  2. Conservative in its prediction of novelty and keeps the seen classes’ accuracy high.

---

## 1. Introduction
### Concept) Zero-shot Learning
  * Meaning : The ability to classify instances of an unseen visual class,


### Main Goal
* Model people’s ability to identify unseen objects even if the only knowledge about that object came from **reading** about it.
  * ex) **READING** the description of a two-wheeled self-balancing electric vehicle, controlled by a stick, with which you can move around while standing on top of it, many would be able to **IDENTIFY** a Segway


### Main Ideas
1. Images are mapped into a semantic space of words that is learned by a neural network model
   * Word vectors capture distributional similarities from a large, unsupervised text corpus.
     1. Learning an image mapping into this space 
     2. The word vectors get implicitly grounded by the visual modality 
     3. They allows us to give prototypical instances for various words   
     ![](~@source/../../images/zero-shot_learning/01_01.png)
2. The model incorporates **novelty detection** which determines whether a new image is on the manifold of known categories
   * Why?) classifiers prefer to assign test images into classes for which they have seen training examples
   * How?)
     * Rule
       * If the image is of a known category, a standard classifier can be used.
       * Otherwise, images are assigned to a class based on the likelihood of being an unseen category.
     * Methodology
       1. Prefers high accuracy for unseen classes
       2. Prefers high accuracy for for seen classes
  

---

## 2. Related Work

### Concept) One-Shot Learning
* Meaning) Seeks to learn a visual object class by using very few training examples
* Description)
  * This paper's model is based on using **deep learning** techniques to learn low-level image features followed by a **probabilistic model** to **transfer knowledge** with the added advantage of needing **no training data** due to the cross-modal knowledge transfer from natural language.

### Concept) Knowledge and Visual Attribute Transfer
* This model has distributional features of words learned from unsupervised, nonparallel corpora and can classify between categories that have thousands or zero training images.

### Concept) Domain Adaptation
* Useful in situations in which there is a lot of training data in one domain but little to none in another.
* ex) In sentiment analysis one could train a classifier for movie reviews and then adapt from that domain to book reviews

### Concept) Multimodal Embeddings
* Meaning) A technique that relates information from multiple sources such
as sound and video or images and text

---

## 3. Word and Image Representations
### Concept) Distributional Approach
* Used for capturing semantic similarity between words. 
* Words are represented as vectors of distributional characteristics
  * Most often their co-occurrences with words in context
  * This representation is effective in NLP tasks such as...
    * sense disambiguation
    * thesaurus extraction
    * cognitive modeling
  * Use the model of Huang et al
    * Unless otherwise mentioned, all word vectors are initialized with pre-trained d = 50-dimensional word vectors from the unsupervised model

---

## 4. Projecting Images into Semantic Word Spaces
### Goal) Learn semantic relationships and class membership of images
* How?) 
  * Project the image feature vectors into the d-dimensional, semantic word space $F$
  * $Y$ : A set of classes $y$
    * $Y_s$ : Seen classes, i.e., classes that have training data
    * $Y_u$ : Unseen classes, i.e., zero-shot classes without any training data
  * $W$ : The set of word vectors in $R^d$
    * where $W = W_s \cup W_u$
  * All training images $x^{(i)} \in X_y$ of a seen class $y \in Y_s$ are mapped to the word vector $w_y$ corresponding to the class name.
* **Training**
  * Objective Function : $J(\Theta) = \sum_{y \in Y_s} \sum_{x^{(i)} \in X_y} {\Vert w_y - \theta^{(2)} f( \theta^{(1)} x^{(i)}) \Vert}^2$
    * $\theta^{(1)} \in R^{h \times I}$
    * $\theta^{(2)} \in R^{d \times h}$
    * $f = tanh$
    * $\Theta = (\theta^{(1)}, \theta^{(2)})$
  * The cost function is trained with standard backpropagation and L-BFGS.
* **Advantage** of projecting images into the word vector space
  * Implicitly extend the semantics with a visual grounding
  * It allows us to query the space
    * ex) for prototypical visual instances of a word.
* **Experiment**
  * Settings
    * The 50-dimensional semantic space with word vectors and images of both seen and unseen classes
    * The unseen classes are **cat** and **truck**.
    * The mapping from 50 to 2 dimensions was done with t-SNE.
  * Result
    ![image](~@source/../../images/zero-shot_learning/04_01.png)
  * Analysis
    * Most classes are tightly clustered around their corresponding word vector.
    * The **zero-shot classes** (cat and truck for this mapping) do not have close-by vectors.
    * The images of the two zero-shot classes are close to semantically similar classes.
  * Motivation
    1. Detect images of unseen classes.
    2. Classify them to the zero-shot word vectors.

---

## 5. Zero-Shot Learning Model
### Goal) Predict $p(y|x)$
* $p(y|x)$ : the conditional probability for both seen and unseen classes $y \in Y_s \cup Y_u$ given an image from the test set $x \in X_t$

### How?)
* $f \in F_t$ : the semantic vectors to which these images have been mapped to
* $V \in \{s, u\}$ : a binary novelty random variable which indicate whether an image is in a seen or unseen class
* $X_s$ : the set of all feature vectors for training images of seen classes
* $F_s$ : the corresponding semantic vectors of $X_s$
* $F_y$ : the semantic vectors of class $y$

### The Model : $p(y|x, X_s, F_s, W, \theta) = \sum_{V \in \{s, u\}}^{ } P(y|V, x, X_s, F_s, W, \theta) P(V|x, X_s, F_s, W, \theta)$