* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 4.6 Remarks on the Backpropagation Algorithm

## 4.6.1 Convergence and Local Minima
- Recall that the Backpropagation over multilayer networks guarantees only to converge toward some local minimum in $E$
  - Not necessarily to the global minimum error.
- Still, the problem of local minima has not been found to be as severe in practice.
  - Possible Explanations)
    1. Multiple Weights
       - Consider that we defined multiple weights correspond to error surfaces in very  high dimensional spaces (one dimension per weight).
       - When gradient descent falls into a local minimum with respect to one of these  weights, it will not necessarily be in a local minimum with respect to the other  weights. 
       - In fact, the more weights in the network, the more dimensions that might provide  "escape routes" for gradient descent to fall away from the local minimum with  respect to this single weight.
    2. Gradual Increase in Weights
       - Consider that we initialized the weights to values near zero.
       - Then, the early gradient descent steps will represent very smooth function.
         - This means that the function output will be linear to the input.
         - why?)
           - The sigmoid function threshold is approximately linear around zero.
       - After sufficient steps pass, the weights will grow to represent highly nonlinear network functions.
       - Then, we might assume that our algorithm reached a point close enough to the global minimum that even local minima in this region are acceptable.
  - Nevertheless, no methods are known to predict with certainty when local minima will cause difficulties.

<br>

#### Concept) Common heuristics to alleviate the problem of local minima
  1. [Add a momentum term](../05/note.md#4521-adding-momentum) to the weight-update rule
  2. Use [stochastic gradient descent](../04/note.md#tech-stochastic-gradient-descent-incremental-gradient-descent) rather than true gradient descent
  3. Train multiple networks using the same data, but initializing each network with different random weights.


<br>

## 4.6.2 Representational Power of Feedforward Networks
- Various functions can be represented by feedforward networks depending on the width and the depth of the networks.
- Still, much is unknown about which function classes can be described by which types of networks.
- Known Three Results)
  1. Boolean Functions
     - Every boolean function can be represented exactly by some network with two layers of units
       - the number of hidden units required grows exponentially in the worst case with the number of network inputs. 
     - How?)
       - Consider the following general scheme for representing an arbitrary boolean function
         1. For each possible input vector, create a distinct hidden unit 
         2. Set its weights so that it activates if and only if this specific vector is input to the network. 
         3. This produces a hidden layer that will always have exactly one unit active. 
         4. Now implement the output unit as an OR gate that activates just for the desired input patterns.
  2. Continuous Functions
     - Every bounded continuous function can be approximated with arbitrarily small error (under a finite norm) by a network with two layers of units (Cybenko 1989; Hornik et al. 1989). 
     - The theorem in this case applies to networks that use sigmoid units at the hidden layer and (unthresholded) linear units at the output layer. 
     - The number of hidden units required depends on the function to be approximated.
  3. Arbitrary Functions
     - Any function can be approximated to arbitrary accuracy by a network with three layers of units (Cybenko 1988). 
     - Again, the output layer uses linear units, the two hidden layers use sigmoid units, and the number of units required at each layer is not known in general. 
     - The proof of this involves showing that any function can be approximated by a linear combination of many localized functions that have value 0 everywhere except for some small region, and then showing that two layers of sigmoid units are sufficient to produce good local approximations.


<br><br>

## 4.6.3 Hypothesis Space Search and Inductive Bias
#### Concept) Hypothesis Space Search of Backpropagation
- The hypothesis space is the $n$-dimensional Euclidean space of the $n$ network weights.
- This hypothesis space is continuous.
  - cf.) Recall that the hypothesis spaces of decision tree learning and other methods based on discrete representations.
  - Also, the error $E$ is differentiable with respect to the continuous parameters of the hypothesis.
    - As a result, a well-defined error gradient provides a very useful structure for organizing the search for the best hypothesis. 

<br>

#### Concept) Inductive Bias of the Backpropagation Algorithm
- It is difficult to characterize precisely the inductive bias of BACKPROPAGATION learning.
  - why?)
    - It depends on the interplay between the gradient descent search and the way in which the weight space spans the space of representable functions.
- Still, one can roughly characterize it as smooth interpolation between data points.
  - Given two positive training examples with no negative examples between them, Backpropagation will tend to label points in between as positive examples as well. 
  - This can be seen, for example, in the decision surface illustrated in the figure below, in which the specific sample of training examples gives rise to smoothly varying decision regions.   
    ![](images/001.png)


<br><br>

## 4.6.4 Hidden Layer Representation
- Prop.)
  - Backpropagation can discover useful intermediate representations at the hidden unit layers inside the network.
    - why?)
      - Training examples constrain only the network **inputs** and **outputs**.
      - The weight-tuning procedure is free to set weights that define whatever hidden unit representation is most effective at minimizing the squared error $E$.

#### Example)
![](images/002.png)
- Settings)
  - The eight network inputs are connected to three hidden units, which are in turn connected to the eight output units.
  - Assume that the network is to learn a simple target function $f$ such that...
    - $f(\overrightarrow{x}) = \overrightarrow{x}$
      - where $\overrightarrow{x}$ is a vector containing sever 0s and a single 1.$
        - e.g.) $0000001, 0000010, \cdots, 1000000$
  - Then, the essential information from all eight input units must be captured by the three learned hidden units.
- Result)
  - The learned encoding is similar to the familiar standard binary encoding of eight values using three bits.
    - e.g.) $000,001,010, \cdots , 111$
      - How?)   
        |Input|Hidden Values|Rounded Hidden Values|Output|
        |:---:|:-----------:|:-----:|:----:|
        |1000000|.89 .04 .08|1 0 0|1000000|
        |0100000|.15 .99 .99|0 1 1|0100000|
        |0010000|.01 .97 .27|0 1 0|0010000|
        |$\vdots$|$\vdots$|$\vdots$|$\vdots$|
        |0000001|.60 .94 .91|1 1 1|0000001|



<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)