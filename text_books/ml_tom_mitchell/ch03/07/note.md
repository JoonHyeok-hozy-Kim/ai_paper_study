* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 3.7 Issue in Decision Tree Learning
- Issues
  - Determining how deeply to grow the decision tree
  - Handling continuous attributes
  - Choosing an appropriate attribute selection measure
  - Handling training data with missing attribute values
  - Handling attributes with differing costs
  - Improving computational efficiency 

<br>

## 3.7.1 Avoiding Overfitting the Data
#### Def.) Overfit
Given a hypothesis space $H$, a hypothesis $h \in H$ is said to **overfit** the training data if there exists some alternative hypothesis $h' \in H$, such that $h$ has smaller error than $h'$ over the **training examples**, but $h'$ has a smaller error than $h$ over the **entire distribution** of instances.
- e.g.)   
  ![](images/001.png)
  - As the size of the tree increase, the model becomes more complex.
  - And its accuracy over the training data increases.
  - But the accuracy over the test data decreases.
    - It implies that the model's accuracy over the entire population decreases.
    
- Why this happens?)
  - One reason is the possible random errors and noise in the training example.




<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)