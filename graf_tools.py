#!/usr/bin/env python3
"""
Narzędzie do wizualizacji i zarządzania grafem zależności przedmiotów.
Wykorzystuje graf_zaleznosci.json do:
- Wizualizacji zależności w formacie Mermaid
- Wizualizacji interaktywnej HTML (vis.js)
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


def generate_html_visualization(graph: Dict[str, Any], output_file: str = 'graf_zaleznosci.html'):
    """
    Generuje interaktywną wizualizację HTML grafu zależności używając vis.js.
    Nie wymaga dodatkowych zależności Python - wszystko w jednym pliku HTML.
    """
    courses = graph.get('courses', {})
    
    # Przygotuj dane dla vis.js
    nodes = []
    edges = []
    node_id_map = {}
    
    # Grupuj przedmioty według semestru
    semester_colors = {
        1: '#e3f2fd',  # Light blue
        2: '#e8f5e9',  # Light green
        3: '#fff3e0',  # Light orange
        4: '#f3e5f5',  # Light purple
        5: '#ffe0b2',  # Light deep orange
        6: '#ffebee',  # Light red
        7: '#e0f2f1',  # Light teal
    }
    
    # Dodaj węzły (przedmioty)
    for idx, (course_id, course_data) in enumerate(courses.items()):
        semester = course_data.get('semester', 0)
        color = semester_colors.get(semester, '#e0e0e0')
        
        label = f"{course_data['name']}\nSem {semester} ({course_data.get('ects', 0)} ECTS)"
        
        nodes.append({
            'id': idx,
            'label': label,
            'title': f"<b>{course_data['name']}</b><br/>Semestr: {semester}<br/>ECTS: {course_data.get('ects', 0)}<br/>Typ: {course_data.get('type', 'N/A')}",
            'color': color,
            'shape': 'box',
            'font': {'size': 14}
        })
        node_id_map[course_id] = idx
    
    # Dodaj krawędzie (zależności)
    for course_id, course_data in courses.items():
        from_id = node_id_map[course_id]
        for dep in course_data.get('dependencies', []):
            if dep in node_id_map:
                to_id = node_id_map[dep]
                edges.append({
                    'from': to_id,
                    'to': from_id,
                    'arrows': 'to',
                    'color': {'color': '#848484', 'highlight': '#ff0000'},
                    'width': 2
                })
    
    # Generuj HTML z vis.js
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Graf zależności - Informatyka Stosowana UMK</title>
    <script type="text/javascript" src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
    <style type="text/css">
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background: #f5f5f5;
        }}
        #header {{
            background: #1976d2;
            color: white;
            padding: 20px;
            text-align: center;
        }}
        #controls {{
            background: white;
            padding: 15px;
            margin: 10px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        #mynetwork {{
            width: 100%;
            height: 800px;
            border: 1px solid lightgray;
            background: white;
            margin: 10px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .button {{
            background: #1976d2;
            color: white;
            border: none;
            padding: 10px 20px;
            margin: 5px;
            border-radius: 3px;
            cursor: pointer;
            font-size: 14px;
        }}
        .button:hover {{
            background: #1565c0;
        }}
        #legend {{
            background: white;
            padding: 15px;
            margin: 10px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .legend-item {{
            display: inline-block;
            margin: 5px 15px;
        }}
        .legend-box {{
            display: inline-block;
            width: 20px;
            height: 20px;
            margin-right: 5px;
            vertical-align: middle;
            border: 1px solid #ccc;
        }}
        #info {{
            background: white;
            padding: 15px;
            margin: 10px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            min-height: 50px;
        }}
    </style>
</head>
<body>
    <div id="header">
        <h1>📊 Graf Zależności Przedmiotów</h1>
        <h3>Informatyka Stosowana - Uniwersytet Mikołaja Kopernika</h3>
    </div>
    
    <div id="controls">
        <button class="button" onclick="network.fit()">🔍 Dopasuj widok</button>
        <button class="button" onclick="filterBySemester(1)">Semestr 1</button>
        <button class="button" onclick="filterBySemester(2)">Semestr 2</button>
        <button class="button" onclick="filterBySemester(3)">Semestr 3</button>
        <button class="button" onclick="filterBySemester(4)">Semestr 4</button>
        <button class="button" onclick="filterBySemester(5)">Semestr 5+</button>
        <button class="button" onclick="showAll()">Pokaż wszystkie</button>
        <button class="button" onclick="highlightCriticalPath()">Ścieżka krytyczna</button>
    </div>
    
    <div id="legend">
        <strong>Legenda - Semestry:</strong>
        <div class="legend-item"><span class="legend-box" style="background: {semester_colors.get(1)}"></span>Semestr 1</div>
        <div class="legend-item"><span class="legend-box" style="background: {semester_colors.get(2)}"></span>Semestr 2</div>
        <div class="legend-item"><span class="legend-box" style="background: {semester_colors.get(3)}"></span>Semestr 3</div>
        <div class="legend-item"><span class="legend-box" style="background: {semester_colors.get(4)}"></span>Semestr 4</div>
        <div class="legend-item"><span class="legend-box" style="background: {semester_colors.get(5)}"></span>Semestr 5</div>
        <div class="legend-item"><span class="legend-box" style="background: {semester_colors.get(6)}"></span>Semestr 6</div>
        <div class="legend-item"><span class="legend-box" style="background: {semester_colors.get(7)}"></span>Semestr 7</div>
    </div>
    
    <div id="mynetwork"></div>
    
    <div id="info">
        <strong>ℹ️ Instrukcja:</strong> Kliknij i przeciągnij węzły. Kliknij na przedmiot, aby zobaczyć szczegóły. Przewiń, aby powiększyć/pomniejszyć.
    </div>
    
    <script type="text/javascript">
        var nodes = new vis.DataSet({json.dumps(nodes, ensure_ascii=False, indent=8)});
        
        var edges = new vis.DataSet({json.dumps(edges, ensure_ascii=False, indent=8)});
        
        var container = document.getElementById('mynetwork');
        var data = {{
            nodes: nodes,
            edges: edges
        }};
        
        var options = {{
            physics: {{
                enabled: true,
                solver: 'hierarchicalRepulsion',
                hierarchicalRepulsion: {{
                    nodeDistance: 200,
                    centralGravity: 0.3,
                    springLength: 150,
                    springConstant: 0.01,
                    damping: 0.09
                }},
                stabilization: {{
                    enabled: true,
                    iterations: 1000,
                    updateInterval: 25
                }}
            }},
            layout: {{
                hierarchical: {{
                    enabled: true,
                    direction: 'UD',
                    sortMethod: 'directed',
                    levelSeparation: 150,
                    nodeSpacing: 200
                }}
            }},
            interaction: {{
                hover: true,
                tooltipDelay: 200,
                navigationButtons: true,
                keyboard: true
            }},
            nodes: {{
                borderWidth: 2,
                borderWidthSelected: 4,
                chosen: {{
                    node: function(values, id, selected, hovering) {{
                        if (selected || hovering) {{
                            values.borderWidth = 4;
                            values.shadow = true;
                        }}
                    }}
                }}
            }}
        }};
        
        var network = new vis.Network(container, data, options);
        
        // Event listener dla kliknięć
        network.on("click", function(params) {{
            if (params.nodes.length > 0) {{
                var nodeId = params.nodes[0];
                var node = nodes.get(nodeId);
                document.getElementById('info').innerHTML = 
                    '<strong>Wybrany przedmiot:</strong> ' + node.title;
            }}
        }});
        
        // Filtrowanie według semestru
        var allNodeIds = nodes.getIds();
        var allEdgeIds = edges.getIds();
        
        function filterBySemester(semester) {{
            var filteredNodes = nodes.get({{
                filter: function(node) {{
                    return node.label.includes('Sem ' + semester);
                }}
            }});
            
            var filteredNodeIds = filteredNodes.map(n => n.id);
            
            // Ukryj wszystkie węzły
            allNodeIds.forEach(id => {{
                nodes.update({{id: id, hidden: true}});
            }});
            
            // Pokaż tylko wybrane
            filteredNodeIds.forEach(id => {{
                nodes.update({{id: id, hidden: false}});
            }});
            
            // Ukryj krawędzie
            allEdgeIds.forEach(id => {{
                edges.update({{id: id, hidden: true}});
            }});
            
            // Pokaż krawędzie między widocznymi węzłami
            edges.get().forEach(edge => {{
                if (filteredNodeIds.includes(edge.from) && filteredNodeIds.includes(edge.to)) {{
                    edges.update({{id: edge.id, hidden: false}});
                }}
            }});
            
            network.fit();
        }}
        
        function showAll() {{
            allNodeIds.forEach(id => {{
                nodes.update({{id: id, hidden: false}});
            }});
            allEdgeIds.forEach(id => {{
                edges.update({{id: id, hidden: false}});
            }});
            network.fit();
        }}
        
        function highlightCriticalPath() {{
            // Znajdź najdłuższą ścieżkę (implementacja uproszczona)
            alert('Funkcja w przygotowaniu - znajdzie najdłuższą ścieżkę zależności');
        }}
        
        // Stabilizacja zakończona
        network.on("stabilizationIterationsDone", function() {{
            network.setOptions({{physics: false}});
        }});
    </script>
</body>
</html>"""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✓ Wygenerowano interaktywną wizualizację: {output_file}")
    print(f"  Otwórz plik w przeglądarce, aby zobaczyć graf zależności.")
    return output_file


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
        print("  python graf_tools.py visualize [plik]  - Generuje interaktywną wizualizację HTML")
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
    
    elif command == 'visualize':
        output_file = sys.argv[2] if len(sys.argv) > 2 else 'graf_zaleznosci.html'
        generate_html_visualization(graph, output_file)
    
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
