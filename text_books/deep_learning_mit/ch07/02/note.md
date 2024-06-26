* [Back to Deep Learning MIT](../../main.md)

# 7.2 Norm Penalties as Constrained Optimization

### Review) Optimization for the Cost Function Subject to Constraints
- Original Problem)
  - The cost function regularized by a [parameter norm penalty](../01/note.md#concept-parameter-norm-penalty).
    - $`\tilde{J}(\theta; X,y) = J(\theta; X,y) + \alpha\Omega(\theta)`$
  - This can be solved using [generalized Lagrangian function](../../ch04/04/note.md#concept-karush-kuhn-tucker-kkt), consisting of the original objective function plus a set of penalties.
- Additional Constraint on the [parameter norm penalty](../01/note.md#concept-parameter-norm-penalty))
  - Make $`\Omega(\theta) \lt k \in\mathbb{R}`$.
    - $`\mathcal{L}(\theta, \alpha; X,y) = J(\theta; X,y) + \alpha(\Omega(\theta)-k)`$
      - where $`\alpha \in\mathbb{R}`$ is the [KKT multiplier](../../ch04/04/note.md#concept-karush-kuhn-tucker-kkt).
  - Then the solution is given by
    - $`\displaystyle\theta^\ast = \arg\min_\theta \max_{\alpha, \alpha\ge0} \mathcal{L}(\theta, \alpha)`$
      - The gradient descent or analytical solutions for where the gradient is zero can be further utilized.
  - Prop.)
    - The [KKT multiplier](../../ch04/04/note.md#concept-karush-kuhn-tucker-kkt) $`\alpha`$
        - $`\alpha`$ must increase if $`\Omega(\theta) \gt k`$.
        - $`\alpha`$ must decrease if $`\Omega(\theta) \lt k`$.
        - The optimal value $`\alpha^\ast`$ will encourage $`\Omega(\theta)`$ to shrink
          - but not so strongly to make $`\Omega(\theta) \lt k`$
        - If we fix $`\alpha = \alpha^\ast`$,
          - the problem goes identical to [the regularized training problem](../01/note.md#concept-parameter-norm-penalty) of minimizing $`\tilde{J}`$.
          - The Constraint Region of Weights)
            - If $`\Omega`$ is the $`L^2`$ norm, then the weights are constrained to lie in an $`L^2`$ ball.
            - If $`\Omega`$ is the $`L^1`$ norm, then the weights are constrained to lie in a region of limited $`L^1`$ norm.
            - Usually we do not know the size of the constraint region that we impose by using weight decay with coefficient $`\alpha^\ast`$.
              - Why?) $`\alpha^\ast`$ does not directly indicate the value of $`k`$.
            - Larger (Smaller) $`\alpha`$ will result in a smaller (larger) constraint region.

<br><br>

### Concept) Explicit Constraints Instead of Penalties
- e.g.)
  - [Modify](../../ch04/04/note.md#concept-constrained-optimization) algorithms like stochastic gradient descent to...
    1. Take a step downhill on $`J(\theta)`$.
    2. Project $`\theta`$ back to the nearest point that satisfies $`\Omega(\theta) \lt k`$
- Advantages)
  1. If we know the appropriate value of $`k`$, we do not have to spend time searching for the value of $`\alpha`$ corresponding to that $`k`$.
  2. **Penalties** can cause non-convex optimization procedures to get stuck in local minima corresponding to small $`\theta`$.
     - When training neural networks, this usually manifests as neural networks that train with several **dead units**.
       - i.e.) The units that do not contribute much to the behavior of the function learned by the network because the **weights** going into or out of them are all **very small**.
     - On the other hand, **explicit constraints** implemented by re-projection can work much better in these cases because they do not encourage the weights to approach the origin.
       - They have effects when the weights become large and attempt to leave the constraint region.
  3. **Explicit Constraints** impose some stability on the optimization procedure.
     - When using high learning rates, it is possible to encounter a positive feedback loop in which large weights induce large gradients which then induce a large update to the weights.
     - If these updates consistently increase the size of the weights, then $`\theta`$ rapidly moves away from the origin until numerical overflow occurs.
     - **Explicit constraints** with reprojection prevent this feedback loop from continuing to increase the magnitude of the weights without bound.
     - e.g.) **Hinton et al. (2012c)** recommend a strategy introduced by **Srebro and Shraibman (2005)**
       - Constraining the norm of each column of the weight matrix of a neural net layer, rather than constraining the [Frobenius norm](../../ch02/05/note.md#concept-frobenius-norm) of the entire weight matrix.
       - Why doing this?)
         - Constraining the norm of **each column separately** prevents any one hidden unit from having very large weights.



<br>

* [Back to Deep Learning MIT](../../main.md)