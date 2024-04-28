* [Back to Main](../../README.md)
---

# Long Short-term Memory
### Sepp Hochreiter, Jurgen Schmidhuber
* [Read Paper](../paper_pdfs/231109%20lstm.pdf)

---
## 1. Introduction
#### The Problem)
- With conventional **Back-Propagation Through Time (BRTT)** or **Real-Time Recurrent Learning (RTRL)**, error signals flowing backwards in time tend to either (1) blow up or (2) vanish.
  - It depends on the size of the weights.
  - Results)
    - (1) : May lead to oscillating weights
    - (2) : learning to bridge long time lags takes a prohibitive amount of time or does not work at all

<br>

#### The Remedy)
- This paper presents **Long Short-term Memory (LTSM)**
  - It can learn to bridge time intervals in excess of 1000 steps even in case of noisy, incompressible input sequences, without loss of short time lag capabilities.
  - How?)
    - Its gradient-based algorithm enforces constant error flow through internal state of special units.

<br><br>

## 2. Previous Work
#### 2.1 Gradient-Descent Variants
- Most Gradient-descent variants suffer from [the same problems as BPTT and RTRL](#the-problem).
  - e.g.)
    - Elman (1988), Fahlman (1991), Williams (1989), Schmidhuber (1992a), Pearlmutter (1989), etc.

<br>

#### 2.2 Time-Delay Neural Network (TDNN)
- Lang et al. (1990)
- TDNN seem to be **practical for short time lags only**.
  - Not practical for the **long term lags**.
- It updates unit activations based on a weighted sum of old activations.
  - cf.) de Vries and Principe (1991)
- Further variant : NARX network

<br>

#### 2.3 Time Constants
- To deal with **long time lags**, Mozer (1992) uses time constants influencing changes of unit activations.
- However, the time constants need external fine tuning.
- Sun et al. (1993) updates the activation of a recurrent unit by adding the old activation and the (scaled) current net input.
  - Still, the net input tends to perturb the stored information.
  - As a result, the long-term storage is impractical.

<br>

#### 2.4 Ring's Approach
- Ring (1993) proposed a method for bridging **long time lags**.
- How?)
  - Whenever a unit in his network receives conflicting error signals, he adds a higher order unit influencing appropriate connections.
- Effect and Limit)
  - Some times extremely fast.
  - As the steps involved in a time lag increases, more units should be added.
    - e.g.) A time lag involving 100 steps require the addition of 100 units.
  - Also, Ring's net does not generalize to unseen lag durations.
    - i.e.) The duration of the lag should be specified.

<br>

#### 2.5 Bengio et al.'s Approaches
- Suggested the followings
  - simulated annealing, multi-grid random search, time-weighted pseudo-Newton optimization, and discrete error propagation.
  - EM approach for propagating targets
    - Provided $n$ state networks, this system can be in one of only $n$ different states.
    - Limit)
      - Require an unacceptable number of states to solve continuous problems.

<br>

#### 2.6 Kalman Filter Trained Recurrent Network 
- Puskorius and Feldkamp (1994) use Kalman filter techniques to improve recurrent net performance.
- How?)
  - It uses the derivative discount factor imposed to decay exponentially the effects of past dynamic derivatives
- Limit)
  - Not verified to be useful for long minimal time lags.

<br>

#### 2.7 Second Order Nets
- Multiplicative Units (MUs) can be used to protect error flow from unwanted perturbations.
  - LTSM to be presented in this paper uses this.
  - Previous works used this as well.
    - e.g.) 
      - Watrous and Kuhn (1992)
        - But the key differences with LTSM is that...
          - They do not enforce constant error flow.
          - Not designed to solve long time lag problems
          - Takes $O(W^2)$ operations per time step, while LTSM takes $O(W)$.
      - Miller an Giles (1993)

<br>

#### 2.8 Simple Weight Guessing
- How?)
  - Simply randomly initialize all network weights until the resulting net happens to classify all training sequences correctly.
- Effect)
  - Solved many of the problems in [Bengio et al.'s Approaches](#25-bengio-et-als-approaches) and [Miller an Giles](#27-second-order-nets).
- Limits)
  - More realistic tasks require either many free parameters or high weight precision.
  - This makes guessing infeasible.

