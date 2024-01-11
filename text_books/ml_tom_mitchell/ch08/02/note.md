* [Back to Machine Learning Tom Mitchell Main](../../main.md)

<br>

### Concept) Instance-Based Learning Methods Overview
- Structure)
  1. Simply store the presented training data. 
  2. When a new query instance is encountered, a set of similar related instances is retrieved from memory and used to classify the new query instance.
- Prop.)
  - Different from other learning methods on the point that...
    - Other methods can construct a different **approximation to the target function** for each distinct query instance that must be classified.
    - Instance-based methods can also use more complex, symbolic representations for instances.
  - Disadvantages of instance-based approaches 
    1. The cost of classifying new instances can be high.
       - Therefore, techniques for **efficiently indexing training examples** are a significant practical issue.
    2. They typically consider **all attributes** of the instances when attempting to retrieve similar training examples from memory. 
       1. If the target concept depends on only a few of the many available attributes, then the instances that are truly most "similar" may well be a large distance apart.

<br><br>

# 8.2 k-Nearest Neighbor Learning













<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)