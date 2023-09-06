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
    1. **Statistics**
         * To estimate this latent structure
         * To get rid of the obscuring "noise."
    2. **Singular-value decomposition**
         * Desc.
           * One sort of latent semantic indexing(LSI)
         * How it works?
           * Take a large matrix of term-document association data 
           * Construct a **semantic space**
             * Concept) Semantic Space
               * Terms and documents that are closely associated are **placed** near one another
           * **Position** in the space then serves as the new kind of semantic indexing.
           * Retrieval proceeds by using the terms in a query to identify a point in the space, and documents in its **neighborhood** are returned to the user.
         * Advantage)
           * It can arrange the space to reflect the major **associative patterns** in the data
           * Ignore the smaller, less important influences
         * Effect)
           * Terms that did not actually appear in a document may still end up close to the document, if that is consistent with the major patterns of association in the data


---
## 1. Deficiencies of Current Automatic Indexing and Retrieval Methods

#### Concept) A Problem in current information retrieval methods 
* (words that searchers use often) $\neq$ (words indexed by the information searchers seek)
  * Two Sides in this issue
    1. Synonymy
       * Meaning)
         * There are many ways to refer to the same object.
         * Users in different contexts, or with different needs, knowledge, or linguistic habits will describe the same information using different terms.
       * Result)
         * The prevalence of synonyms tends to **decrease the "recall" performance of retrieval systems**.
    2. Polysemy
       * Meaning)
         * Most words have more than one distinct meaning (homography).
         * In different contexts or when used by different people the same term takes on varying referential significance.
       * Result)
         * The use of a term in a search query does not necessarily mean that a document containing or labeled by the same term is of interest.
         * Polysemy is one factor underlying **poor "precision."**


---
* [Back to Main](../README.md)