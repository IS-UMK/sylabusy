# Graf Zależności - Dokumentacja

Ten plik zawiera dokumentację systemu grafu zależności dla programu Informatyki Stosowanej.

## Struktura grafu

Graf zależności jest zapisany w pliku `graf_zaleznosci.json` w formacie JSON. Składa się z następujących sekcji:

### 1. Concepts (Pojęcia)

Każde pojęcie to pojedyncze zagadnienie naucza na w ramach przedmiotu. Struktura:

```json
{
  "concept_id": {
    "name": "Nazwa pojęcia po polsku",
    "semester": 1,
    "course": "Nazwa przedmiotu",
    "dependencies": ["lista", "wymaganych", "pojęć"],
    "required_for": ["lista", "pojęć", "wymagających", "tego"]
  }
}
```

**Zasady:**
- `dependencies` - pojęcia, które MUSZĄ być poznane PRZED tym pojęciem
- `required_for` - pojęcia, do których to pojęcie jest WYMAGANE (informacyjne)
- Semester wskazuje najwcześniejszy semestr, w którym pojęcie może być nauczone

### 2. Courses (Przedmioty)

Przedmioty grupują pojęcia i mają własne zależności:

```json
{
  "course_id": {
    "name": "Nazwa przedmiotu",
    "semester": 1,
    "ects": 6,
    "type": "obowiązkowy",
    "concepts": ["lista", "pojęć"],
    "dependencies": ["lista", "wymaganych", "przedmiotów"],
    "required_for": ["lista", "przedmiotów", "wymagających"]
  }
}
```

### 3. Specializations (Specjalizacje)

Ścieżki specjalizacyjne definiują kluczowe pojęcia i kursy:

```json
{
  "specialization_id": {
    "name": "Nazwa specjalizacji",
    "description": "Opis",
    "key_concepts": ["kluczowe", "pojęcia"],
    "recommended_courses": ["polecane", "kursy"],
    "foundation_courses": ["podstawowe", "kursy"]
  }
}
```

## Narzędzia

Skrypt `graf_tools.py` pozwala na:

### Walidacja grafu

```bash
python3 graf_tools.py validate
```

Sprawdza:
- Czy wszystkie zależności istnieją
- Czy nie ma cykli w grafie
- Czy graf jest spójny

### Generowanie diagramu Mermaid

```bash
python3 graf_tools.py mermaid 30 > diagram.mmd
```

Generuje diagram w formacie Mermaid (max 30 pojęć dla czytelności).

### Wyświetlanie specjalizacji

```bash
python3 graf_tools.py specializations
```

Pokazuje wszystkie dostępne specjalizacje z kluczowymi pojęciami.

### Generowanie ścieżki nauki

```bash
python3 graf_tools.py path ai
```

Generuje zalecaną ścieżkę nauki dla specjalizacji (np. `ai`, `gaming`, `networking`).

## Przykład: Kluczowe zależności

```
Indukcja matematyczna (S1) 
    → Rekurencja (S2) 
        → Algorytmy rekurencyjne (S2)
        → Struktury rekurencyjne (S2)

Wektory (S1) 
    → Macierze (S2) 
        → Uczenie maszynowe (S2+)

Pochodne (S1) 
    → Gradient (S2) 
        → Optymalizacja (S2) 
            → ML/AI (S3+)

Zbiory i relacje (S1) 
    → Teoria grafów (S2) 
        → Algorytmy grafowe (S3+)
        → Sieci komputerowe (S3+)

Drzewa binarne (S2) 
    → DOM w JavaScript (S2)
```

## Zasady zarządzania grafem

1. **Dodawanie nowego pojęcia:**
   - Zdefiniuj wszystkie wymagane zależności
   - Upewnij się, że semestr jest >= najwyższego semestru zależności
   - Dodaj do odpowiedniego kursu
   - Uruchom `graf_tools.py validate`

2. **Dodawanie nowego kursu:**
   - Zdefiniuj wszystkie pojęcia kursu
   - Określ zależności od innych kursów
   - Upewnij się, że semestr respektuje zależności
   - Dodaj do README.md w sekcji odpowiedniego semestru

3. **Dodawanie specjalizacji:**
   - Zdefiniuj kluczowe pojęcia (cel ścieżki)
   - Wskaż podstawowe kursy (semestry 1-4)
   - Dodaj opis "PO CO" w README.md
   - Dodaj polecane kursy specjalizacyjne (semestry 5-7)

## Wizualizacja - przykładowy fragment grafu

```mermaid
graph TD
    indukcja[Indukcja matematyczna<br/>(sem 1)]
    rekurencja[Rekurencja<br/>(sem 2)]
    algo_rek[Algorytmy rekurencyjne<br/>(sem 2)]
    
    wektory[Wektory<br/>(sem 1)]
    macierze[Macierze<br/>(sem 2)]
    ml[Uczenie maszynowe<br/>(sem 2+)]
    
    pochodne[Pochodne<br/>(sem 1)]
    gradient[Gradient<br/>(sem 2)]
    optym[Optymalizacja<br/>(sem 2)]
    
    indukcja --> rekurencja
    rekurencja --> algo_rek
    
    wektory --> macierze
    macierze --> ml
    
    pochodne --> gradient
    gradient --> optym
    optym --> ml
```

## Motywacja: PO CO ten graf?

Graf zależności rozwiązuje kluczowe problemy w edukacji:

1. **Unikanie frustracji studenta** - student nie uczy się zagadnień, których nie może zrozumieć (brak podstaw)

2. **Transparentność** - każdy widzi DLACZEGO uczy się danego zagadnienia i JAK łączy się z przyszłą specjalizacją

3. **Optymalna kolejność** - zagadnienia są wprowadzane we właściwej kolejności (indukcja przed rekurencją!)

4. **Świadome wybory** - student od semestru 1 wie, które przedmioty prowadzą do jego wymarzonej specjalizacji

5. **Łatwa ewolucja programu** - można dodawać/modyfikować kursy z zachowaniem spójności

## Przykład użycia: Ścieżka do AI

Student zainteresowany AI może użyć:

```bash
python3 graf_tools.py path ai
```

I zobaczy DOKŁADNIE które pojęcia i w jakiej kolejności musi opanować, aby osiągnąć cel.

## Rozwój grafu

Graf jest żywym dokumentem. Każdy kurs dodany do programu powinien:
1. Być dodany do `graf_zaleznosci.json`
2. Mieć zdefiniowane zależności
3. Przejść walidację (`graf_tools.py validate`)
4. Być połączony z odpowiednimi specjalizacjami

Dzięki temu program studiów pozostaje spójny i logiczny w miarę rozwoju.
