# Wizualizacja Programu Studiów

## Struktura całego programu

```mermaid
graph LR
    S1[Semestr I<br/>Fundamenty]
    S2[Semestr II<br/>Zaawansowane podstawy]
    S3[Semestr III<br/>Specjalizacje podstawowe]
    S4[Semestr IV<br/>Specjalizacje zaawansowane]
    S5_7[Semestry V-VII<br/>Głęboka specjalizacja]
    
    S1 --> S2
    S2 --> S3
    S3 --> S4
    S4 --> S5_7
    
    style S1 fill:#e1f5ff
    style S2 fill:#b3e5ff
    style S3 fill:#80d4ff
    style S4 fill:#4dc3ff
    style S5_7 fill:#1ab2ff
```

## Semestr I - Fundamenty (31 ECTS)

```mermaid
graph TD
    WMI[Wstęp do matematyki<br/>i informatyki<br/>6 ECTS]
    Unix[Wstęp do Unix<br/>3 ECTS]
    WProg[Wstęp do<br/>programowania<br/>5 ECTS]
    WAlgo1[Wstęp do<br/>algorytmów I<br/>6 ECTS]
    AM1[Analiza<br/>matematyczna I<br/>6 ECTS]
    AL1[Algebra<br/>liniowa I<br/>5 ECTS]
    
    Unix --> WProg
    WMI --> WAlgo1
    WProg --> WAlgo1
    
    style WMI fill:#ffcccc
    style AM1 fill:#ffcccc
    style AL1 fill:#ffcccc
    style Unix fill:#ccffcc
    style WProg fill:#ccccff
    style WAlgo1 fill:#ccccff
```

**Legenda:**
- 🔴 Czerwony: Matematyka
- 🟢 Zielony: Narzędzia i środowisko
- 🔵 Niebieski: Programowanie

## Semestr II - Zaawansowane podstawy (31 ECTS)

```mermaid
graph TD
    MD[Matematyka<br/>dyskretna<br/>6 ECTS]
    WAlgo2[Wstęp do<br/>algorytmów II<br/>6 ECTS]
    PC[Projektowy C<br/>4 ECTS]
    AL2[Algebra<br/>liniowa II<br/>5 ECTS]
    AM2[Analiza<br/>matematyczna II<br/>6 ECTS]
    HTML[HTML, CSS,<br/>JavaScript<br/>4 ECTS]
    
    MD --> WAlgo2
    MD --> HTML
    AL2 -.ML.-> ML[Wprowadzenie do<br/>uczenia maszynowego]
    AM2 -.ML.-> ML
    
    style MD fill:#ffcccc
    style AM2 fill:#ffcccc
    style AL2 fill:#ffcccc
    style WAlgo2 fill:#ccccff
    style PC fill:#ccccff
    style HTML fill:#ffffcc
    style ML fill:#ffccff,stroke-dasharray: 5 5
```

**Kluczowe zależności:**
- Rekurencja (MD, S2) wymaga indukcji (WMI, S1) ✅
- Listy i drzewa (WAlgo2, S2) wymagają rekurencji (MD, S2) ✅
- DOM (HTML, S2) wymaga drzew (MD, S2) ✅
- ML (AL2/AM2, S2) wymaga gradientu i macierzy ✅

## Semestr III - Pierwsze specjalizacje (29-31 ECTS)

```mermaid
graph TD
    OOP[Programowanie<br/>obiektowe<br/>6 ECTS]
    Stat[Prawdopodobieństwo<br/>i statystyka<br/>6 ECTS]
    DB[Bazy danych<br/>5 ECTS]
    OS[Systemy<br/>operacyjne<br/>6 ECTS]
    
    subgraph "Wybór 1-2 (6-8 ECTS)"
        PythonAI[Python dla AI<br/>4 ECTS]
        Graphics[Grafika<br/>komputerowa<br/>6 ECTS]
        Network[Sieci<br/>komputerowe<br/>6 ECTS]
    end
    
    OOP -.-> Graphics
    OOP -.-> OS
    Stat -.-> PythonAI
    
    style OOP fill:#ccccff
    style DB fill:#ffffcc
    style OS fill:#ccffcc
    style Stat fill:#ffcccc
    style PythonAI fill:#ffccff
    style Graphics fill:#ffccff
    style Network fill:#ffccff
```

