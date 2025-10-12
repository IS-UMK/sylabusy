# Przewodnik Szybkiego Startu - System Grafu Zależności

## Dla studentów

### "Chcę wiedzieć, czego się uczyć aby zostać X"

Gdzie X = AI engineer, web developer, network engineer, etc.

**Krok 1: Zobacz dostępne specjalizacje**
```bash
python3 graf_tools.py specializations
```
Ta komenda wyświetli listę wszystkich dostępnych specjalizacji z ich opisami i kluczowymi konceptami.

**Krok 2: Wygeneruj swoją ścieżkę nauki**
```bash
# Dla AI i Data Science
python3 graf_tools.py path ai_data_science

# Dla Web Development i Sieci
python3 graf_tools.py path web_networking

# Dla Systemów Wbudowanych i Mikroprocesorów
python3 graf_tools.py path embedded_systems

# Dla Inżynierii Oprogramowania
python3 graf_tools.py path software_engineering

# Dla Przetwarzania Sygnałów
python3 graf_tools.py path signal_processing
```

**Krok 3: Zrozum wynik**

Komenda `path` wyświetli szczegółową ścieżkę nauki, pogrupowaną według:
- Semestru (kiedy dany materiał jest zazwyczaj realizowany)
- Przedmiotu (w ramach którego kursu jest nauczany)
- Konceptu (konkretna wiedza lub umiejętność)

Przykład: jeśli widzisz w semestrze 2 "Macierze i operacje na macierzach", oznacza to, że powinieneś zwrócić szczególną uwagę na ten temat w Algebrze liniowej II.

### "Dlaczego muszę się uczyć X?"

Zajrzyj do:
- `README.md` - Sekcja "Ścieżki specjalizacyjne" - tam jest "PO CO?" dla każdej ścieżki
- Syllabus przedmiotu (np. `algebra_liniowa.md`) - sekcja "Połączenie ze specjalizacjami"

### "Co muszę znać PRZED tym przedmiotem?"

Każdy syllabus ma sekcję "Zależności" z listą wymaganych zagadnień.

Przykład z `python_dla_ai.md`:
> **Wymagane wcześniejsze zagadnienia:**
> - Algebra liniowa II (macierze, wektory, transformacje)
> - Analiza matematyczna II (gradient, optymalizacja)
> - Podstawy programowania w Pythonie

## Dla wykładowców

### "Dodaję nowy przedmiot do programu"

1. Otwórz `graf_zaleznosci.json`
2. Dodaj przedmiot do sekcji `"courses"`
3. Zdefiniuj jego pojęcia w sekcji `"concepts"`
4. Określ zależności (`dependencies`)
5. Waliduj:
```bash
python3 graf_tools.py validate
```

### "Chcę zobaczyć wszystkie zależności graficznie"

```bash
# Wygeneruj diagram (50 pierwszych pojęć)
python3 graf_tools.py mermaid 50 > diagram.mmd

# Możesz wkleić zawartość diagram.mmd do:
# https://mermaid.live/
```

### "Sprawdzam czy mój przedmiot nie ma cyklicznych zależności"

```bash
python3 graf_tools.py validate
```

Jeśli jest cykl, dostaniesz błąd:
```
BŁĘDY W GRAFIE:
  - Cycle detected in dependencies: ...
```

## Dla koordynatorów programu

### "Chcę zobaczyć kompletną strukturę programu"

Otwórz `WIZUALIZACJA.md` - tam są diagramy Mermaid pokazujące:
- Strukturę semestrów
- Zależności między przedmiotami
- Ścieżki specjalizacyjne

### "Student pyta: czy mogę wziąć przedmiot X w semestrze Y?"

**Metoda 1: Sprawdź ręcznie w `graf_zaleznosci.json`:**
1. Znajdź przedmiot X w pliku
2. Zobacz jego `dependencies`
3. Sprawdź czy student miał wszystkie wymagane przedmioty przed semestrem Y