<br>

#### 2.9 Adaptive Sequence Chunkers
- Schmidhuber's hierarchical chunker system have a capability to bridge arbitrary time lags.
  - Only if there is local predictability across the subsequences causing the time lags.
- Effect)
  - Rapidly solve certain grammar learning tasks involving minimal time lags in excess of 1000 steps.
- Limit)
  - The chunker system deteriorates as the noise level increases and the input sequences become less compressible.
    - LTSM does not suffer from this problem.


<br><br>

## 3. Constant Error Backprop
### 3.1 Exponentially Decaying Error
#### 3.1.1 Conventional BPTT (Back-Propagation Through Time)
- e.g.) *Williams and Zipser 1992*
- Model)
  - Let
    - $i,j$ : units
      - where $j$ outputs to $i$
    - $w_{ij}$ : the weight on the connection from unit $j$ to $i$
    - $f_i$ : the differentiable activation function of $i$
    - $y^i(t) = f_i\left(\textrm{net}_i(t)\right)$ : the activation of a non-input unit $i$ with differentiable activation function $f_i$ at time $t$
      - where 
        - $\displaystyle\textrm{net}_i(t) = \sum_j w_{ij} y^j (t-1)$ : unit $i$'s current net input
  - Using mean squared error, unit $k$'s error signal goes
    - $`\vartheta_k(t) = f_k'\left(\textrm{net}_k(t)\right) \;\left(d_k(t)-y^k(t)\right)`$
      - where
        - $d_k(t)$ : Output unit $k$'s target at time $t$
  - Thus, some non-output unit $j$'s backpropagated error signal is
    - $`\displaystyle\vartheta_j(t) = f_j'\left(\textrm{net}_j(t)\right)\sum_j w_{ij} \vartheta_i(t+1)`$
      - why?)
        - Backpropagating from $i$ to $j$.
  - Then, for an arbitrary unit $l$ connected to $j$
    - $\alpha\vartheta_j(t)y^l(t-1)$ : the corresponding contribution to $w_{jl}$'s total weight update
      - where $\alpha$ is the learning rate


<br>

#### 3.1.2 Local Error Flow 
*Outline of Hochreiter's Analysis (1991, page 19-21)*
- Setting)
  - Consider a fully connected net whose non-input unit indices range from 1 to $n$.