## Ścieżki specjalizacyjne

```mermaid
graph TD
    Base[Semestry I-II<br/>Fundamenty]
    
    Base --> AI[Sztuczna Inteligencja]
    Base --> Gaming[Gaming & Graphics]
    Base --> Net[Networking]
    Base --> Sys[C++/Systems]
    Base --> Web[Web Development]
    Base --> DS[Data Science]
    
    AI --> AI_Courses[Python dla AI<br/>Machine Learning<br/>Deep Learning<br/>Computer Vision<br/>NLP]
    
    Gaming --> Gaming_Courses[Grafika komputerowa<br/>Unity/Unreal<br/>Fizyka w grach<br/>VR/AR]
    
    Net --> Net_Courses[Sieci komputerowe<br/>Cloud Computing<br/>Cybersecurity<br/>Systemy rozproszone]
    
    Sys --> Sys_Courses[Prog. obiektowe C++<br/>Systemy operacyjne<br/>Kompilatory<br/>Embedded]
    
    Web --> Web_Courses[HTML/CSS/JS<br/>React/Angular<br/>Node.js<br/>DevOps]
    
    DS --> DS_Courses[Statystyka<br/>Python dla AI<br/>Big Data<br/>Time Series]
    
    style AI fill:#ff6b6b
    style Gaming fill:#4ecdc4
    style Net fill:#45b7d1
    style Sys fill:#96ceb4
    style Web fill:#ffeaa7
    style DS fill:#dfe6e9
```

## Graf kluczowych zależności

```mermaid
graph TD
    Indukcja[Indukcja<br/>matematyczna<br/>S1]
    Rekurencja[Rekurencja<br/>S2]
    AlgoRek[Algorytmy<br/>rekurencyjne<br/>S2]
    
    Wektory[Wektory<br/>S1]
    Macierze[Macierze<br/>S2]
    ML[Machine<br/>Learning<br/>S3+]
    
    Pochodne[Pochodne<br/>S1]
    Gradient[Gradient<br/>S2]
    Optym[Optymalizacja<br/>S2]
    
    Zbiory[Zbiory<br/>i relacje<br/>S1]
    Grafy[Teoria<br/>grafów<br/>S2]
    AlgoGraf[Algorytmy<br/>grafowe<br/>S3+]
    
    Drzewa[Drzewa<br/>binarne<br/>S2]
    DOM[DOM w<br/>JavaScript<br/>S2]
    
    Indukcja --> Rekurencja
    Rekurencja --> AlgoRek
    Rekurencja --> Drzewa
    
    Wektory --> Macierze
    Macierze --> ML
    Macierze --> Gradient
    
    Pochodne --> Gradient
    Gradient --> Optym
    Optym --> ML
    
    Zbiory --> Grafy
    Grafy --> AlgoGraf
    
    Drzewa --> DOM
    
    style Indukcja fill:#ffe6e6
    style Rekurencja fill:#ffcccc
    style AlgoRek fill:#ffb3b3
    
    style Wektory fill:#e6f3ff
    style Macierze fill:#cce7ff
    style ML fill:#99d6ff
    
    style Pochodne fill:#e6ffe6
    style Gradient fill:#ccffcc
    style Optym fill:#b3ffb3
```

## Motywacja "PO CO?" dla każdej ścieżki

### Sztuczna Inteligencja
**Kluczowe przedmioty podstawowe (S1-S2):**
- Algebra liniowa I & II → reprezentacja danych jako wektory/macierze
- Analiza matematyczna II → gradient descent, trenowanie modeli
- Matematyka dyskretna → złożoność algorytmów ML

**Co to daje?**
Umiejętność budowy systemów AI od rozpoznawania obrazów po chatboty.

### Gaming i Grafika
**Kluczowe przedmioty podstawowe (S1-S2):**
- Algebra liniowa I & II → transformacje 3D, fizyka gier
- Programowanie obiektowe → architektura silników
- Wstęp do algorytmów → struktury danych dla game state

