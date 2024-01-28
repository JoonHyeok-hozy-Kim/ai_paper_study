* [Back to Machine Learning Tom Mitchell Main](../../main.md)

# 9.7 Parallelizing Genetic Algorithms

### Concept) Coarse Grain Approach
- Desc.)
  - It subdivides the population into somewhat distinct groups of individuals, called *demes*.
  - Each *deme* is assigned to a different computational node, and a standard GA search is performed at each node.
  - Communication and cross-fertilization between demes occurs on a less frequent basis than within demes.
  - Transfer between demes occurs by a *migration* process, in which individuals from one deme are copied or transferred to other demes.
- Prop.)
  - Advantage)
    - It reduces the crowding problem often encountered in nonparallel GAs, in which the system falls into a local optimum due to the early appearance of a genotype that comes to dominate the entire population.
- e.g.)
  - Tanese (1989)
  - Cohoon et al. (1987).

<br>

### Concept) Fine Grain Approach
- Desc.)
  - It assigns one processor per individual in the population.
  - Recombination then takes place among neighboring individuals.
  - Several different types of neighborhoods have been proposed, ranging from planar grid to torus.
- e.g.)
  - Spiessens and Manderick (1991)
  - Stender (1993)


<br>

* [Back to Machine Learning Tom Mitchell Main](../../main.md)