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
  - Schema
    - A string composed of $0$s, $1$s, and $`*`$s.
      - e.g.) $`0\ast10 \equiv \{0010, 0110\}`$
      - Prop.)
        - An individual $n$-length bit string is a representative of $2^n$ distinct schemas.
          - e.g.) $0010$ represents $0010, *010, 0*10, \cdots, 0***, ****$







<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)