- Local Error Flow)
  - Let $u$, $v$ be units of the net.
  - Then the error occurring at an arbitrary unit $u$ at the time step $t$ is propagated "back into time" for $q$ time steps to an arbitrary unit $v$.
    - The factor that scales the error will be   
      $`\begin{aligned}
        \displaystyle\frac{\partial \vartheta_v (t-q)}{\partial \vartheta_u(t)} = 
        \begin{cases}
          f_v'(\textrm{net}_v(t-1)) w_{uv} & q=1 \\
          f_v'(\textrm{net}_v(t-q)) \displaystyle\sum_{l=1}^n \frac{\partial \vartheta_l(t-q+1)}{\partial \vartheta_u(t)} & q \gt 1
        \end{cases}
      \end{aligned}`$
  - Putting $l_q = v$ and $l_0 = u$, we obtain **the local error flow formula**   
    $`\displaystyle \frac{\partial \vartheta_v (t-q)}{\partial \vartheta_u(t)} = \sum_{l_1=1}^n \cdots \sum_{l_{q-1}=1}^n \prod_{m=1}^q f_{l_m}'\left(\textrm{net}_{l_m}(t-m)\right)w_{l_m l_{m-1}}`$
    - Here, the sum of all the $n^{q-1}$ terms $`\prod_{m=1}^q f_{l_m}'\left(\textrm{net}_{l_m}(t-m)\right)w_{l_m l_{m-1}}`$ determines the total error back flow.
      - cf.) Since the summation terms may have different signs, increasing the number of units $n$ does not necessarily increase error flow.
    - Intuitive Explanation)
      - Explosive / Vanishing Error)
        - If $`\left|f_{l_m}'\left(\textrm{net}_{l_m}(t-m)\right)w_{l_m l_{m-1}}\right| \gt 1.0`$ for all $m$
          - then the largest product increases exponentially with $q$.
          - i.e.) The error blows up.
            - Conflicting error signals arriving at unit $v$ can lead to oscillating weights and unstable learning.
        - If $`\left|f_{l_m}'\left(\textrm{net}_{l_m}(t-m)\right)w_{l_m l_{m-1}}\right| \lt 1.0`$ for all $m$
          - then the largest product decreases exponentially with $q$.
          - i.e.) The error vanishes.
            - Nothing can be learned in acceptable time.
    - Further Assumption)
      - Suppose $f_{lm}$ is the logistic sigmoid function.
        - Then the maximal value of $f_{lm}'$ is $0.25$.
      - If $y^{l_{m-1}}$ is constant and not equal to zero then    
        $`\begin{aligned}
          \left|f_{l_m}'\left(\textrm{net}_{l_m}\right)w_{l_m l_{m-1}}\right|
          \begin{cases}
            \textrm{takes on maximal values} & \textrm{for } \displaystyle w_{l_m l_{m-1}} = \frac{1}{y^{l_{m-1}}} \coth\left(\frac{\textrm{net}_{l_m}}{2}\right) \\
            \textrm{goes to zero} & \textrm{for }  \left|w_{l_m l_{m-1}}\right|\rightarrow\infty \\
            \textrm{is less than } 1.0 & \textrm{for }\left|w_{l_m l_{m-1}}\right|\lt 4.0
          \end{cases}
        \end{aligned}`$ 
      - Interpretation)
        - With conventional **logistic sigmoid** activation functions...
          1. The error flow tends to **vanish** as long as the weights have absolute values below $4.0$, especially in the beginning of the training phase.
          2. Using larger initial weights will not help.
             - Why?)
               - For $`\left|w_{l_m l_{m-1}}\right|\rightarrow\infty`$, the relevant derivatives goes to zero "faster" than the absolute weight can grow.
          3. Increasing learning rate does not help either.
             - Why?)
               - It will not change the ratio of long-range error flow and short-range error flow.

<br>

#### 3.1.3 Global Error Flow
- The local error flow analysis above shows that global error flow vanishes too.
  - How?)
    - Compute the following.   
      $`\displaystyle\sum_{u: \textrm{ output unit}}\frac{\partial\vartheta_v(t-q)}{\partial\vartheta_u(t)}`$

<br>

#### 3.1.4 Weak Upper Bound for Scaling Factor
- The Weak Upper Bound)
  - Settings)
    - Let's rewrite [the local error flow formula](#312-local-error-flow) as the following.
      - $`\displaystyle\left(W_{u^\top}\right)^\top F'(t-1) \prod_{m=2}^{q-1}\left(W F'(t-m)\right) W_v f_v'\left(\textrm{net}_v(t-q)\right)`$
        - where
          - $W$ : the weight **matrix** defined by $\left[W\right]_{ij}\equiv w_{ij}$
          - $W_v$ : unit $v$'s outgoing weight **vector** defined by $\left[W_v\right]_{i}\equiv\left[W\right]_{iv}=w_{iv}$
          - $W_{u^\top}$ : unit $u$'s incoming weight **vector** defined by $\left[W_{u^\top}\right]_{i}\equiv\left[W\right]_{ui}=w_{ui}$
          - $`F'(t-m)`$ : the **diagonal matrix** of first order derivatives defined as   
            - $`\begin{aligned}
                \left[F'(t-m)\right]_{ij} = 
                \begin{cases}
                  0 & i \ne j \\
                  f_i'(\textrm{net}_i(t-m)) & \textrm{otherwise}
                \end{cases}
            \end{aligned}`$
        - Notations)
          - $`\left[A\right]_{ij}`$ is the element in the $i$-th column and $j$-th row of matrix $A$.
          - $`\left[x\right]_i`$ is the $i$-th component of vector $x$.
    - Define $`f'_{\max}\equiv\max_{m=1,\cdots,q}\left\lbrace || F'(t-m) ||_A \right\rbrace`$.
      - where
        - $||\cdot||_A$ : a matrix norm compatible with vector norm $||\cdot||_x$
  - The Bound)
    - $`\begin{aligned}
  \displaystyle\left|\frac{\partial\vartheta_v(t-q)}{\partial\vartheta_u(t)}\right| & \le & n(f_{\max}')^q \; || W_v ||_x \; || W_{u^\top} ||_x \; || W ||_A^{q-2} & \le & n\left(f_{\max}' ||W||_A\right)^q
\end{aligned}`$
  - How?)
    - Consider the followings. 
      - $`|x^\top y| \le n ||x||_x ||y||_y`$
        - for $`\max_{i=1,\cdots,n}\left\lbrace |x_i| \right\rbrace \le ||x||_x`$
      - $`|f_v'(\textrm{net}_v(t-q))| \le || F'(t-q) ||_A \le f_{\max}'`$.
      - $`\begin{cases}
        || W_v ||_x \; = || W_{e_v} ||_x \; \le || W ||_A \; || e_v ||_x \;  \le || W ||_A \; \\
        || W_{u^\top} ||_x \; = || e_u W ||_x \; \le || W ||_A \; || e_u ||_x \;  \le || W ||_A \; 
      \end{cases}`$
        - where $e_k$ is the unit vector whose components are $0$ except for the $k$-th component, which is $1$.
