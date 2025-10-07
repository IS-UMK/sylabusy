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

### Projekt praktyczny:

**Opcja 1: Konkurencyjny solver problemu**
- Wybrany problem NP-hard (np. TSP, Graph Coloring)
- Implementacja kilku podejść (greedy, DP, approximation)
- Porównanie wydajności
- Raport z analizą złożoności

**Opcja 2: Biblioteka struktur danych**
- Implementacja 5-10 zaawansowanych struktur
- Testy jednostkowe
- Benchmarki wydajności
- Dokumentacja i przykłady użycia

**Opcja 3: Problem grafowy**
- Aplikacja rozwiązująca realny problem (np. routing, scheduling)
- Algorytmy grafowe
- Wizualizacja
- Analiza złożoności

### Zależności:

**Wymagane wcześniejsze zagadnienia:**
- Wstęp do algorytmów I i II (podstawowe struktury danych)
- Matematyka dyskretna (teoria grafów, rekurencja, asymptotyka)
- Programowanie obiektowe (dla implementacji złożonych struktur)
- Dowodzenie poprawności algorytmów

**Przygotowuje do:**
- Rozmów rekrutacyjnych (coding interviews)
- Olimpiad programistycznych
- Competitive programming
- Optymalizacji w produkcji
- Badań naukowych w algorytmice

### Cele edukacyjne:

- Głębokie zrozumienie analizy złożoności
- Umiejętność wyboru odpowiedniej struktury danych do problemu
- Znajomość klasycznych algorytmów i ich zastosowań
- Umiejętność projektowania efektywnych algorytmów
- Rozumienie ograniczeń obliczeniowych (NP-completeness)
- Praktyka w implementacji złożonych struktur danych

### Połączenie ze specjalizacjami:

- **Wszystkie specjalizacje**: Fundamentalny przedmiot
- **AI/ML**: Algorytmy optymalizacyjne, struktury danych dla dużych zbiorów
- **Gaming**: Pathfinding (A*), spatial data structures
- **Networking**: Routing algorithms, grafowe problemy sieciowe
- **Data Science**: Efektywne przetwarzanie dużych zbiorów danych
- **Competitive Programming**: Przygotowanie do zawodów

### Format zajęć:

**Wykład:** Teoria, dowody, analiza złożoności

**Laboratorium:**
- Implementacja algorytmów w C++/Python
- Analiza wydajności (benchmarking)
- Problem solving sessions
- Mini-konkursy algorytmiczne (codeforces-style)

**Materiały:**
- "Introduction to Algorithms" (CLRS)
- "Algorithm Design" (Kleinberg & Tardos)
- Platformy: LeetCode, Codeforces, AtCoder, HackerRank

Kurs jest intensywny i wymagający, ale przygotowuje do najwyższego poziomu w programowaniu konkurencyjnym i profesjonalnym.
