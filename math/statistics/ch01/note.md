* [Back to Statistics Main](../main.md)

# Chapter 1. Descriptive Statistics

## 1.2 Basic Concepts

#### Def) Population
* A population is the collection or set of all objects or measurements that are of interest to
the collector

#### Def) Sample
* The sample is a subset of data selected from a population. The size of a sample is the
number of elements in it

#### Def) Descriptive Statistics
* The methods consisting mainly of organizing, summarizing, and presenting data in the form of tables, graphs, and charts

#### Def) Inferential Statistics
* The methods of drawing inferences and making decisions about the population using the sample

#### Def) Statistical Inference
* An estimate, a prediction, a decision, or a generalization about the population based on information contained in a sample

<br>

### 1.2.1 Types of Data

#### Concept) Quantitative vs Qualitative(Categorical) 
* Def) Quantitative Data
  * Observations measured on a numerical scale. 
* Def) Categorical data(Qualitative)
  * Nonnumerical data that can only be classified into one of the groups of categories
  * Types)
    1. Nominal Data : Data groups that do not have a specific order
    2. Ordinal Data : Data groups that should be listed in a specific order

#### Concept) Cross-sectional vs Time-series
* Def) Cross-sectional Data
  * Data collected on different elements or variables at the same point in time or for the same period of time
* Def) Time-series Data
  * Data collected on the same element or the same variable at different points in time or for different periods of time

<br><br>

## 1.3 Sampling Schemes

#### Concept) Census Study
* A study in which the entire population is included.
* It is usually not possible to obtain information on the entire population

#### Concept) Sample
  * Props)
    * Obtained by collecting information from only some members of the population
    * A good sample must reflect all the characteristics (of importance) of the population.
  * Types
    * Based on the quality
      1. Representative Sample
         * A sample that accurately reflects its population characteristics
      2. Biased Sample
         * A sample that is not representative of the population characteristics
    * Based on the way of sampling
      1. [Simple Random Sampling]()
      2. [Systemic Sampling]()
      3. [Stratified Sampling]()
      4. [Cluster Sampling (Area Sampling)]()
      5. [Multiphase sampling]()

#### Concept) Simple Random Sample
* Def)
  * A sample selected in such a way that every element of the population has an equal chance of being chosen
* Advantages)
  1. Ensures against possible investigator biases.
  2. Analytic computations are relatively simple, and probabilistic bounds on errors can be computed in many cases.
  3. Possible to estimate the sample size for a prescribed error level when designing the sampling procedure.

#### Concept) Systemic Sample
* Def)
  * A sample in which every $K$-th element in the sampling frame is selected after a suitable random start for the first element
* How?
  * List the population elements in some order 
    * e.g.) alphabetical order
  * Choose the desired sampling fraction.
    1. Number the elements of the population from 1 to N.
    2. Decide on the sample size, say $n$, that we need.
    3. Choose $K = N/n$.
    4. Randomly select an integer between 1 to $K$ .
    5. Then take every $K$-th element
* Advantage)
  * Easy to implement
* Disadvantage)
  * Possibility of bias in case...
    * $\exists$ correlation or association between successive elements
    * $\exists$ periodic structure

#### Concept) Stratified Sample
* Def) 
  * A sample obtained by stratifying (dividing into nonoverlapping groups) the sampling frame based on some factor or factors and then selecting some elements from each of the strata
* How to)
  1. Decide on the relevant stratification factors (sex, age, income, etc.).
  2. Divide the entire population into strata (subpopulations) based on the stratification criteria. Sizes of strata may vary.
  3. Select the requisite number of units using simple random sampling or systematic sampling from
  each subpopulation. The requisite number may depend on the subpopulation sizes.
* Prop)
  * A modification of simple random sampling and systematic sampling
  * Designed to obtain a more representative sample, but at the cost of a more complicated procedure.
* Advantages)
  * Reduces sampling error compared to random sampling
* Ex.) Sampling 100 children out of 1000.
  ![](./images/01_03_01.png)
  ![](./images/01_03_02.png)

#### Concept) Cluster Sampling (Area Sampling)
* Def) 
  * The sampling unit contains groups of elements called clusters instead of individual elements of the population
* Prop.) 
  * The clusters naturally exist and are not formed by the researcher for data collection.
* How to)
  * Take a simple random sample of groups and then sample all elements within the selected clusters
* Advantage)
  * Convenient
  * May be less precise than simple random sampling
    * why?)
      * It is likely that units in a cluster will be relatively homogeneous.

#### Concept) Multiphase Sampling
* Def)
  * Involve collection of some information from the whole sample and additional information either at the same time or later from subsamples of the whole sample. 
  * Basically a combination of the techniques presented earlier





* [Back to Statistics Main](../main.md)