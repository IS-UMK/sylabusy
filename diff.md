# Analiza zmian w sylabusach — Informatyka Stosowana UMK

> **Dokument porównuje** stare sylabusy kierunku Informatyka Stosowana (obowiązujące do reformy)
> z nowymi propozycjami zawartymi w tym repozytorium.  
> Omówione przedmioty: Algebra liniowa (1 i 2), Analiza matematyczna (1 i 2), Matematyka dyskretna,
> Statystyka (oraz nowy Rachunek prawdopodobieństwa).

---

## Spis treści

1. [Cele reformy](#1-cele-reformy)
2. [Zmiany strukturalne (przekrojowe)](#2-zmiany-strukturalne-przekrojowe)
3. [Algebra liniowa](#3-algebra-liniowa)
4. [Analiza matematyczna](#4-analiza-matematyczna)
5. [Matematyka dyskretna](#5-matematyka-dyskretna)
6. [Statystyka → Rachunek prawdopodobieństwa + Statystyka](#6-statystyka--rachunek-prawdopodobieństwa--statystyka)
7. [Nowe przedmioty bez odpowiednika w starym planie](#7-nowe-przedmioty-bez-odpowiednika-w-starym-planie)
8. [Podsumowanie](#8-podsumowanie)

---

## 1. Cele reformy

Repozytorium explicite formułuje następujące motywacje zmian (patrz `README.md`):

| Cel | Wyjaśnienie |
|-----|-------------|
| **Intuicja przed formalizacją** | Pojęcia matematyczne mają być najpierw zakorzenione w intuicji geometrycznej lub obliczeniowej, a dopiero potem formalizowane. |
| **Połączenie teorii z praktyką AI/ML** | Student od pierwszego semestru widzi, *po co* dana teoria jest potrzebna — np. regresja liniowa, gradient descent, sieci neuronowe. |
| **Kultura współpracy i jakości kodu** | Kod pisany tak, aby czytający wkładał minimalne wysiłki w zrozumienie; nacisk na dobre praktyki (git, testy, code review). |
| **Ścieżki specjalizacyjne** | Po 2 latach wspólnych podstaw student wybiera jedną z kilku ścieżek (AI/Python, gaming, networking, C++, neuronauki). |
| **Grupy gwiazdkowe** | W ramach każdego przedmiotu istnieje co najmniej jedna grupa gwiazdkowa dla zaawansowanych/zainteresowanych studentów. |
| **Ujednolicenie oceniania** | Wspólne kolokwia dla wszystkich grup danego przedmiotu — przejrzystość i sprawiedliwość. |
| **Podniesienie poziomu kształcenia** | Renoma → rekrutacja najlepszych studentów → włączenie ich w badania naukowe. |

---

## 2. Zmiany strukturalne (przekrojowe)

### Rozbicie jednosemestralnych przedmiotów na dwa

| Stary plan | Nowy plan |
|-----------|-----------|
| Algebra liniowa (1 sem., ~45 godz.) | **Algebra liniowa 1** (sem. I) + **Algebra liniowa 2** (sem. II) |
| Analiza matematyczna (1–2 sem.) | **Analiza matematyczna 1** (sem. I) + **Analiza matematyczna 2** (sem. II) |
| Statystyka (z elementami rachunku prawdopodobieństwa) | **Rachunek prawdopodobieństwa** (sem. III) + **Statystyka** (sem. IV) |

**Dlaczego?**  
Rozbicie materiału na dwa semestry pozwala:
- wprowadzać pojęcia stopniowo i z odpowiednią głębią,
- zachować właściwą kolejność zależności między przedmiotami (np. macierze po wektorach, całki wielokrotne po pochodnych jednej zmiennej),
- uniknąć pośpiechu, który w starym planie prowadził do powierzchownego omawiania trudnych zagadnień.

### Nowy przedmiot wprowadzający

Dodano **Wstęp do matematyki i informatyki** (sem. I), który buduje wspólny język formalny (logika, zbiory, relacje, indukcja) niezbędny do rozumienia pozostałych kursów. W starym planie te pojęcia były albo pomijane, albo zakładane jako znane ze szkoły średniej.

### Orientacja na zastosowania w AI/ML

Każdy nowy syllabus matematyczny zawiera:
- sekcję zastosowań w informatyce (uczenie maszynowe, algorytmy optymalizacji, grafika komputerowa),
- jawne powiązania między przedmiotami (np. macierz Jakobiego z Analizy mat. 2 jest używana w Algebrze liniowej 2),
- zadania projektowe lub praktyczne dla grup gwiazdkowych (np. pytorch, regresja liniowa, SVM).

---

## 3. Algebra liniowa

### Stary syllabus (Algebra liniowa, jeden przedmiot)

Typowy zakres kursu algebry liniowej dla informatyki stosowanej przed reformą:

- Grupy, pierścienie, ciała — abstrakcyjne struktury algebraiczne
- Przestrzenie wektorowe — definicja aksjomatyczna, przykłady
- Podprzestrzenie, bazy, wymiar — formalne dowody
- Odwzorowania liniowe — jądro i obraz
- Macierze i działania na macierzach
- Wyznacznik — własności, rozwinięcie Laplace'a
- Układy równań liniowych — metoda Gaussa
- Wartości własne i wektory własne
- Formy kwadratowe i formy dwuliniowe
- Opcjonalnie: przestrzenie euklidesowe (iloczyn skalarny)

**Charakterystyczne cechy starego podejścia:**  
- Nacisk na abstrakcję algebraiczną i aksjomaty  
- Geometria analityczna jako temat poboczny lub nieobecny  
- Brak jawnych zastosowań w informatyce lub ML  
- Jeden ciężki kurs bez podziału na części

### Nowy syllabus

#### Algebra liniowa 1 (semestr I)

Skupiona na **wektorach w przestrzeniach euklidesowych $\mathbb{R}^d$** z naciskiem na intuicję geometryczną:

- Działania na wektorach i interpretacja geometryczna (proste, płaszczyzny, rzutowania)
- Iloczyn skalarny, norma, prostopadłość, rzut ortogonalny, ortogonalizacja Grama–Schmidta
- Liniowa niezależność, bazy, układ współrzędnych
- Wypukłość i afiniczność — zastosowania w optymalizacji i geometrii obliczeniowej
- *Grupa gwiazdkowa:* przestrzeń Hilberta, warunkowa wartość oczekiwana jako rzut ortogonalny, problemy najmniejszych kwadratów

#### Algebra liniowa 2 (semestr II)

Skupiona na **macierzach**:

- Macierz jako reprezentacja przekształcenia liniowego (połączenie z macierzą Jakobiego z Analizy 2)
- Działania na macierzach, eliminacja Gaussa, macierze elementarne
- Wyznacznik — definicja, własności, interpretacja geometryczna (objętość równoległościanu), rząd
- Macierz odwrotna, układy równań liniowych
- Wartości i wektory własne, diagonalizacja
- *Grupa gwiazdkowa:* SVD, tensory, macierze unitarne, programowanie kwantowe, pytorch

### Kluczowe zmiany w Algebrze liniowej

| Aspekt | Stary plan | Nowy plan |
|--------|-----------|-----------|
| Kolejność materiału | Abstrakcja → konkrety | Intuicja geometryczna → formalizm |
| Podział kursu | 1 semestr | 2 semestry (sem. I i II) |
| Struktury abstrakcyjne | Grupy, ciała (na początku) | Pominięte lub w tle |
| Zastosowania w ML | Brak lub marginalne | Jawne (regresja liniowa, SVM, feedforward, SVD) |
| Geometria euklidesowa | Poboczna | Centralny temat Algebry 1 |
| Tensory / pytorch | Nieobecne | Grupa gwiazdkowa w Algebrze 2 |
| Programowanie kwantowe | Nieobecne | Opcjonalnie (grupa gwiazdkowa) |

---

## 4. Analiza matematyczna

### Stary syllabus (Analiza matematyczna, jeden lub dwa semestry)

Typowy zakres:

- Ciągi liczbowe — granica, kryteria zbieżności
- Szeregi liczbowe — kryteria zbieżności (d'Alembert, Cauchy, Leibniz)
- Funkcje jednej zmiennej — granica, ciągłość (definicja Cauchy'ego, Heinego)
- Pochodna — definicja, twierdzenia (Rolle, Lagrange), reguła de l'Hospitala, wzór Taylora
- Całka Riemanna — definicja, Newton-Leibniz, metody całkowania
- Funkcje wielu zmiennych — pochodne cząstkowe, gradient, ekstrema
- Całki wielokrotne
- Szeregi Fouriera (opcjonalnie)
- Pojęcie miary Lebesgue'a (opcjonalnie, dla mocniejszych grup)

**Charakterystyczne cechy starego podejścia:**  
- Nacisk na rygorystyczne dowody (styl klasycznej analizy)  
- Brak połączenia z algorytmiką lub uczeniem maszynowym  
- Metody całkowania jako centralne ćwiczenie (mnóstwo technik)  
- Asymptotyka omawiana osobno lub przy okazji szeregów  
- Funkcje wielu zmiennych często pominięte lub potraktowane pobieżnie z braku czasu

### Nowy syllabus

#### Analiza matematyczna 1 (semestr I)

- Systemy liczbowe $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$
- Ciągi i szeregi liczbowe (granica, punkt skupienia, granice górna/dolna, kryteria zbieżności)
- Notacja asymptotyczna Bachmana-Landaua — **explicite jako narzędzie analizy algorytmów**
- Granica i ciągłość funkcji (Cauchy, Heine, Darboux, Weierstrass)
- Ciągi i szeregi funkcyjne — zbieżność punktowa i jednostajna, szeregi potęgowe
- Pochodna — interpretacja geometryczna i fizyczna, twierdzenia Rolle'a i Lagrange'a, de l'Hospital, wzór Taylora, badanie przebiegu zmienności
- Całka nieoznaczona — metody całkowania
- Całka Riemanna — interpretacja geometryczna, Newton-Leibniz, zastosowania
- *Grupa gwiazdkowa:* Całka Lebesgue'a

#### Analiza matematyczna 2 (semestr II)

- Funkcje wielu zmiennych: granice, ciągłość
- Różniczkowanie: pochodna Frécheta, pochodne kierunkowe, pochodne cząstkowe
- Gradient, rozwinięcie Taylora, ekstrema, hesjan
- Funkcje wypukłe — rola w optymalizacji
- Ekstrema warunkowe — metoda mnożników Lagrange'a
- **Połączenie z ML:** metoda najmniejszych kwadratów, gradient descent, oszacowania błędów
- *Grupa gwiazdkowa:* macierz Jakobiego (połączenie z Algebrą 2), całki wielokrotne i krzywoliniowe, twierdzenia Greena/Gaussa-Ostrogradskiego/Stokesa

### Kluczowe zmiany w Analizie matematycznej

| Aspekt | Stary plan | Nowy plan |
|--------|-----------|-----------|
| Podział kursu | 1–2 semestry, mniej ustrukturyzowane | Wyraźny podział: jednej zmiennej (sem. I) / wielu zmiennych (sem. II) |
| Notacja asymptotyczna | Brak lub przy szeregach | Explicite — jako narzędzie informatyczne |
| Funkcje wielu zmiennych | Często pominięte lub pobieżne | Pełny odrębny semestr (Analiza 2) |
| Całki wielokrotne | Opcjonalne | Grupa gwiazdkowa w Analizie 2 |
| Gradient descent / ML | Nieobecne | Explicite jako zastosowanie w Analizie 2 |
| Ciągłość jednostajna | Marginalnie | Omawiana explicite |
| Całka Lebesgue'a | Nieobecna | Grupa gwiazdkowa w Analizie 1 |
| Szeregi Fouriera | Opcjonalnie | Opcjonalnie (*) w Analizie 1 |

---

## 5. Matematyka dyskretna

### Stary syllabus

Typowy zakres kursu matematyki dyskretnej dla informatyki stosowanej:

- Logika matematyczna (rachunek zdań, kwantyfikatory)
- Teoria zbiorów i relacje (często traktowane jako wstęp)
- Indukcja matematyczna
- Kombinatoryka — permutacje, wariacje, kombinacje
- Teoria liczb — podzielność, NWD, NWW, kongruencje
- Grafy — pojęcia podstawowe, drogi, cykle, drzewa
- Algorytmy grafowe (DFS, BFS, drzewo rozpinające)
- Kolorowanie grafów, problem Eulera i Hamiltona
- Rekurencja i równania rekurencyjne
- Elementy kryptografii (RSA) lub automatów skończonych (opcjonalnie)

**Charakterystyczne cechy starego podejścia:**  
- Szeroki, encyklopedyczny zakres (logika + teoria zbiorów + grafy + kombinatoryka + teoria liczb)  
- Logika i teoria zbiorów jako odrębny blok (tematycznie nakładający się z innymi kursami)  
- Złożoność obliczeniowa traktowana marginalnie lub nieobecna  
- Brak wyraźnego połączenia z algorytmiką i strukturami danych  

### Nowy syllabus (`matematyka_dyskretna.md` + `usos.md`)

- **Rekurencja** — definicja rekurencyjna problemów, równania rekurencyjne, dowody poprawności
- **Kombinatoryka** — permutacje, wariacje, kombinacje, zasada włączeń i wyłączeń, szufladkowa Dirichleta
- **Asymptotyka i złożoność** — notacja O/Ω/Θ, Master Theorem (twierdzenie o rekursji universalnej) — **centralne dla algorytmiki**
- **Drzewa binarne** — struktura, operacje, obchodzenia (preorder, inorder, postorder), zastosowania w rekurencji
- **Teoria grafów** — pojęcia podstawowe, problem Eulera i Hamiltona, kolorowanie
- Przedmiot jest **kontynuacją Wstępu do matematyki i informatyki** (logika i zbiory przeniesione tam)

### Kluczowe zmiany w Matematyce dyskretnej

| Aspekt | Stary plan | Nowy plan |
|--------|-----------|-----------|
| Logika i zbiory | Wstęp do kursu | Przeniesione do *Wstępu do matematyki i informatyki* (sem. I) |
| Teoria liczb | Podzielność, NWD, NWW, kongruencje | Usunięta (lub jako temat facultatif) |
| Złożoność obliczeniowa | Marginalna | **Centralna** — Master Theorem explicite |
| Rekurencja | Jeden temat z wielu | **Centralna** — fundament kursu |
| Struktury danych | Nieobecne | Drzewa binarne jako zastosowanie rekurencji |
| Automaty/kryptografia | Opcjonalnie | Usunięte (przenoszone do innych kursów lub specjalizacji) |
| Powiązanie z Algorytmiką | Słabe | Ścisłe — kurs przygotowuje bezpośrednio do Wstępu do algorytmów II |

---

## 6. Statystyka → Rachunek prawdopodobieństwa + Statystyka

### Stary syllabus (Statystyka, jeden przedmiot)

Typowy zakres:

- Podstawy rachunku prawdopodobieństwa (zdarzenia, prawdopodobieństwo klasyczne)
- Zmienne losowe — rozkłady dyskretne i ciągłe
- Najważniejsze rozkłady: dwumianowy, Poissona, normalny, wykładniczy
- Wartość oczekiwana, wariancja, kowariancja
- Centralne Twierdzenie Graniczne (CTG)
- Statystyka opisowa — miary tendencji centralnej i rozproszenia
- Estymacja punktowa i przedziałowa
- Testowanie hipotez (t-Student, z)
- Regresja liniowa (często pobieżnie)

**Charakterystyczne cechy starego podejścia:**  
- Rachunek prawdopodobieństwa i statystyka zmieszane w jednym kursie  
- Brak formalnych podstaw miary (σ-ciała, miara Lebesgue'a)  
- Nacisk na obliczenia (ćwiczenia rachunkowe) kosztem zrozumienia  
- Brak połączenia z ML (np. bias-variance tradeoff, overfitting, ocena modeli)

### Nowy syllabus

#### Rachunek prawdopodobieństwa (semestr III)

**Nowość:** Formalne podstawy teorii miary jako fundament probabilistyki:

- Podstawy teorii miary — σ-ciała, miara i przestrzeń mierzalna
- Przestrzeń probabilistyczna, aksjomaty Kołmogorowa
- Prawdopodobieństwo warunkowe, wzór Bayesa — **zastosowanie: klasyfikator bayesowski**
- Zmienne losowe — definicja przez funkcję mierzalną, rozkłady, dystrybuanta, gęstość
- Podstawowe rozkłady: dwumianowy, Poissona, jednostajny, wykładniczy, normalny
- Charakterystyki liczbowe: wartość oczekiwana, wariancja, momenty, kowariancja, korelacja
- *Grupa gwiazdkowa:* CTG, prawo wielkich liczb, procesy stochastyczne, wektory losowe

#### Statystyka (semestr IV)

- Statystyka opisowa — skale pomiarowe, miary tendencji centralnej i rozproszenia, wizualizacja
- Wnioskowanie statystyczne — próba losowa i populacja
- Estymacja punktowa i przedziałowa
- Testowanie hipotez — hipoteza zerowa/alternatywna, p-wartość, moc testu
- Test t-Studenta i test z
- **Zastosowania w informatyce:** ocena jakości modeli ML, porównywanie eksperymentów
- *Grupa gwiazdkowa:* regresja liniowa, overfitting, kompromis bias–variance

### Kluczowe zmiany w Statystyce / Rachunku prawdopodobieństwa

| Aspekt | Stary plan | Nowy plan |
|--------|-----------|-----------|
| Podział | 1 kurs (prawdopodobieństwo + statystyka) | 2 odrębne kursy (sem. III i IV) |
| Formalne podstawy | Brak (prawdopodobieństwo klasyczne) | σ-ciała, miara — formalna teoria miary |
| Twierdzenie Bayesa | Wzór bez kontekstu | Explicite z zastosowaniem (klasyfikator bayesowski) |
| CTG i prawo wielkich liczb | Często pomijane lub bez dowodu | Grupa gwiazdkowa (sem. III) |
| Procesy stochastyczne | Nieobecne | Wprowadzenie (grupa gwiazdkowa) |
| Regresja liniowa | Pobieżnie | Grupa gwiazdkowa w Statystyce (sem. IV) |
| Połączenie z ML | Brak | Explicite — ocena modeli, overfitting, bias-variance |
| Wizualizacja danych | Marginalnie | Wyraźnie w programie (histogramy, boxplot, scatter) |

---

## 7. Nowe przedmioty bez odpowiednika w starym planie

### Wstęp do matematyki i informatyki (semestr I)

Przenosi z Matematyki dyskretnej i kursów matematycznych treści, które były albo zakładane jako znane, albo omawiane ad hoc:

- Indukcja matematyczna
- Logika (rachunek zdań, kwantyfikatory)
- Funkcje i ich własności (injektywność, surjektywność, bijektywność)
- Teoria zbiorów (operacje, moc zbioru)
- Relacje równoważności i porządki

**Motywacja:** student od pierwszego dnia rozumie precyzyjny język matematyki i informatyki, co eliminuje nieporozumienia terminologiczne w kolejnych kursach.

### Wstęp do algorytmów I i II (semestry I i II)

Nie ma bezpośredniego odpowiednika jako *osobnego* przedmiotu — algorytmika była wcześniej wtopiona w kursy programowania lub matematyki dyskretnej. Teraz:

- **Algorytmy I** (sem. I, język C): podstawy algorytmiki, tablice, niezmienniki pętli
- **Algorytmy II** (sem. II, C lub C++): listy, drzewa binarne, rekurencja → korzysta z Matematyki dyskretnej

### Wstęp do programowania (semestr I)

Nacisk na *jak pisać kod*, nie tylko *jak go uruchomić*:
- Środowisko pracy (git, GitHub, IDE)
- Dobre praktyki programowania
- Testowanie i code review
- AI-assisted development (generowanie kodu, lintery, formattery)
- CI/CD w zarysie

### Wstęp do systemu Unix (semestr I)

Kurs systematycznego opanowania środowiska Unix — terminala, komend, skryptów powłoki. Uzasadnienie: student potrzebuje sprawnie poruszać się w środowisku, aby efektywnie realizować projekty w kolejnych semestrach.

---

## 8. Podsumowanie

### Tabela porównawcza — najważniejsze zmiany

| Kategoria | Stary plan | Nowy plan |
|-----------|-----------|-----------|
| **Liczba kursów mat.** | ~4 (Algebra, Analiza, Mat. dyskretna, Statystyka) | ~8 (każdy rozbity lub nowy) |
| **Orientacja** | Matematyczna, abstrakcyjna | Matematyczno-informatyczna, zorientowana na ML/AI |
| **Intuicja geometryczna** | Drugorzędna | Priorytetowa (szczególnie w Algebrze 1) |
| **Zastosowania w ML** | Nieobecne lub marginalnie | Explicite w każdym kursie mat. |
| **Formalne podstawy prob.** | Brak | Teoria miary (σ-ciała) |
| **Grupy zaawansowane** | Brak lub niesystematyczne | Grupy gwiazdkowe w każdym kursie |
| **Zależności między kursami** | Słabo zarządzane | Graf zależności explicite (patrz `graf_zaleznosci.json`) |
| **Asymptotyka algorytmów** | Marginalnie (Algorytmika) | W Analizie 1, Mat. dyskretnej i Algorytmice |
| **Język formalny** | Zakładany jako znany | Kurs wstępny (Wstęp do mat. i inf.) |
| **Programowanie praktyczne** | Jeden kurs programowania | Wstęp do prog. + Algorytmy I/II + Unix |

### Główne powody reformy

1. **Dostosowanie do AI/ML**: algorytmy uczenia maszynowego wymagają konkretnych narzędzi matematycznych (gradient, macierze, regresja, probabilistyka) — nowy program buduje do nich drogę explicite.

2. **Spójność programowa**: dzięki grafowi zależności każde pojęcie jest omawiane w odpowiednim momencie, a student nie napotyka zagadnień, do których nie ma jeszcze podstaw.

3. **Jakość vs. zakres**: zamiast pobieżnie omawiać wiele tematów, nowy plan skupia się na głębokim zrozumieniu mniejszego, starannie dobranego zakresu.

4. **Motywacja studentów**: jawne ścieżki specjalizacyjne i ciągłe wskazywanie zastosowań sprawiają, że student od początku rozumie *po co* uczy się danego materiału.

5. **Nowoczesne narzędzia**: AI w programowaniu (generowanie kodu, lintery AI), git, github, CI/CD — zintegrowane od pierwszego semestru.

6. **Równe szanse**: ujednolicone kolokwia i projekty dla wszystkich grup (poza gwiazdkowymi) zwiększają sprawiedliwość oceniania.
