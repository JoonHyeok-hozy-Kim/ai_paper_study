* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 4.6 Remarks on the Backpropagation Algorithm

## 4.6.1 Convergence and Local Minima
- Recall that the Backpropagation over multilayer networks guarantees only to converge toward some local minimum in $E$
  - Not necessarily to the global minimum error.
- Still, the problem of local minima has not been found to be as severe in practice.
  - Why?)
    1. Multiple weights
       - Consider that we defined multiple weights correspond to error surfaces in very  high dimensional spaces (one dimension per weight).
       - When gradient descent falls into a local minimum with respect to one of these  weights, it will not necessarily be in a local minimum with respect to the other  weights. 
       - In fact, the more weights in the network, the more dimensions that might provide  "escape routes" for gradient descent to fall away from the local minimum with  respect to this single weight.














<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)