# Kruskal’s Algorithm for a Minimal Spanning Tree

Kruskal’s algorithm is a **greedy algorithm** used to find a **minimal spanning tree (MST)** in a connected, weighted, undirected graph. The goal of the algorithm is to connect all the vertices in the graph with the minimum possible total edge weight without forming cycles.

Here’s a detailed step-by-step explanation of Kruskal’s algorithm, along with the mathematical ideas behind it:

### Step 1: Definition and Notation

Let’s define the problem formally:

- Let \( G = (V, E) \) be a connected, undirected graph where \( V \) is the set of vertices and \( E \) is the set of edges.
- Each edge \( e \in E \) has an associated weight \( w(e) \), which is a real number representing the "cost" of that edge.
- The goal is to find a **spanning tree** \( T \) (a subgraph of \( G \) that connects all the vertices without cycles) such that the sum of the edge weights in \( T \) is minimized. This is called the **minimal spanning tree**.

### Step 2: Initialization

Kruskal's algorithm begins by initializing a few key components:

1. **Edge List**: Collect all the edges \( E \) in a list and sort them by their weights in **non-decreasing order**:
   \[
   \text{Sort } E \text{ so that } w(e_1) \leq w(e_2) \leq \dots \leq w(e_m)
   \]
   where \( m \) is the number of edges.

2. **Forest Initialization**: Initialize a **forest** (a collection of trees) where each vertex is its own tree. Initially, each vertex is considered as a separate component.

### Step 3: Greedily Select the Minimum Edge

Kruskal's algorithm uses a greedy strategy. The algorithm iterates over the sorted edge list and performs the following steps:

1. **Pick the Minimum Weight Edge**: Consider the edge \( e = (u, v) \) with the smallest weight from the sorted list.
2. **Cycle Check**: Check if adding the edge \( e = (u, v) \) forms a cycle. This is done using **disjoint-set data structures** (also known as union-find structures). A cycle would occur if \( u \) and \( v \) are in the same tree (component).
   - If \( u \) and \( v \) are in **different components**, add the edge to the MST.
   - If \( u \) and \( v \) are in the **same component**, skip the edge to avoid forming a cycle.
3. **Union**: If \( u \) and \( v \) are in different components, **union** their components, meaning that you merge the two trees together.

Mathematically, this is represented as finding the **union of sets** in the disjoint-set data structure. We use two operations:

- **Find**: Find the root or representative of the component (tree) containing a vertex.
- **Union**: Merge two components into one.

### Step 4: Repeat Until the MST is Found

Continue the process until:

- The MST contains exactly \( |V| - 1 \) edges (where \( |V| \) is the number of vertices).
- The forest becomes a single connected tree that spans all the vertices.

### Step 5: The Result is a Minimal Spanning Tree

The resulting tree \( T \) will be a **minimal spanning tree**. By construction, Kruskal’s algorithm ensures that the total weight of the tree is minimized because we always add the smallest edge possible without forming a cycle.

### Theoretical Justification

Kruskal’s algorithm works correctly due to the following mathematical properties:

1. **Greedy Choice Property**: The algorithm makes a series of locally optimal (greedy) choices by always picking the smallest edge that doesn't form a cycle. This ensures that the global solution is optimal because every edge added is the smallest possible and doesn't introduce a cycle.
2. **Cut Property**: In any graph, for any cut (a partition of the vertices into two sets), the **minimum weight edge crossing the cut** belongs to the MST. Kruskal's algorithm implicitly exploits this property by always adding the minimum edge that connects two different components (trees).

### Complexity of Kruskal’s Algorithm

The time complexity of Kruskal’s algorithm is dominated by two main tasks:

1. **Sorting the edges**: Sorting takes \( O(m \log m) \), where \( m \) is the number of edges.
2. **Union-Find operations**: Each union and find operation can be done in nearly constant time \( O(\alpha(n)) \) using the union-find data structure with **path compression** and **union by rank**, where \( \alpha(n) \) is the **inverse Ackermann function**, which grows very slowly.

Thus, the total time complexity of Kruskal’s algorithm is:

\[
O(m \log m + n \alpha(n))
\]

where \( n \) is the number of vertices and \( m \) is the number of edges. In most cases, this simplifies to \( O(m \log m) \) because sorting dominates the overall complexity.

### Conclusion

Kruskal's algorithm is an efficient method for finding the minimal spanning tree in a graph by following a greedy approach that adds edges in increasing order of weight while avoiding cycles. It is both optimal and simple, making it a popular choice for MST problems.
