* [Back to Main](../README.md)
---

# Indexing by Latent Semantic Analysis
#### Scott Deerwester, Susan T. Dumais, George W. Furnas, and Thomas K. Landauer, Richard Harshman

* [Read Paper](../papers/230906%20lsa.pdf)

---
## 0. Introduction
#### Goal) Describing a new approach to automatic indexing and retrieval
* Why doing this?
  * A fundamental problem in matching **words of queries** with **words of documents**
  * Users want to retrieve on the basis of **conceptual content**
  * **Individual words** provide unreliable evidence about the conceptual topic or meaning of a document. 
  * So the **literal terms** in a user's query may not match those of a relevant document.
  * Most words have **multiple meanings**, so terms in a user's query will literally match terms in documents that are not of interest to the user.
  
#### Sol.) Treating the **unreliability** of observed term-document association data as a **statistical problem**
  * Assumption) 
    * There is some underlying **latent semantic structure** in the data that is partially obscured by the **randomness of word choice** with respect to retrieval.
  * Tool) 
    1. Statistics
         * To estimate this latent structure
         * To get rid of the obscuring "noise."
    2. Singular-value decomposition
         * One sort of latent semantic indexing(LSI)
         * How?
           * Take a large matrix of term-document association data 
           * Construct a **semantic space**
             * Concept) Semantic Space
               * Terms and documents that are closely associated are placed near one another
         * Advantage
           * Arranging the space to reflect the major **associative patterns** in the data

---
* [Back to Main](../README.md)