**Co to daje?**
Umiejętność tworzenia gier od małych indie po AAA.

### Networking
**Kluczowe przedmioty podstawowe (S1-S2):**
- Matematyka dyskretna → routing jako problem grafowy
- Unix → administracja serwerami
- Programowanie → implementacja protokołów

**Co to daje?**
Umiejętność budowy infrastruktury internetowej, chmur, systemów rozproszonych.

### C++/Programowanie Systemowe
**Kluczowe przedmioty podstawowe (S1-S2):**
- Wstęp do algorytmów → struktury danych w C
- Projektowy C → duże projekty w C
- Programowanie obiektowe → zaawansowany C++

**Co to daje?**
Umiejętność pisania niskopoziomowego, wydajnego kodu dla systemów krytycznych.

### Web Development
**Kluczowe przedmioty podstawowe (S1-S2):**
- HTML/CSS/JavaScript → frontend
- Bazy danych → backend
- Git/GitHub → workflow

**Co to daje?**
Umiejętność budowy pełnych aplikacji webowych od frontu po deployment.

### Data Science
**Kluczowe przedmioty podstawowe (S1-S2):**
- Prawdopodobieństwo i statystyka → modelowanie niepewności
- Algebra liniowa → operacje na danych
- Python → narzędzia analizy

**Co to daje?**
Umiejętność wyciągania wniosków z danych, predykcji, wizualizacji.

## Harmonogram ECTS

| Semestr | Obowiązkowe | Wybór | Suma |
|---------|-------------|-------|------|
| I       | 31          | 0     | 31   |
| II      | 31          | 0     | 31   |
| III     | 23          | 6-8   | 29-31|
| IV      | 17          | 9-12  | 26-29|
| V       | 0           | 24-28 | 24-28|
| VI      | 0           | 24-28 | 24-28|
| VII     | 15 (praca)  | 10-15 | 25-30|
| **SUMA**| **117-122** | **73-91** | **190-213** |

Minimalnie wymagane: 180 ECTS (licencjat), typowo: 210 ECTS

## Uwagi o zależnościach

### ✅ Poprawne sekwencje
1. **Indukcja (S1) → Rekurencja (S2)**
   - Student najpierw uczy się dowodzenia przez indukcję
   - Potem stosuje to w rekurencji i równaniach rekurencyjnych

2. **Drzewa binarne (S2) → DOM (S2)**
   - W matematyce dyskretnej student poznaje drzewa
   - Potem rozumie DOM jako drzewo w JavaScript

3. **Wektory (S1) → Macierze (S2) → ML (S2-S3)**
   - Geometryczna intuicja wektorów
   - Macierze jako transformacje
   - Wreszcie zastosowanie w uczeniu maszynowym

4. **Pochodne (S1) → Gradient (S2) → Optymalizacja (S2) → ML (S3)**
   - Funkcje 1D i ich pochodne
   - Rozszerzenie na wiele wymiarów (gradient)
   - Metody optymalizacji (gradient descent)
   - Trenowanie modeli ML

### ⚠️ Potencjalne problemy (do rozważenia)

1. **HTML/CSS/JS w semestrze II**
   - PRO: Student ma już podstawy programowania
   - CON: Event loop i DOM wymagają zaawansowanej wiedzy
   - **Sugestia:** Rozważyć przeniesienie do semestru 3 lub 4

2. **Współbieżność Analiza II + Algebra II + Matematyka dyskretna**
   - Trzy ciężkie przedmioty matematyczne w S2
   - **Sugestia:** Upewnić się o grupach gwiazdkowych dla chętnych

## Podsumowanie

Graf zależności zapewnia:
- ✅ Logiczną kolejność nauki (fundamenty → zaawansowane)
- ✅ Transparentność (student wie PO CO się uczy)
- ✅ Połączenie z przyszłą karierą (specjalizacje)
- ✅ Brak frustracji (student ma zawsze odpowiednie podstawy)
- ✅ Łatwość zarządzania programem (walidacja spójności)