**Metoda 2: Użyj narzędzia automatycznego:**
```bash
# Sprawdź optymalną ścieżkę dla specjalizacji studenta
python3 graf_tools.py path <id_specjalizacji>
```
Na przykład:
```bash
python3 graf_tools.py path ai_data_science
```
Komenda ta pokaże optymalną kolejność przedmiotów i konceptów.

### "Chcę dodać nową specjalizację"

**Krok 1:** Otwórz `graf_zaleznosci.json`

**Krok 2:** Dodaj nową specjalizację do sekcji `"specializations"`:
```json
"nowa_specjalizacja": {
  "name": "Nazwa Specjalizacji",
  "description": "Opis czego uczy",
  "key_concepts": ["pojęcie1", "pojęcie2"],
  "recommended_courses": ["Kurs1", "Kurs2"],
  "foundation_courses": ["przedmiot1", "przedmiot2"]
}
```

**Krok 3:** Waliduj zmiany:
```bash
python3 graf_tools.py validate
```

**Krok 4:** Przetestuj nową specjalizację:
```bash
python3 graf_tools.py path nowa_specjalizacja
```

**Krok 5:** Dodaj dokumentację specjalizacji w `README.md` pod sekcją "Ścieżki specjalizacyjne"

**Krok 6:** Zaktualizuj ten przewodnik (`PRZEWODNIK.md`), dodając przykład użycia nowej specjalizacji

## Przykłady użycia

### Student: "Chcę być AI engineerem"

```bash
$ python3 graf_tools.py path ai_data_science

=== ŚCIEŻKA NAUKI: Sztuczna Inteligencja i Data Science ===

# Semestr 1

## Algebra liniowa I
### Wektory w przestrzeniach euklidesowych
### Iloczyn skalarny i geometria wektorów
### Liniowa niezależność i bazy

## Analiza matematyczna I
### Ciągi i granice
### Ciągłość funkcji
### Pochodne funkcji jednej zmiennej
### Ekstrema funkcji jednej zmiennej

## Wstęp do matematyki i informatyki
### Indukcja matematyczna
### Zbiory i operacje na zbiorach
### Relacje i relacje równoważności

# Semestr 2

## Algebra liniowa II
### Macierze i operacje na macierzach

## Algebra liniowa II / warsztaty ML
### Uczenie maszynowe - podstawy (regresja, SVM)

## Analiza matematyczna II
### Gradient i pochodne funkcji wielu zmiennych
### Ekstrema funkcji wielu zmiennych
### Metody optymalizacji (gradient descent)

## Matematyka dyskretna
### Kombinatoryka (wariacje, permutacje)

# Semestr 3

## Bazy danych I
### Podstawy baz danych (SQL, NoSQL)

## Prawdopodobieństwo i statystyka
### Statystyka podstawowa

# Semestr 5

## Sztuczna inteligencja
### Machine Learning - podstawy
### Sieci neuronowe

## Sztuczna inteligencja / Data mining
### Algorytmy klasyfikacji
### Modele regresji

## Wstęp do data mining
### Eksploracja i analiza danych
```

**Interpretacja:** 
- W semestrze 1: Skup się szczególnie na algebrze (wektory!) i analizie (pochodne!) oraz podstawach matematyki i informatyki
- W semestrze 2: Macierze i gradient - to jest klucz do ML! Plus kombinatoryka i pierwsze warsztaty z ML
- W semestrze 3: Bazy danych i statystyka - fundamenty dla Data Science
- W semestrze 5: Główne przedmioty ze sztucznej inteligencji i eksploracji danych

### Student: "Interesuję się tworzeniem aplikacji webowych"

```bash
$ python3 graf_tools.py path web_networking

=== ŚCIEŻKA NAUKI: Web Development i Sieci ===

# Semestr 1
## Wstęp do algorytmów I
### Podstawy programowania (funkcje, programy)

## Wstęp do matematyki i informatyki
### Zbiory i operacje na zbiorach
### Relacje i relacje równoważności

# Semestr 2
## Matematyka dyskretna
### Graf i podstawowe pojęcia teorii grafów
...
```

**Interpretacja:**
- W semestrze 1: Podstawy programowania są fundamentem
- W semestrze 2: Teoria grafów przyda się do zrozumienia routingu i protokołów sieciowych
- W kolejnych semestrach: Koncentruj się na przedmiotach z sieci komputerowych, bazach danych i programowaniu webowym

