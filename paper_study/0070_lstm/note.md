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
#### 3.1.1 Conventional BPTT


<br>



---
* [Back to Main](../../README.md)