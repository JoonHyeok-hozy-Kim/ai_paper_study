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

<center>
<img src="~@source/../../images/zero-shot_learning/01_01.png" width="400rm" />
</center>

2. The model incorporates **novelty detection** which determines whether a new image is on the manifold of known categories
   * Why?) classifiers prefer to assign test images into classes for which they have seen training examples
   * How?)
     * Rule
       * If the image is of a known category, a standard classifier can be used.
       * Otherwise, images are assigned to a class based on the likelihood of being an unseen category.
     * Methodology
       1. Prefers high accuracy for unseen classes
       2. Prefers high accuracy for for seen classes