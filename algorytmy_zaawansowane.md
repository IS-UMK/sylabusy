## Algorytmy i Struktury Danych (Zaawansowane)

Kurs wprowadza zaawansowane techniki algorytmiczne i złożone struktury danych. Nacisk kładziony jest na analizę złożoności, poprawność i efektywne rozwiązywanie problemów.

### Tematyka kursu:

1. **Analiza algorytmów - przypomnienie i rozszerzenie**
   - Notacja asymptotyczna (O, Ω, Θ)
   - Master Theorem dla rekurencji
   - Analiza amortyzowana
   - Probabilistyczna analiza algorytmów

2. **Algorytmy sortowania zaawansowane**
   - QuickSort i jego warianty (randomized, 3-way)
   - MergeSort i sortowanie external
   - HeapSort i kolejki priorytetowe
   - Sortowanie w czasie liniowym: Counting, Radix, Bucket sort
   - Dolne ograniczenie sortowania przez porównania

3. **Techniki projektowania algorytmów**
   
   **Divide and Conquer:**
   - Karatsuba (mnożenie liczb)
   - Strassen (mnożenie macierzy)
   - Closest pair of points
   
   **Programowanie dynamiczne:**
   - Najdłuższy wspólny podciąg (LCS)
   - Knapsack problem
   - Edit distance
   - Matrix chain multiplication
   - Optymalizacja czasu i pamięci
   
   **Algorytmy zachłanne:**
   - Activity selection
   - Huffman coding
   - Fractional knapsack
   - Dowodzenie poprawności greedy algorithms

4. **Struktury danych zaawansowane**
   
   **Drzewa zrównoważone:**
   - AVL trees
   - Red-Black trees
   - B-trees (użycie w bazach danych)
   - Splay trees
   
   **Kolejki priorytetowe:**
   - Binary heaps
   - Fibonacci heaps
   - Binomial heaps
   
   **Inne struktury:**
   - Skip lists
   - Tries (prefix trees)
   - Suffix trees i suffix arrays
   - Disjoint Set Union (Union-Find) z kompresją ścieżki
   - Segment trees
   - Fenwick trees (Binary Indexed Trees)

5. **Algorytmy grafowe**
   
   **Podstawowe traversale:**
   - BFS i DFS (przypomnienie)
   - Topological sort
   - Strongly connected components (Kosaraju, Tarjan)
   
   **Najkrótsze ścieżki:**
   - Dijkstra
   - Bellman-Ford
   - Floyd-Warshall
   - A* search
   
   **Minimalne drzewa rozpinające:**
   - Kruskal
   - Prim
   - Borůvka
   
   **Przepływy w sieciach:**
   - Ford-Fulkerson
   - Max-flow min-cut theorem
   - Zastosowania: bipartite matching
   
   **Inne:**
   - Cycle detection
   - Euler path/circuit
   - Hamiltonian path (NP-complete)

6. **Algorytmy na tekstach (String algorithms)**
   - Pattern matching:
     - Naive approach
     - KMP (Knuth-Morris-Pratt)
     - Boyer-Moore
     - Rabin-Karp
   - Suffix arrays i suffix trees
   - Longest common substring
   - Aho-Corasick (multiple pattern matching)

7. **Haszowanie (Hashing)**
   - Funkcje haszujące
   - Collision resolution: chaining vs open addressing
   - Universal hashing
   - Perfect hashing
   - Bloom filters
   - Consistent hashing (distributed systems)

8. **Wprowadzenie do NP-zupełności**
   - Klasy P, NP, NP-complete, NP-hard
   - Redukcje
   - Cook-Levin theorem
   - Przykłady problemów NP-complete:
     - SAT
     - 3-SAT
     - Traveling Salesman Problem
     - Knapsack (decision version)
     - Graph coloring
   - Techniki radzenia sobie z NP-hard:
     - Algorytmy aproksymacyjne
     - Heurystyki
     - Randomizacja

9. **Algorytmy randomizowane**
   - Las Vegas vs Monte Carlo
   - QuickSort randomizowany
   - Randomized selection (k-th smallest)
   - Primality testing (Miller-Rabin)
   - Skip lists

10. **Algorytmy geometryczne (podstawy)**
    - Convex hull (Graham scan, Jarvis march)
    - Line segment intersection
    - Closest pair of points
    - Voronoi diagrams (wprowadzenie)