### Koordynator: "Sprawdzam dostępne specjalizacje dla studenta"

```bash
$ python3 graf_tools.py specializations
```
Komenda wyświetli wszystkie dostępne specjalizacje z ich kluczowymi konceptami i podstawowymi kursami. 
Możesz następnie pokazać studentowi konkretną ścieżkę używając komendy `path`.

### Wykładowca: "Dodam nowe pojęcie do matematyki dyskretnej"

1. Edytuj `graf_zaleznosci.json`
2. Dodaj pojęcie:
```json
"teoria_liczb": {
  "name": "Podstawy teorii liczb",
  "semester": 2,
  "course": "Matematyka dyskretna",
  "dependencies": ["indukcja_matematyczna"],
  "required_for": ["kryptografia"]
}
```
3. Waliduj:
```bash
$ python3 graf_tools.py validate
✓ Graf jest poprawny
```

### Koordynator: "Sprawdzam spójność całego programu"

```bash
$ python3 graf_tools.py validate
✓ Graf jest poprawny (brak cykli, wszystkie zależności zdefiniowane)
```

Jeśli są problemy:
```bash
$ python3 graf_tools.py validate
BŁĘDY W GRAFIE:
  - Concept 'nowe_pojecie' depends on undefined concept 'nieistniejace'
  - Cycle detected in dependencies: pojecie1 -> pojecie2 -> pojecie1
```

## Struktura plików

```
sylabusy/
├── README.md                          # Główny opis programu
├── graf_zaleznosci.json              # Graf zależności (CORE)
├── graf_tools.py                      # Narzędzia zarządzania
├── GRAF_ZALEZNOSCI.md                # Dokumentacja grafu
├── WIZUALIZACJA.md                   # Diagramy wizualne
├── PODSUMOWANIE_REFORMY.md           # Opis reformy
│
├── Syllabi - Semestry I-II (podstawy):
│   ├── wstęp_do_matematyki_i_informatyki.md
│   ├── wstęp_do_systemu_unix.md
│   ├── wstęp_do_programowania.md
│   ├── wstęp_do_algorytmów.md
│   ├── analiza_matematyczna.md
│   ├── algebra_liniowa.md
│   └── matematyka_dyskretna.md
│
└── Syllabi - Semestry III+ (specjalizacje):
    ├── programowanie_obiektowe.md
    ├── prawdopodobienstwo_i_statystyka.md
    ├── bazy_danych.md
    ├── systemy_operacyjne.md
    ├── algorytmy_zaawansowane.md
    ├── python_dla_ai.md
    ├── grafika_komputerowa.md
    └── sieci_komputerowe.md
```

## FAQ

**Q: Graf mówi, że muszę znać X przed Y, ale nie pamiętam X. Co robić?**
A: Zajrzyj do syllabusa przedmiotu, który uczył X. Są tam "Cele edukacyjne" - to powinieneś umieć.

**Q: Jak dodać nowy przedmiot do grafu?**
A: Edytuj `graf_zaleznosci.json`, dodaj do sekcji `courses` i `concepts`, uruchom `graf_tools.py validate`.

**Q: Graf pokazuje, że przedmiot X jest w semestrze 3, ale chcę go wziąć w semestrze 2. Czy mogę?**
A: Sprawdź `dependencies` przedmiotu. Jeśli masz wszystkie wymagane przedmioty z semestru 1, teoretycznie tak. Ale to jest optymalna ścieżka.

**Q: Jak mogę przyczynić się do rozwoju programu?**
A: 
1. Zgłoś issue jeśli widzisz błąd w zależnościach
2. Zaproponuj nową specjalizację
3. Dodaj syllabus dla przedmiotu, którego brakuje
4. Ulepszaj istniejące syllabi (pull requesty mile widziane!)

## Kontakt

Masz pytania? Problemy? Sugestie?
- Otwórz issue na GitHubie
- Skontaktuj się z koordynatorem programu

---

**Powodzenia w nauce! 🚀**