- Props.)
  - This bound is a weak extreme case upper bound.
    - It will be reached only if 
      1. All $`|| F'(t-m) ||_A`$ take on maximal values 
      2. The contribution of all paths across which error flows back from unit $u$ to unit $v$ have the same sign.
    - However, large $||W||_A$ typically result in small values of $`|| F'(t-m) ||_A`$.
      - *Hochreiter, 1991*
      - e.g.)
        - Suppose
          - $`\displaystyle||W||_A \equiv \max_r\sum_s |w_{rs}|`$
          - $`\displaystyle||x||_x \equiv \max_r|x_r|`$
          - $`f_{\max}'= 0.25`$ for the logistic sigmoid function.
        - The author observed that
          - If $`\displaystyle|w_{ij}| \le w_{\max} \lt \frac{4.0}{n} \; \forall i, j`$
            - then $`||W||_A \le n w_{\max} \lt 4.0`$ will result in exponential decay.
          - By setting $\displaystyle\tau\equiv \frac{n w_{\max}}{4.0} \lt 1.0$,
            - the author obtained $`\displaystyle \left|\frac{\partial\vartheta_v(t-q)}{\partial\vartheta_u(t)}\right| \le n(\tau)^q`$.

<br><br>

### 3.2 Constant Error Flow : Naive Approach
- Why we need the constant error flow?)
  - Recall that the error flow easily explodes or vanishes.
  - In order to prevent this, we should get a constant error flow.
  - How?)
    - [Constant Error Carrousel (CEC)](#concept-constant-error-carrousel-cec)


#### Concept) Constant Error Carrousel (CEC)
- Settings)
  - A Single Unit Connected to itself
    - Suppose a unit $j$ is connected to itself.
      - Then, $j$'s local error back flow goes as follows.
        - $`\vartheta_j(t) = f_j'(\textrm{net}_j(t)) \; \vartheta_j(t+1) \; w_{jj}`$
- Derivation)
  - Recall that we want to enforce the error flow to be constant.
    - i.e.) $`f_j'(\textrm{net}_j(t)) \; \; w_{jj} = 1`$
  - Thus, $f_j$ has to be linear and unit $j$'s activation function should remain constant.
    - i.e.) $y_j(t+1) = f_j(\textrm{net}_j(t+1)) = f_j(w_{jj} y^j(t)) = y^j(t)$
  - In the experiments, this will be ensured by 
    - using the identity function $f_j : f_j(x) = x, \forall x$
    - setting $w_{jj}=1.0$
  - The author refers to this the **Constant Error Carrousel**.
- Props.)
  - There are problems when unit $j$ is connected to other units.
    1. Input weight conflict
       - Desc.)
         - For simplicity, assume a single additional input weight $w_{ji}$.
    2. Output weight conflict


---
* [Back to Main](../../README.md)