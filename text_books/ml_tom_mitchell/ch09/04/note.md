* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 9.4 Hypothesis Space Search

#### Analysis) GA
1. The GA search is less likely to fall into the same kind of local minima.
   - Why?)
     - Recall that the Backpropagation utilized the gradient descent search which moves smoothly from one hypothesis to a new hypothesis that is very similar.
     - In contrast, the GA search can move much more abruptly, replacing a parent hypothesis by an offspring that may be radically different from the parent.
2. Crowding Problem
   - Desc.)
     - A phenomenon in which some **individual that is more highly fit** than others in the population quickly reproduces, so that copies of this individual and **very similar individuals take over a large fraction of the population**.
   - Why matters?)
     - It reduces the diversity of the population, thereby **slowing further progress** by the GA.
   - Sol.)
     1. Alter the selection function, using criteria such as [tournament selection or rank selection](../02/note.md#concept-fitness-function) in place of fitness proportionate roulette wheel selection.
     2. Fitness Sharing
        - Desc.)
          - The measured fitness of an individual is reduced by the presence of other, similar individuals in the population.
     3. Restrict the kinds of individuals allowed to recombine to form offspring.
        - Desc.)
          - By allowing only the most similar individuals to recombine, we can encourage the formation of clusters of similar individuals, or multiple "subspecies" within the population.

<br><br>

## 9.4.1 Population Evolution and the Schema Theorem
### Theorem) The Schema Theorem
- Motivation)
  - A mathematical characterization of the evolution over time of the population within a GA.
  - Based on the concept **schemas**
    - i.e.) patterns that describe sets of bit strings.
- Settings)
  - Concept) Schema
    - A string composed of $`0`$s, $`1`$s, and $`*`$s.
      - e.g.) $`0*10 \equiv \{0010, 0110\}`$
      - Prop.)
        - An individual $n$-length bit string is a representative of $2^n$ distinct schemas.
          - e.g.) $0010$ represents $`0010, *010, 0*10, \cdots, 0***, \textrm{ and } ****`$
        - . Similarly, **a population of bit strings can be viewed in terms of the set of schemas that it represents and the number of individuals associated with each of these schema.**
  - Notations)
    - $s$ : a schema
    - $t$ : a time or the $t$-th generation
    - $m(s,t)$ :  the number of instances of schema $s$ in the population at time $t$ 
      - cf.) The goal of this theorem is to describe $E[m(s,t+1)]$ in terms of $m(s,t)$
    - $h$ : an individual bit string
      - $h \in s\cap p_t$ where $p_t$ is the population at $t$
        - i.e.) The individual $h$ is both a representative of schema $s$ and a member of the population at time $t$.
    - $f(h)$ : the fitness of $h$
    - $\bar{f}(t)$ : the average fitness of ALL individuals in the population at time $t$
    - $n$ : the total number of individuals in the population
    - $\hat{u}(s,t)$ : the average fitness of instances of schema $s$ in the population at time $t$

#### Result) 
$E[m(s,t+1)]=\frac{\hat{u}(s,t)}{\bar{f}(t)}m(s,t)$
- Derivation)
  - The probability distribution for **selection** can be denoted as follows:
    - $\displaystyle Pr(h) = \frac{f(h)}{\sum_{i=1}^n f(h_i)} = \frac{f(h)}{n\bar{f}(t)}$
  - If we select one member for the new population according to this probability distribution, then the probability that we will select a representative of schema $s$ is
    - $`\displaystyle Pr(h\in s) = \sum_{h \in s\cap p_t}Pr(h) = \sum_{h \in s\cap p_t}\frac{f(h)}{n\bar{f}(t)} = \frac{\hat{u}(s,t)\space m(s,t)}{n\bar{f}(t)} \; \left(\because \textrm{by def. }\hat{u}(s,t) = \frac{\sum_{h \in s\cap p_t}f(h)}{\space m(s,t)}\right)`$
  - Consider that every individual $h$ will go through the selection step.
    - i.e.) There will be $n$ times of **independent** selection steps.
  - Thus, the expected number of instances of $s$ resulting from $n$ independent selection steps is...
    - $`n \cdot Pr(h\in s) = \frac{\hat{u}(s,t)\space m(s,t)}{\bar{f}(t)}`$
  - This number of instances of $s$ will create the entire new generation.
  - $\therefore E[m(s,t+1)] = \frac{\hat{u}(s,t)}{\bar{f}(t)}m(s,t)$
- Props.)
  - The expected number of instances of schema $s$ at generation $t + 1$, $E[m(s,t+1)]$, is...
    1. **proportional** to the average fitness $\hat{u}(s,t)$ of instances of this schema at time $t$
    2. **inversely proportional** to the average fitness $\bar{f}(t)$ of all members of the population at time $t$.
  - Thus, we can expect **schemas with above average fitness** to be represented with increasing frequency on successive generations.
    - i.e.) More fit schemas will grow in influence over time.

<br>

#### Extension) Considering Crossover and Mutation
- Settings)
  - $p_c$ : the probability that the **single-point crossover** operator will be applied to an arbitrary individual.
  - $p_m$ : the probability that an arbitrary bit of an arbitrary individual will be **mutated** by the mutation operator
  - $o(s)$ : the number of **defined bits** in schema $s$, where $0$ and $1$ are defined bits, but $`*`$ is not.
  - $d(s)$ : the distance between the leftmost and rightmost defined bits in $s$
  - $l$ : the distance between the leftmost and rightmost defined bits in
- Result)
  - $`\begin{align}
    E[m(s,t+1)] \ge & \underbrace{\frac{\hat{u}(s,t)}{\bar{f}(t)}m(s,t)} \; & \underbrace{\left(1-p_c\frac{d(s)}{l-1}\right)} \; & \underbrace{(1-p_m)^{o(s)}} \\
    & \textrm{selection} & \textrm{crossover} & \textrm{mutation} 
  \end{align}`$


<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)