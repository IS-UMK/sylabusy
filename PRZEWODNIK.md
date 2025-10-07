# Przewodnik Szybkiego Startu - System Grafu Zależności

## Dla studentów

### "Chcę wiedzieć, czego się uczyć aby zostać X"

Gdzie X = AI engineer, game developer, network engineer, etc.

```bash
# Zobacz dostępne specjalizacje
python3 graf_tools.py specializations

# Wygeneruj swoją ścieżkę nauki
python3 graf_tools.py path ai              # Dla AI
python3 graf_tools.py path gaming          # Dla Gaming
python3 graf_tools.py path networking      # Dla Networking
python3 graf_tools.py path cpp_systems     # Dla C++/Systems
python3 graf_tools.py path web_development # Dla Web Dev
python3 graf_tools.py path data_science    # Dla Data Science
```

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

Sprawdź `graf_zaleznosci.json`:
1. Znajdź przedmiot X
2. Zobacz jego `dependencies`
3. Sprawdź czy student miał wszystkie wymagane przedmioty przed semestrem Y

Automatycznie:
```bash
python3 graf_tools.py path <specjalizacja>
# Pokaże optymalną kolejność
```

### "Chcę dodać nową specjalizację"

1. Otwórz `graf_zaleznosci.json`
2. Dodaj do sekcji `"specializations"`:
```json
"nowa_specjalizacja": {
  "name": "Nazwa Specjalizacji",
  "description": "Opis czego uczy",
  "key_concepts": ["pojęcie1", "pojęcie2"],
  "recommended_courses": ["Kurs1", "Kurs2"],
  "foundation_courses": ["przedmiot1", "przedmiot2"]
}
```
3. Dodaj sekcję w README.md pod "Ścieżki specjalizacyjne"

## Przykłady użycia

### Student: "Chcę być AI engineerem"

```bash
$ python3 graf_tools.py path ai

=== ŚCIEŻKA NAUKI: Sztuczna Inteligencja ===

--- Semestr 1 ---
  Wektory w przestrzeniach euklidesowych (Algebra liniowa I)
  Iloczyn skalarny i geometria wektorów (Algebra liniowa I)
  Liniowa niezależność i bazy (Algebra liniowa I)
  Pochodne funkcji jednej zmiennej (Analiza matematyczna I)
  
--- Semestr 2 ---
  Macierze i operacje na macierzach (Algebra liniowa II)
  Gradient i pochodne funkcji wielu zmiennych (Analiza matematyczna II)
  Metody optymalizacji (gradient descent) (Analiza matematyczna II)
  Uczenie maszynowe - podstawy (Algebra liniowa II / warsztaty ML)
```

**Interpretacja:** 
- W semestrze 1: Skup się szczególnie na algebrze (wektory!) i analizie (pochodne!)
- W semestrze 2: Macierze i gradient - to jest klucz do ML!
- W semestrze 3+: Możesz już brać Python dla AI, Machine Learning, etc.

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
