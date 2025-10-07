#!/usr/bin/env python3
"""
Narzędzie do wizualizacji i zarządzania grafem zależności przedmiotów.
Wykorzystuje graf_zaleznosci.json do:
- Wizualizacji zależności w formacie Mermaid
- Walidacji spójności grafu (brak cykli, wszystkie zależności zdefiniowane)
- Generowania ścieżki nauki dla danej specjalizacji
"""

import json
import sys
from typing import Set, List, Dict, Any
from collections import defaultdict, deque


def load_graph(filename='graf_zaleznosci.json'):
    """Wczytuje graf zależności z pliku JSON."""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


def validate_graph(graph: Dict[str, Any]) -> List[str]:
    """
    Waliduje spójność grafu zależności.
    Zwraca listę błędów (pusta jeśli graf jest poprawny).
    """
    errors = []
    concepts = graph['concepts']
    
    # Sprawdź czy wszystkie zależności istnieją
    for concept_id, concept_data in concepts.items():
        for dep in concept_data.get('dependencies', []):
            if dep not in concepts:
                errors.append(f"Concept '{concept_id}' depends on undefined concept '{dep}'")
    
    # Sprawdź czy nie ma cykli (topological sort)
    try:
        topological_sort(concepts)
    except ValueError as e:
        errors.append(f"Cycle detected in dependencies: {e}")
    
    return errors


def topological_sort(concepts: Dict[str, Any]) -> List[str]:
    """
    Zwraca posortowaną topologicznie listę konceptów.
    Rzuca ValueError jeśli wykryto cykl.
    """
    # Oblicz in-degree dla każdego konceptu
    in_degree = defaultdict(int)
    graph = defaultdict(list)
    
    for concept_id, concept_data in concepts.items():
        if concept_id not in in_degree:
            in_degree[concept_id] = 0
        for dep in concept_data.get('dependencies', []):
            graph[dep].append(concept_id)
            in_degree[concept_id] += 1
    
    # BFS (Kahn's algorithm)
    queue = deque([c for c in concepts if in_degree[c] == 0])
    sorted_concepts = []
    
    while queue:
        concept = queue.popleft()
        sorted_concepts.append(concept)
        
        for neighbor in graph[concept]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(sorted_concepts) != len(concepts):
        raise ValueError("Graph contains a cycle")
    
    return sorted_concepts


def generate_mermaid_graph(graph: Dict[str, Any], max_concepts: int = 50) -> str:
    """Generuje diagram Mermaid dla grafu zależności."""
    concepts = graph['concepts']
    
    # Weź tylko pierwsze max_concepts konceptów dla czytelności
    concept_list = list(concepts.items())[:max_concepts]
    
    mermaid = ["graph TD"]
    
    for concept_id, concept_data in concept_list:
        # Dodaj węzeł z nazwą
        node_label = concept_data['name'].replace('"', '\\"')
        semester = concept_data.get('semester', '?')
        mermaid.append(f'    {concept_id}["{node_label}<br/>(sem {semester})"]')
        
        # Dodaj krawędzie
        for dep in concept_data.get('dependencies', []):
            if dep in dict(concept_list):
                mermaid.append(f'    {dep} --> {concept_id}')
    
    return '\n'.join(mermaid)


def generate_specialization_path(graph: Dict[str, Any], specialization: str) -> List[str]:
    """
    Generuje zalecaną ścieżkę nauki dla danej specjalizacji.
    Zwraca listę konceptów w kolejności topologicznej.
    """
    if specialization not in graph['specializations']:
        raise ValueError(f"Unknown specialization: {specialization}")
    
    spec_data = graph['specializations'][specialization]
    key_concepts = set(spec_data['key_concepts'])
    
    # Zbierz wszystkie wymagane koncepty (z zależnościami)
    required = set()
    to_process = list(key_concepts)
    
    while to_process:
        concept = to_process.pop()
        if concept in required or concept not in graph['concepts']:
            continue
        required.add(concept)
        deps = graph['concepts'][concept].get('dependencies', [])
        to_process.extend(deps)
    
    # Sortuj topologicznie
    sorted_all = topological_sort(graph['concepts'])
    path = [c for c in sorted_all if c in required]
    
    return path


def print_specialization_info(graph: Dict[str, Any]):
    """Wypisuje informacje o dostępnych specjalizacjach."""
    print("\n=== DOSTĘPNE SPECJALIZACJE ===\n")
    
    for spec_id, spec_data in graph['specializations'].items():
        print(f"## {spec_data['name']}")
        print(f"{spec_data['description']}\n")
        print("Kluczowe koncepty:")
        for concept in spec_data['key_concepts']:
            if concept in graph['concepts']:
                print(f"  - {graph['concepts'][concept]['name']}")
        print("\nPodstawowe kursy:")
        for course in spec_data['foundation_courses']:
            if course in graph['courses']:
                print(f"  - {graph['courses'][course]['name']}")
        print("\n" + "="*50 + "\n")


def main():
    """Główna funkcja programu."""
    if len(sys.argv) < 2:
        print("Użycie:")
        print("  python graf_tools.py validate          - Waliduje graf")
        print("  python graf_tools.py mermaid [N]       - Generuje diagram Mermaid (max N konceptów)")
        print("  python graf_tools.py specializations   - Wyświetla informacje o specjalizacjach")
        print("  python graf_tools.py path <spec_id>    - Generuje ścieżkę nauki dla specjalizacji")
        sys.exit(1)
    
    command = sys.argv[1]
    graph = load_graph()
    
    if command == 'validate':
        errors = validate_graph(graph)
        if errors:
            print("BŁĘDY W GRAFIE:")
            for error in errors:
                print(f"  - {error}")
            sys.exit(1)
        else:
            print("✓ Graf jest poprawny (brak cykli, wszystkie zależności zdefiniowane)")
    
    elif command == 'mermaid':
        max_concepts = int(sys.argv[2]) if len(sys.argv) > 2 else 50
        print(generate_mermaid_graph(graph, max_concepts))
    
    elif command == 'specializations':
        print_specialization_info(graph)
    
    elif command == 'path':
        if len(sys.argv) < 3:
            print("Podaj ID specjalizacji (np. 'ai', 'gaming', 'networking')")
            sys.exit(1)
        spec_id = sys.argv[2]
        path = generate_specialization_path(graph, spec_id)
        
        spec_name = graph['specializations'][spec_id]['name']
        print(f"\n=== ŚCIEŻKA NAUKI: {spec_name} ===\n")
        
        current_sem = 0
        for concept_id in path:
            concept = graph['concepts'][concept_id]
            sem = concept.get('semester', '?')
            if sem != current_sem:
                current_sem = sem
                print(f"\n--- Semestr {sem} ---")
            print(f"  {concept['name']} ({concept['course']})")
    
    else:
        print(f"Nieznana komenda: {command}")
        sys.exit(1)


if __name__ == '__main__':
    main()
