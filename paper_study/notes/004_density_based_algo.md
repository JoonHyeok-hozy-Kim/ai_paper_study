* [Back to Main](../../README.md)
---

# A Density-Based Algorithm for Discovering Clusters in Large Spatial Database with Noise
### Martin Ester, Hans-Peter Kriegel, Jorg Sander, Xiaowei Xu
* [Read Paper](../paper_pdfs/231008%20density_based_algo.pdf)

---

## 1. Introduction
* The task considered in this paper is
class identification, i.e. the grouping of the objects of a database into meaningful subclasses.
* Requirements for clustering algorithms when applied to large spatial data.
  * **Minimal requirements of domain knowledge** to determine the input parameters, because appropriate values are often not known in advance when dealing with large databases.
  * **Discovery of clusters with arbitrary shape**, because the shape of clusters in spatial databases may be spherical, drawn-out, linear, elongated etc.
  * **Good efficiency on large databases**, i.e. on databases of significantly more than just a few thousand objects.
* This paper presents the new clustering algorithm DBSCAN.
  * DBSCAN 
    * Requires only one input parameter 
    * Supports the user in determining an appropriate value for it
    * Discovers clusters of arbitrary shape
    * Efficient even for large spatial databases.

<br><br>

## 2. Clustering Algorithms (Partitioning vs Hierarchical)
### 2.1 Partitioning Algorithms
* Props.)
  * Construct a partition of a database $D$ of $n$ objects into a set of $k$ clusters.
    * $k$ is an input parameter for these algorithms, i.e some domain knowledge is required which unfortunately is not available for many applications. 
  * Typically starts with an initial partition of $D$ and then uses an iterative control strategy to optimize an objective function. 
  * Each cluster is represented by the gravity center of the cluster ($k$-means algorithms) or by one of the objects of the cluster located near its center ($k$-medoid algorithms). 
  * Use a two-step procedure. 
    1. Determine $k$ representatives minimizing the objective function. 
    2. Assign each object to the cluster with its representative "closest" to the considered object. 
  * Very Restrictive.
    * Why?)
      * Consider the second step.
      * A partition is equivalent to a voronoi diagram 
      * Each cluster is contained in one of the voronoi cells. 
      * Thus, the shape of **all clusters found by a partitioning algorithm is convex** which is very restrictive.

#### Ex.) CLARANS (Clustering Large Applications based on RANdomized Search)
* An improved $k$-medoid method.
* Prop.)
  * Runs efficiently on databases of thousands of objects compared to former $k$-medoid algorithms
* Application)
  * Ng & Han (1994) 
    * Discuss methods to determine the "natural" number $k_{nat}$ of clusters in a database.
    * Run CLARANS **once** for each $k$ from 2 to n.
    * For each of the discovered clusterings the silhouette coefficient (Kaufman & Rousseeuw 1990) is calculated and the clustering with the maximum silhouette coefficient is chosen as the natural clustering
    * The run time of this approach is prohibitive for large n, because it implies $O(n)$ calls of CLARANS.
* Drawback
  * Assumes that all objects to be clustered can reside in main memory at the same time which does not hold for large database.
  * The run time of CLARANS is prohibitive on large databases
* DBSCAN's Improvement
  * Small enough to be memory resident and second
  * The run time of CLARANS on the objects of the focus is significantly less than its run time on the whole database.

<br>

#### 2.2 Hierarchical Algorithms
* Algorithms that create a hierarchical decomposition of the database $D$.
* Props.)
  * Represented by a *dendrogram*, a tree that iteratively splits $D$ into smaller subsets until each subset consists of only one object.
  * In such a hierarchy, each node of the tree represents a cluster of $D$.
  * Types
    1. Agglomerative Approach
       * From the leaves up to the root     
    2. Divisive Approach
       * From the root down to the leaves by merging or dividing clusters at each step
  * Do not need $k$ as an input.
    * [Partitioning Algorithms]() did.




---
* [Back to Main](../../README.md)