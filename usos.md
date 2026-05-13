# Opisy przedmiotów matematycznych — format USOS

Opisy przygotowane z perspektywy kierunku **Informatyka Stosowana** na Wydziale Fizyki, Astronomii i
Informatyki Stosowanej UMK.  Zgodne z wymogami formalnymi USOS (efekty uczenia się, pełny opis).
Nacisk na **CO** student powinien wiedzieć/umieć, a nie JAK to osiągnąć.

---

## Spis treści

1. [Wstęp do matematyki i informatyki](#1-wstęp-do-matematyki-i-informatyki)
2. [Algebra liniowa 1](#2-algebra-liniowa-1)
3. [Algebra liniowa 2](#3-algebra-liniowa-2)
4. [Analiza matematyczna 1](#4-analiza-matematyczna-1)
5. [Analiza matematyczna 2](#5-analiza-matematyczna-2)
6. [Matematyka dyskretna](#6-matematyka-dyskretna)
7. [Rachunek prawdopodobieństwa](#7-rachunek-prawdopodobieństwa)
8. [Statystyka](#8-statystyka)

---

## 1. Wstęp do matematyki i informatyki

**Kod przedmiotu:** 0800-WDMII *(do uzgodnienia)*
**Kierunek:** Informatyka Stosowana
**Semestr:** I
**Forma zajęć:** wykład + ćwiczenia

### Efekty uczenia się — wiedza

Efekty przedmiotowe W1–W6 realizują efekty kierunkowe: **K_W01**

| Symbol | Opis efektu |
|--------|-------------|
| W1 | Zna zasadę indukcji matematycznej i jej związek z pojęciem zbioru dobrze uporządkowanego. |
| W2 | Zna rachunek zdań, podstawowe operatory logiczne (koniunkcja, alternatywa, negacja, implikacja) oraz kwantyfikatory ogólny i szczegółowy. |
| W3 | Zna pojęcie funkcji, w tym pojęcia surjekcji, injekcji, bijekcji, oraz złożenia funkcji. |
| W4 | Zna pojęcie zbioru, podstawowe operacje na zbiorach oraz pojęcia mocy zbioru (zbiory skończone, przeliczalne, nieprzeliczalne). |
| W5 | Zna pojęcie relacji, w szczególności relacji równoważności i konstrukcji ilorazowych. |
| W6 | Zna pojęcie porządku częściowego i liniowego oraz zbioru dobrze uporządkowanego. |

### Efekty uczenia się — umiejętności

Efekty przedmiotowe U1–U6 realizują efekty kierunkowe: **K_U01, K_U02**

| Symbol | Opis efektu |
|--------|-------------|
| U1 | Potrafi przeprowadzić dowód przez indukcję matematyczną. |
| U2 | Potrafi formalizować zdania języka naturalnego za pomocą rachunku zdań i kwantyfikatorów. |
| U3 | Potrafi określić własności funkcji (injektywność, surjektywność, bijektywność) i stosować złożenia funkcji. |
| U4 | Potrafi wykonywać operacje na zbiorach oraz rozstrzygać o mocy zbiorów. |
| U5 | Potrafi identyfikować relacje równoważności i konstruować zbiory ilorazowe. |
| U6 | Potrafi rozpoznawać i klasyfikować porządki oraz stosować pojęcie dobrego uporządkowania. |

### Efekty uczenia się — kompetencje społeczne

Efekty przedmiotowe K1–K2 realizują efekty kierunkowe: **K_K02, K_K04, K_K06**

| Symbol | Opis efektu |
|--------|-------------|
| K1 | Rozumie rolę precyzyjnego języka formalnego jako wspólnego narzędzia komunikacji informatyków i matematyków. |
| K2 | Jest świadomy konieczności ścisłego formułowania twierdzeń i definicji w pracy informatyka. |

### Pełny opis

Przedmiot stanowi fundament kształcenia matematycznego na kierunku informatyka stosowana. Wprowadza pojęcia i język formalny wspólny dla matematyki i informatyki, stanowiący podstawę dalszych przedmiotów kierunkowych.

Program obejmuje następujące zagadnienia:

1. **Indukcja matematyczna** — zasada indukcji jako podstawowa metoda dowodowa w matematyce i informatyce; związek indukcji z pojęciem zbioru dobrze uporządkowanego.

2. **Logika** — rachunek zdań: koniunkcja, alternatywa, negacja, implikacja, równoważność; tautologie i prawa logiczne; kwantyfikatory ogólny i szczegółowy; opcjonalnie elementy rachunku predykatów. Zastosowania logiki w specyfikacji i weryfikacji programów.

3. **Funkcje** — pojęcie funkcji i jej własności: injektywność, surjektywność, bijektywność; złożenie funkcji; funkcja odwrotna.

4. **Zbiory** — operacje na zbiorach (suma, iloczyn, różnica, dopełnienie); zbiory potęgowe; liczebność zbioru — zbiory skończone, przeliczalne i nieprzeliczalne; twierdzenie Cantora.

5. **Relacje** — relacje binarne i ich własności; relacje równoważności; klasy abstrakcji i konstrukcje ilorazowe.

6. **Porządki** — porządek częściowy i liniowy; elementy minimalne, maksymalne, kresy; zbiory dobrze uporządkowane i ich związek z indukcją.

---

## 2. Algebra liniowa 1

**Kod przedmiotu:** 0800-ALGEB1
**Kierunek:** Informatyka Stosowana
**Semestr:** I
**Forma zajęć:** wykład + ćwiczenia

### Efekty uczenia się — wiedza

Efekty przedmiotowe W1–W6 realizują efekty kierunkowe: **K_W01**

| Symbol | Opis efektu |
|--------|-------------|
| W1 | Zna pojęcie wektora w przestrzeni euklidesowej $\mathbb{R}^d$ oraz podstawowe działania na wektorach (dodawanie, mnożenie przez skalar). |
| W2 | Zna pojęcie iloczynu skalarnego, normy wektora, prostopadłości oraz rzutu ortogonalnego. |
| W3 | Zna pojęcie liniowej niezależności wektorów, bazy i układu współrzędnych. |
| W4 | Zna geometryczną interpretację wektorów, prostych i płaszczyzn w $\mathbb{R}^2$ i $\mathbb{R}^3$. |
| W5 | Zna pojęcie zbioru wypukłego i kombinacji wypukłej wektorów. |
| W6 | Zna zastosowania rachunku wektorowego w kontekście informatyki, w tym reprezentacji danych i geometrii obliczeniowej. |

### Efekty uczenia się — umiejętności

Efekty przedmiotowe U1–U5 realizują efekty kierunkowe: **K_U01, K_U02**

| Symbol | Opis efektu |
|--------|-------------|
| U1 | Potrafi wykonywać działania na wektorach w przestrzeni $\mathbb{R}^d$ oraz interpretować je geometrycznie. |
| U2 | Potrafi obliczać iloczyn skalarny i wykorzystywać go do wyznaczania kątów, prostopadłości i rzutów. |
| U3 | Potrafi badać liniową niezależność wektorów i wyznaczać bazy podprzestrzeni. |
| U4 | Potrafi wyznaczać równania prostych i płaszczyzn w $\mathbb{R}^2$ i $\mathbb{R}^3$. |
| U5 | Potrafi stosować pojęcia wypukłości do analizy zbiorów punktów. |

### Efekty uczenia się — kompetencje społeczne

Efekty przedmiotowe K1–K2 realizują efekty kierunkowe: **K_K01, K_K06**

| Symbol | Opis efektu |
|--------|-------------|
| K1 | Rozumie znaczenie intuicji geometrycznej w rozwiązywaniu problemów informatycznych i matematycznych. |
| K2 | Docenia rolę algebry liniowej jako narzędzia modelowania w informatyce, w tym w uczeniu maszynowym i grafice komputerowej. |

### Pełny opis

Przedmiot wprowadza studenta w rachunek wektorowy w przestrzeniach euklidesowych. Nacisk położony jest na budowanie intuicji geometrycznej, która stanowi fundament rozumienia algorytmów uczenia maszynowego, grafiki komputerowej i analizy danych.

Program obejmuje następujące zagadnienia:

1. **Wektory w przestrzeniach euklidesowych $\mathbb{R}^d$** — definicja wektora; dodawanie wektorów i mnożenie przez skalar; interpretacja geometryczna w $\mathbb{R}^2$ i $\mathbb{R}^3$; proste, płaszczyzny i rzutowania jako zastosowania rachunku wektorowego.

2. **Iloczyn skalarny i prostopadłość** — definicja i własności iloczynu skalarnego; norma wektora; kąt między wektorami; prostopadłość; rzut ortogonalny wektora na wektor i na podprzestrzeń; ortogonalizacja Gramma–Schmidta.

3. **Liniowa niezależność, bazy, układ współrzędnych** — pojęcie liniowej kombinacji i liniowej niezależności; podprzestrzenie generowane; baza i wymiar; układ współrzędnych; bazy i układy ortonormalne.

4. **Wypukłość i afiniczność** — zbiory wypukłe; kombinacje wypukłe; otoczka wypukła; podprzestrzenie afiniczne i kombinacje afiniczne; zastosowania w optymalizacji i geometrii obliczeniowej.

5. **Tematy rozszerzone (grupa gwiazdkowa)** — praktyczne przykłady w przestrzeni Hilberta z naciskiem na przestrzeń $L^2$; warunkowa wartość oczekiwana jako rzut ortogonalny w $L^2$; związek z rachunkiem prawdopodobieństwa i statystyką; interpretacja rzutów ortogonalnych jako rozwiązań problemów najmniejszych kwadratów.

---

## 3. Algebra liniowa 2

**Kod przedmiotu:** 0800-ALGEB2 *(do uzgodnienia)*
**Kierunek:** Informatyka Stosowana
**Semestr:** II
**Forma zajęć:** wykład + ćwiczenia

### Efekty uczenia się — wiedza

Efekty przedmiotowe W1–W7 realizują efekty kierunkowe: **K_W01**

| Symbol | Opis efektu |
|--------|-------------|
| W1 | Zna pojęcie macierzy, w tym macierzy jako reprezentacji przekształcenia liniowego. |
| W2 | Zna podstawowe działania na macierzach (dodawanie, mnożenie, transpozycja) oraz ich interpretację. |
| W3 | Zna metodę eliminacji Gaussa i jej zastosowanie do rozwiązywania układów równań liniowych. |
| W4 | Zna pojęcie wyznacznika macierzy, jego własności i interpretację geometryczną (objętość równoległościanu). |
| W5 | Zna pojęcie rzędu macierzy i macierzy odwrotnej oraz warunki jej istnienia. |
| W6 | Zna pojęcie wartości własnych i wektorów własnych macierzy oraz ich interpretację geometryczną. |
| W7 | Zna zastosowania rachunku macierzowego w kontekście informatyki, w szczególności w uczeniu maszynowym. |

### Efekty uczenia się — umiejętności

Efekty przedmiotowe U1–U7 realizują efekty kierunkowe: **K_U01, K_U02, K_U08**

| Symbol | Opis efektu |
|--------|-------------|
| U1 | Potrafi wykonywać działania na macierzach i interpretować macierz jako przekształcenie liniowe. |
| U2 | Potrafi stosować eliminację Gaussa do rozwiązywania układów równań liniowych i obliczania rzędu macierzy. |
| U3 | Potrafi obliczać wyznacznik macierzy i stosować go do badania odwracalności macierzy. |
| U4 | Potrafi wyznaczać macierz odwrotną. |
| U5 | Potrafi rozwiązywać układy równań liniowych i dyskutować istnienie oraz jednoznaczność rozwiązań. |
| U6 | Potrafi wyznaczać wartości własne i wektory własne macierzy oraz przeprowadzać diagonalizację. |
| U7 | Potrafi wskazać zastosowania rachunku macierzowego w modelach informatycznych (np. sieci neuronowe typu feedforward, transformacje w grafice komputerowej). |

### Efekty uczenia się — kompetencje społeczne

Efekty przedmiotowe K1–K2 realizują efekty kierunkowe: **K_K01, K_K06**

| Symbol | Opis efektu |
|--------|-------------|
| K1 | Rozumie rolę algebry liniowej jako fundamentalnego narzędzia obliczeniowego we współczesnej informatyce. |
| K2 | Jest świadomy związku między abstrakcyjnymi pojęciami algebry liniowej a ich konkretnymi zastosowaniami w algorytmach i modelach obliczeniowych. |

### Pełny opis

Przedmiot stanowi kontynuację Algebry liniowej 1 i koncentruje się na rachunku macierzowym. Macierze są przedstawiane zarówno jako obiekty algebraiczne, jak i jako reprezentacje przekształceń liniowych, co buduje most między algebrą a jej zastosowaniami w informatyce — od uczenia maszynowego (model feedforward, macierze wag) po grafikę komputerową (transformacje afiniczne).

Program obejmuje następujące zagadnienia:

1. **Macierze i przekształcenia liniowe** — pojęcie macierzy; macierz jako reprezentacja przekształcenia liniowego; związek z macierzą Jakobiego z Analizy matematycznej 2.

2. **Działania na macierzach** — dodawanie macierzy; mnożenie macierzy; transpozycja; macierze elementarne.

3. **Eliminacja Gaussa** — algorytm eliminacji; macierze elementarne i ich rola; sprowadzanie macierzy do postaci schodkowej.

4. **Wyznacznik macierzy** — definicja i obliczanie wyznacznika; własności wyznacznika; interpretacja geometryczna (objętość równoległościanu); rząd macierzy.

5. **Macierz odwrotna** — warunki istnienia macierzy odwrotnej; metody obliczania; zastosowania do rozwiązywania układów równań.

6. **Układy równań liniowych** — twierdzenie Kroneckera-Capelliego; rozwiązywanie układów; dyskusja istnienia i jednoznaczności rozwiązań.

7. **Wartości własne i wektory własne** — definicja i obliczanie wartości własnych; wielomian charakterystyczny; diagonalizacja macierzy; interpretacja geometryczna.

8. **Tematy rozszerzone (grupa gwiazdkowa)** — zastosowania macierzy w informatyce (uczenie maszynowe, warstwy sieci neuronowych, transformacje w grafice komputerowej); rozkłady macierzowe, w szczególności SVD; wprowadzenie do pojęcia tensorów, macierzy unitarnych i podstaw programowania kwantowego.

---

## 4. Analiza matematyczna 1

**Kod przedmiotu:** 0800-AMAT1 *(do uzgodnienia)*
**Kierunek:** Informatyka Stosowana
**Semestr:** I
**Forma zajęć:** wykład + ćwiczenia

### Efekty uczenia się — wiedza

Efekty przedmiotowe W1–W8 realizują efekty kierunkowe: **K_W01**

| Symbol | Opis efektu |
|--------|-------------|
| W1 | Zna systemy liczbowe ($\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$) oraz podstawowe nierówności. |
| W2 | Zna pojęcie ciągu liczbowego i wektorowego, w tym pojęcia granicy, punktu skupienia, granic dolnej i górnej. |
| W3 | Zna notację asymptotyczną Bachmana-Landaua i jej zastosowanie w analizie złożoności algorytmów. |
| W4 | Zna pojęcie szeregu liczbowego, kryteria zbie��ności oraz podstawowe typy szeregów. |
| W5 | Zna pojęcie granicy i ciągłości funkcji jednej zmiennej (definicje Cauchy'ego i Heinego). |
| W6 | Zna pojęcie pochodnej funkcji jednej zmiennej, jej interpretację geometryczną i fizyczną oraz twierdzenia o pochodnych. |
| W7 | Zna pojęcie całki Riemanna funkcji jednej zmiennej oraz podstawowe twierdzenie rachunku różniczkowego i całkowego. |
| W8 | Zna pojęcia zbieżności ciągów i szeregów funkcyjnych (zbieżność punktowa, jednostajna) oraz szeregów potęgowych. |

### Efekty uczenia się — umiejętności

Efekty przedmiotowe U1–U8 realizują efekty kierunkowe: **K_U01**

| Symbol | Opis efektu |
|--------|-------------|
| U1 | Potrafi badać zbieżność ciągów liczbowych i obliczać ich granice. |
| U2 | Potrafi stosować notację asymptotyczną do opisu zachowania ciągów i funkcji. |
| U3 | Potrafi badać zbieżność szeregów liczbowych, stosując odpowiednie kryteria. |
| U4 | Potrafi obliczać granice funkcji i badać ich ciągłość. |
| U5 | Potrafi obliczać pochodne i stosować je do badania monotoniczności, ekstremów, wypukłości i przebiegu zmienności funkcji. |
| U6 | Potrafi stosować wzór Taylora do przybliżania wartości funkcji. |
| U7 | Potrafi obliczać całki oznaczone i nieoznaczone metodami podstawiania i całkowania przez części. |
| U8 | Potrafi stosować rachunek całkowy do obliczania pól, objętości i długości krzywych. |

### Efekty uczenia się — kompetencje społeczne

Efekty przedmiotowe K1–K2 realizują efekty kierunkowe: **K_K01, K_K06**

| Symbol | Opis efektu |
|--------|-------------|
| K1 | Rozumie rolę analizy matematycznej jako fundamentu narzędzi obliczeniowych stosowanych w informatyce, w szczególności w algorytmach optymalizacji i uczeniu maszynowym. |
| K2 | Docenia znaczenie pojęć ciągłości i różniczkowalności w modelowaniu problemów informatycznych. |

### Pełny opis

Przedmiot wprowadza studenta w podstawowe pojęcia analizy matematycznej funkcji jednej zmiennej. Pojęcia takie jak supremum, infimum, ciągłość, pochodna i całka stanowią niezbędny fundament do zrozumienia algorytmów optymalizacji, uczenia maszynowego oraz analizy złożoności.

Program obejmuje następujące zagadnienia:

1. **Ciągi liczbowe i wektorowe** — granica ciągu; punkt skupienia; granice dolna i górna; granice niewłaściwe; granice ciągów zadanych rekurencyjnie.

2. **Szeregi liczbowe** — warunek konieczny zbieżności; sumy częściowe; szeregi arytmetyczny, geometryczny, harmoniczny; kryteria zbieżności (porównawcze, d'Alemberta, Cauchy'ego, całkowe).

3. **Granica i ciągłość funkcji** — definicje Cauchy'ego i Heinego; własność Darboux; twierdzenie Weierstrassa o osiąganiu kresów przez funkcję ciągłą; granice niewłaściwe; ciągłość w punkcie i ciągłość jednostajna.

4. **Ciągi i szeregi funkcyjne** — zbieżność punktowa i jednostajna ciągów funkcji; szeregi potęgowe i promień zbieżności.

5. **Pochodna** — interpretacja geometryczna (styczna do wykresu) i fizyczna (prędkość chwilowa); twierdzenia o pochodnych; symbole nieoznaczone i reguła de l'Hospitala; twierdzenia Rolle'a i Lagrange'a; monotoniczność; ekstrema lokalne i globalne; pochodne wyższych rzędów; wzór Taylora; wypukłość; badanie przebiegu zmienności funkcji.

6. **Całka nieoznaczona (pierwotna)** — pojęcie funkcji pierwotnej; metody całkowania (podstawianie, przez części, ułamki proste).

7. **Całka Riemanna funkcji jednej zmiennej** — interpretacja geometryczna; funkcje całkowalne w sensie Riemanna; podstawowe twierdzenie rachunku różniczkowego i całkowego (Newtona-Leibniza); twierdzenie o zamianie zmiennych; zastosowania: obliczanie pól, objętości brył obrotowych, długości krzywych.

8. **Tematy rozszerzone (grupa gwiazdkowa)** — całka Lebesgue'a jako uogólnienie całki Riemanna oraz jej znaczenie dla analizy, statystyki i rachunku prawdopodobieństwa.

---

## 5. Analiza matematyczna 2

**Kod przedmiotu:** 0800-AMAT2 *(do uzgodnienia)*
**Kierunek:** Informatyka Stosowana
**Semestr:** II
**Forma zajęć:** wykład + ćwiczenia

### Efekty uczenia się — wiedza

Efekty przedmiotowe W1–W8 realizują efekty kierunkowe: **K_W01**

| Symbol | Opis efektu |
|--------|-------------|
| W1 | Zna pojęcie granicy i ciągłości funkcji wielu zmiennych. |
| W2 | Zna pojęcie pochodnej funkcji wielu zmiennych (pochodna Frécheta, pochodna kierunkowa, pochodne cząstkowe). |
| W3 | Zna pojęcie gradientu funkcji i jego interpretację jako kierunku najszybszego wzrostu. |
| W4 | Zna pojęcie macierzy Jakobiego jako reprezentacji pochodnej funkcji wektorowej. |
| W5 | Zna pojęcie funkcji wypukłej wielu zmiennych i jego znaczenie w problemach optymalizacji. |
| W6 | Zna metody znajdowania ekstremów funkcji wielu zmiennych, w tym ekstremów warunkowych. |
| W7 | Zna pojęcia całek wielokrotnych, krzywoliniowych i powierzchniowych. |
| W8 | Zna zastosowania rachunku różniczkowego funkcji wielu zmiennych w informatyce, w tym metodę najszybszego spadku (gradient descent). |

### Efekty uczenia się — umiejętności

Efekty przedmiotowe U1–U7 realizują efekty kierunkowe: **K_U01**

| Symbol | Opis efektu |
|--------|-------------|
| U1 | Potrafi obliczać granice i badać ciągłość funkcji wielu zmiennych. |
| U2 | Potrafi obliczać pochodne cząstkowe, pochodne kierunkowe i gradient funkcji wielu zmiennych. |
| U3 | Potrafi wyznaczać macierz Jakobiego dla funkcji wektorowych. |
| U4 | Potrafi znajdować ekstrema lokalne i globalne funkcji wielu zmiennych. |
| U5 | Potrafi stosować metodę mnożników Lagrange'a do wyznaczania ekstremów warunkowych. |
| U6 | Potrafi obliczać całki wielokrotne, w tym z zastosowaniem twierdzenia Fubiniego. |
| U7 | Potrafi stosować metody rachunku różniczkowego i całkowego w kontekście problemów informatycznych (np. metoda najmniejszych kwadratów, metoda najszybszego spadku). |

### Efekty uczenia się — kompetencje społeczne

Efekty przedmiotowe K1–K2 realizują efekty kierunkowe: **K_K01, K_K06**

| Symbol | Opis efektu |
|--------|-------------|
| K1 | Rozumie znaczenie rachunku różniczkowego i całkowego funkcji wielu zmiennych jako narzędzia optymalizacji w algorytmach uczenia maszynowego. |
| K2 | Jest świadomy konieczności stosowania rygorystycznego aparatu matematycznego w modelowaniu i analizie algorytmów. |

### Pełny opis

Przedmiot stanowi kontynuację Analizy matematycznej 1 i wprowadza rachunek funkcji wielu zmiennych. Pojęcia gradientu, macierzy Jakobiego i funkcji wypukłych są fundamentalne dla zrozumienia algorytmów optymalizacji stosowanych w uczeniu maszynowym — w szczególności metody spadku gradientowego.

Program obejmuje następujące zagadnienia:

1. **Funkcje wielu zmiennych — granice i ciągłość** — granica funkcji wielu zmiennych; ciągłość funkcji wielu zmiennych; przykłady i patologie w porównaniu z funkcjami jednej zmiennej.

2. **Różniczkowanie funkcji wielu zmiennych** — pochodna Frécheta jako uogólnienie pochodnej funkcji jednej zmiennej; pochodna kierunkowa; pochodne cząstkowe; warunki różniczkowalności.

3. **Gradient, rozwinięcie Taylora i ekstrema** — gradient funkcji jako kierunek najszybszego wzrostu; rozwinięcie Taylora dla funkcji wielu zmiennych; ekstrema lokalne i globalne funkcji wielu zmiennych; warunki konieczne i dostateczne istnienia ekstremum; hesjan; interpretacja optymalizacyjna i podstawowe warunki zbieżności metod gradientowych.

4. **Funkcje wypukłe** — definicja i własności funkcji wypukłych; znaczenie wypukłości w problemach optymalizacji.

5. **Ekstrema warunkowe** — metoda mnożników Lagrange'a; zastosowania.

6. **Tematy rozszerzone (grupa gwiazdkowa)** — macierz Jakobiego jako macierz pochodnych cząstkowych i jej interpretacja przez pryzmat przekształceń liniowych; zastosowania rachunku różniczkowego funkcji wielu zmiennych w informatyce (oszacowania błędów rachunkowych, metoda najmniejszych kwadratów, metoda najszybszego spadku); rachunek całkowy funkcji wielu zmiennych: całki podwójne, potrójne i wielokrotne, twierdzenie Fubiniego, całki krzywoliniowe i powierzchniowe oraz wzory Greena, Gaussa-Ostrogradskiego i Stokesa.

---

## 6. Matematyka dyskretna

**Kod przedmiotu:** 0800-MDYS
**Kierunek:** Informatyka Stosowana
**Semestr:** II
**Forma zajęć:** wykład + ćwiczenia

### Efekty uczenia się — wiedza

Efekty przedmiotowe W1–W7 realizują efekty kierunkowe: **K_W01, K_W04**

| Symbol | Opis efektu |
|--------|-------------|
| W1 | Zna pojęcie rekurencji i równań rekurencyjnych oraz metody ich rozwiązywania. |
| W2 | Zna podstawowe pojęcia kombinatoryki: permutacje, wariacje, kombinacje, rozbicia. |
| W3 | Zna notację asymptotyczną Bachmana-Landaua (O, Ω, Θ) oraz pojęcie złożoności obliczeniowej algorytmu. |
| W4 | Zna twierdzenie o rekursji uniwersalnej (Master Theorem) i jego zastosowania. |
| W5 | Zna pojęcie drzewa binarnego, jego strukturę i podstawowe operacje. |
| W6 | Zna podstawowe pojęcia teorii grafów: graf, wierzchołek, krawędź, ścieżka, cykl, spójność, klika. |
| W7 | Zna klasyczne problemy teorii grafów: problem Eulera, problem Hamiltona, kolorowanie grafów. |

### Efekty uczenia się — umiejętności

Efekty przedmiotowe U1–U7 realizują efekty kierunkowe: **K_U02, K_U03, K_U08**

| Symbol | Opis efektu |
|--------|-------------|
| U1 | Potrafi definiować problemy rekurencyjnie i formułować odpowiadające im równania rekurencyjne. |
| U2 | Potrafi rozwiązywać równania rekurencyjne oraz dowodzić poprawności rozwiązań rekurencyjnych. |
| U3 | Potrafi stosować metody kombinatoryczne do zliczania obiektów dyskretnych. |
| U4 | Potrafi wyznaczać złożoność obliczeniową algorytmów z użyciem notacji asymptotycznej. |
| U5 | Potrafi stosować twierdzenie o rekursji uniwersalnej do analizy złożoności algorytmów typu „dziel i zwyciężaj". |
| U6 | Potrafi modelować problemy informatyczne z użyciem drzew binarnych i grafów. |
| U7 | Potrafi rozwiązywać podstawowe problemy na grafach (szukanie ścieżek, cykli, kolorowanie). |

### Efekty uczenia się — kompetencje społeczne

Efekty przedmiotowe K1–K2 realizują efekty kierunkowe: **K_K01, K_K06**

| Symbol | Opis efektu |
|--------|-------------|
| K1 | Rozumie rolę matematyki dyskretnej jako teoretycznego fundamentu algorytmiki i informatyki. |
| K2 | Docenia znaczenie formalnej analizy złożoności algorytmów w projektowaniu efektywnych rozwiązań programistycznych. |

### Pełny opis

Przedmiot stanowi kontynuację Wstępu do matematyki i informatyki i wprowadza kluczowe koncepcje matematyki dyskretnej niezbędne w algorytmice i informatyce teoretycznej. Szczególny nacisk położony jest na narzędzia analizy algorytmów (rekurencja, złożoność obliczeniowa) oraz struktury dyskretne (drzewa, grafy) powszechnie stosowane w informatyce.

Program obejmuje następujące zagadnienia:

1. **Rekurencja** — rekurencja jako metoda definiowania problemów; równania rekurencyjne i metody ich rozwiązywania; dowodzenie poprawności rozwiązań rekurencyjnych; związek rekurencji z indukcją matematyczną.

2. **Kombinatoryka** — podstawowe pojęcia: permutacje, wariacje, kombinacje z powtórzeniami i bez; rozbicia zbiorów; zasada włączeń i wyłączeń; zasada szufladkowa Dirichleta.

3. **Asymptotyka i złożoność algorytmu** — notacja asymptotyczna Bachmana-Landaua (O, Ω, Θ); klasy złożoności; twierdzenie o rekursji uniwersalnej (Master Theorem) i jego zastosowanie do analizy algorytmów „dziel i zwyciężaj".

4. **Drzewa binarne** — definicja i struktura drzew binarnych; operacje na drzewach; obchodzenie drzew (preorder, inorder, postorder); zastosowania drzew binarnych w algorytmice — problemy naturalnie rozwiązywalne przez rekurencję.

5. **Teoria grafów** — pojęcia podstawowe: graf skierowany i nieskierowany, wierzchołki, krawędzie, ścieżki, cykle, kliki, spójność; stopień wierzchołka; grafy dwudzielne; problem ścieżki Eulera; problem cyklu Hamiltona; kolorowanie grafów.

---

## 7. Rachunek prawdopodobieństwa

**Kod przedmiotu:** 0800-RPROB *(do uzgodnienia)*
**Kierunek:** Informatyka Stosowana
**Semestr:** III
**Forma zajęć:** wykład + ćwiczenia

### Efekty uczenia się — wiedza

Efekty przedmiotowe W1–W7 realizują efekty kierunkowe: **K_W01**

| Symbol | Opis efektu |
|--------|-------------|
| W1 | Zna pojęcia σ-ciała, miary i przestrzeni mierzalnej jako formalne podstawy teorii prawdopodobieństwa. |
| W2 | Zna aksjomaty teorii prawdopodobieństwa (aksjomaty Kołmogorowa) oraz pojęcie przestrzeni probabilistycznej. |
| W3 | Zna pojęcie prawdopodobieństwa warunkowego, niezależności zdarzeń i zmiennych losowych, wzór na prawdopodobieństwo całkowite i wzór Bayesa. |
| W4 | Zna pojęcie schematu Bernoulliego. |
| W5 | Zna pojęcie zmiennej losowej, jej rozkładu (dyskretnego i ciągłego), dystrybuanty i funkcji gęstości. |
| W6 | Zna podstawowe rozkłady prawdopodobieństwa: dwumianowy, Poissona, jednostajny, wykładniczy, normalny. |
| W7 | Zna charakterystyki liczbowe zmiennych losowych: wartość oczekiwaną, wariancję, momenty, kowariancję i współczynnik korelacji. |

### Efekty uczenia się — umiejętności

Efekty przedmiotowe U1–U7 realizują efekty kierunkowe: **K_U01**

| Symbol | Opis efektu |
|--------|-------------|
| U1 | Potrafi konstruować model probabilistyczny dla opisanego doświadczenia losowego. |
| U2 | Potrafi stosować wzór na prawdopodobieństwo całkowite i wzór Bayesa do rozwiązywania problemów. |
| U3 | Potrafi wyznaczać rozkład zmiennej losowej, obliczać jej dystrybuantę i charakterystyki liczbowe. |
| U4 | Potrafi identyfikować i stosować standardowe rozkłady prawdopodobieństwa w modelowaniu zjawisk losowych. |
| U5 | Potrafi badać niezależność zdarzeń i zmiennych losowych. |
| U6 | Potrafi obliczać wartość oczekiwaną, wariancję, kowariancję i współczynnik korelacji. |
| U7 | Potrafi stosować pojęcia rachunku prawdopodobieństwa w kontekście algorytmów probabilistycznych i analizy danych. |

### Efekty uczenia się — kompetencje społeczne

Efekty przedmiotowe K1–K2 realizują efekty kierunkowe: **K_K01, K_K06**

| Symbol | Opis efektu |
|--------|-------------|
| K1 | Rozumie rolę modelowania probabilistycznego w informatyce, w tym w uczeniu maszynowym, kryptografii i analizie algorytmów probabilistycznych. |
| K2 | Jest świadomy ograniczeń modeli deterministycznych i znaczenia podejścia probabilistycznego w rozwiązywaniu problemów praktycznych. |

### Pełny opis

Przedmiot wprowadza formalne podstawy teorii prawdopodobieństwa — od aparatu pojęciowego (σ-ciała, miary) przez zmienne losowe i ich charakterystyki, aż po elementy procesów stochastycznych. Pojęcia te stanowią fundament dla statystyki, uczenia maszynowego, analizy algorytmów probabilistycznych i modelowania stochastycznego w informatyce.

Program obejmuje następujące zagadnienia:

1. **Podstawy teorii miary** — σ-ciała (σ-algebry zbiorów): definicja, przykłady, σ-ciało generowane przez rodzinę zbiorów; miara i przestrzeń mierzalna; miara probabilistyczna jako szczególny przypadek miary.

2. **Doświadczenie losowe i przestrzeń probabilistyczna** — przestrzeń zdarzeń elementarnych; zdarzenia losowe; aksjomaty Kołmogorowa; własności prawdopodobieństwa (monotoniczność, ciągłość, nierówność Boole'a); klasyczna definicja prawdopodobieństwa (model Laplace'a).

3. **Prawdopodobieństwo warunkowe i niezależność** — prawdopodobieństwo warunkowe: definicja i własności; wzór na prawdopodobieństwo całkowite; wzór Bayesa i jego zastosowania (m.in. w klasyfikatorze bayesowskim); niezależność zdarzeń; niezależność zmiennych losowych; niezależność doświadczeń losowych; schemat Bernoulliego.

4. **Zmienne losowe** — definicja zmiennej losowej jako funkcji mierzalnej; rozkład dyskretny i ciągły; dystrybuanta: definicja, własności, interpretacja; funkcja gęstości prawdopodobieństwa; funkcja masy prawdopodobieństwa; przykłady rozkładów: dwumianowy, Poissona, jednostajny, wykładniczy, normalny.

5. **Charakterystyki liczbowe zmiennych losowych** — wartość oczekiwana: definicja, własności, interpretacja; wariancja i odchylenie standardowe; momenty wyższych rzędów; kowariancja i współczynnik korelacji.

6. **Tematy rozszerzone (grupa gwiazdkowa)** — zbieżność według prawdopodobieństwa, zbieżność prawie na pewno oraz słaba zbieżność miar; słabe i mocne prawo wielkich liczb; centralne twierdzenie graniczne; warunkowanie zmiennych losowych oraz wektory losowe; elementy teorii procesów stochastycznych: definicja procesu stochastycznego, procesy o przyrostach niezależnych, procesy stacjonarne, podstawowe charakterystyki procesów stochastycznych (funkcja średnia, funkcja korelacji).

---

## 8. Statystyka

**Kod przedmiotu:** 0800-STAT *(do uzgodnienia)*
**Kierunek:** Informatyka Stosowana
**Semestr:** IV *(po Rachunku prawdopodobieństwa)*
**Forma zajęć:** wykład + ćwiczenia

### Efekty uczenia się — wiedza

Efekty przedmiotowe W1–W6 realizują efekty kierunkowe: **K_W01**

| Symbol | Opis efektu |
|--------|-------------|
| W1 | Zna rodzaje danych i skal pomiarowych oraz podstawowe miary statystyki opisowej (miary tendencji centralnej i rozproszenia). |
| W2 | Zna metody wizualizacji danych (histogramy, wykresy pudełkowe, wykresy rozrzutu). |
| W3 | Zna pojęcie próby losowej, populacji oraz podstawowe schematy losowania. |
| W4 | Zna pojęcie estymacji punktowej i przedziałowej oraz własności estymatorów (nieobciążoność, efektywność, zgodność). |
| W5 | Zna pojęcie testu statystycznego, hipotezy zerowej i alternatywnej, poziomu istotności oraz p-wartości. |
| W6 | Zna podstawowe testy statystyczne (test t-Studenta, test z) i warunki ich stosowania. |

### Efekty uczenia się — umiejętności

Efekty przedmiotowe U1–U6 realizują efekty kierunkowe: **K_U01, K_U04**

| Symbol | Opis efektu |
|--------|-------------|
| U1 | Potrafi przeprowadzić analizę statystyki opisowej dla danego zbioru danych, w tym obliczać miary tendencji centralnej i rozproszenia. |
| U2 | Potrafi dobrać i wykonać odpowiednią wizualizację danych. |
| U3 | Potrafi przeprowadzić estymację punktową i przedziałową parametrów rozkładu na podstawie próby losowej. |
| U4 | Potrafi sformułować hipotezę statystyczną i przeprowadzić test statystyczny, interpretując wynik w kontekście problemu. |
| U5 | Potrafi stosować test t-Studenta i test z do weryfikacji hipotez o wartości oczekiwanej. |
| U6 | Potrafi stosować metody statystyczne w kontekście analizy danych informatycznych (np. ocena jakości modelu, porównywanie wyników eksperymentów). |

### Efekty uczenia się — kompetencje społeczne

Efekty przedmiotowe K1–K2 realizują efekty kierunkowe: **K_K01, K_K02, K_K06**

| Symbol | Opis efektu |
|--------|-------------|
| K1 | Rozumie rolę wnioskowania statystycznego w podejmowaniu decyzji opartych na danych w informatyce i naukach stosowanych. |
| K2 | Jest świadomy zagrożeń wynikających z niewłaściwego stosowania metod statystycznych (np. p-hacking, nadmierne dopasowanie modelu). |

### Pełny opis

Przedmiot poświęcony jest metodom opisu danych oraz wnioskowaniu statystycznemu. Opiera się na pojęciach wprowadzonych w Rachunku prawdopodobieństwa. Umiejętności statystyczne są niezbędne w informatyce stosowanej m.in. do oceny jakości modeli uczenia maszynowego, analizy wyników eksperymentów obliczeniowych oraz podejmowania decyzji opartych na danych.

Program obejmuje następujące zagadnienia:

1. **Statystyka opisowa** — rodzaje danych i skal pomiarowych (nominalna, porządkowa, interwałowa, ilorazowa); miary tendencji centralnej: średnia arytmetyczna, mediana, dominanta (moda); miary rozproszenia: wariancja, odchylenie standardowe, rozstęp, odchylenie ćwiartkowe; wizualizacja danych: histogramy, wykresy pudełkowe (box plot), wykresy rozrzutu (scatter plot).

2. **Wnioskowanie statystyczne** — pojęcie próby losowej i populacji; estymacja punktowa: estymatory, obciążenie, efektywność, zgodność; estymacja przedziałowa: przedziały ufności dla wartości oczekiwanej i proporcji; testowanie hipotez statystycznych: hipoteza zerowa i alternatywna, poziom istotności, p-wartość, moc testu; testowanie hipotez o wartości oczekiwanej: test t-Studenta (dla małych prób), test z (dla dużych prób); interpretacja wyników testów statystycznych w kontekście problemów informatycznych.

3. **Tematy rozszerzone (grupa gwiazdkowa)** — regresja liniowa; problem overfittingu; kompromis bias–variance.
