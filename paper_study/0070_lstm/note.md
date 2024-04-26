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

#### 3.1.2 Outline of Hochreiter's Analysis (1991, page 19-21)
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
  - Putting $l_q = v$ and $l_0 = u$, we obtain   
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




---
* [Back to Main](../../README.md)