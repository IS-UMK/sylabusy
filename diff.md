# Analiza zmian w sylabusach — Informatyka Stosowana UMK

> **Dokument porównuje** stare sylabusy kierunku Informatyka Stosowana (obowiązujące przed reformą)
> z nowymi propozycjami zawartymi w tym repozytorium.
> Omówione przedmioty: Algebra 1 i 2, Analiza matematyczna 1 i 2, Matematyka dyskretna,
> Statystyka i rachunek prawdopodobieństwa.

---

## Spis treści

1. [Cele reformy](#1-cele-reformy)
2. [Zmiany strukturalne (przekrojowe)](#2-zmiany-strukturalne-przekrojowe)
3. [Algebra liniowa](#3-algebra-liniowa)
4. [Analiza matematyczna](#4-analiza-matematyczna)
5. [Matematyka dyskretna](#5-matematyka-dyskretna)
6. [Statystyka → Rachunek prawdopodobieństwa + Statystyka](#6-statystyka--rachunek-prawdopodobieństwa--statystyka)
7. [Podsumowanie](#8-podsumowanie)

---

## 1. Cele reformy

Reforma programu jest motywowana kilkoma wyraźnymi celami:

| Cel | Wyjaśnienie |
|-----|-------------|
| **Intuicja przed formalizacją** | Pojęcia matematyczne mają być najpierw zakorzenione w intuicji geometrycznej lub obliczeniowej, a dopiero potem formalizowane. |
| **Połączenie teorii z praktyką AI/ML** | Student od pierwszego semestru widzi, *po co* dana teoria jest potrzebna — np. regresja liniowa, gradient descent, sieci neuronowe. |
| **Kultura współpracy i jakości kodu** | Kod pisany tak, aby czytający wkładał minimalne wysiłki w zrozumienie; nacisk na dobre praktyki (git, testy, code review). |
| **Ścieżki specjalizacyjne** | Po 2 latach wspólnych podstaw student wybiera jedną z kilku ścieżek (AI/Python, gaming, networking, C++, neuronauki). |
| **Grupy gwiazdkowe** | W ramach każdego przedmiotu istnieje co najmniej jedna grupa gwiazdkowa dla zaawansowanych i zainteresowanych studentów. |
| **Ujednolicenie oceniania** | Wspólne kolokwia dla wszystkich grup danego przedmiotu — przejrzystość i sprawiedliwość. |
| **Podniesienie poziomu kształcenia** | Renoma → rekrutacja najlepszych studentów → włączenie ich w badania naukowe. |

---

## 2. Zmiany strukturalne (przekrojowe)

### Rozbicie lub uporządkowanie dotychczasowego materiału

Najważniejsza zmiana nie polega tylko na „dodaniu tematów”, ale na **innym rozłożeniu treści między kursami**.

| Stary plan | Nowy plan |
|-----------|-----------|
| **Algebra 1** + **Algebra 2** istniały już formalnie jako dwa kursy, ale ich układ był podporządkowany klasycznemu porządkowi matematycznemu | **Algebra liniowa 1** i **2** zostają przeprojektowane pod potrzeby Informatyki Stosowanej |
| **Analiza matematyczna 1** obejmowała głównie funkcje jednej zmiennej, ale zawierała też elementy funkcji wielu zmiennych i równań różniczkowych | **Analiza matematyczna 1** zostaje wyraźnie uporządkowana wokół jednej zmiennej, a **Analiza matematyczna 2** przejmuje rachunek wielu zmiennych |
| **Statystyka i rachunek prawdopodobieństwa** był jednym kursem | **Rachunek prawdopodobieństwa** (sem. III) + **Statystyka** (sem. IV) |
| Elementy logiki, zbiorów i relacji były rozproszone po Algebrze 1 i Matematyce dyskretnej | Zostają przeniesione do **Wstępu do matematyki i informatyki** |


**Dlaczego?**  
Taki podział pozwala:
- zachować lepszą kolejność zależności pojęciowych,
- ograniczyć przeładowanie pojedynczych kursów,
- lepiej powiązać matematykę z algorytmiką, programowaniem i AI/ML,
- wyraźniej oddzielić materiał fundamentowy od materiału specjalistycznego i rozszerzonego.

### Nowy przedmiot wprowadzający

Dodano **Wstęp do matematyki i informatyki** (sem. I), który buduje wspólny język formalny (logika, zbiory, relacje, funkcje, indukcja, porządki) niezbędny do rozumienia pozostałych kursów.  
W starym planie te treści były częściowo realizowane w **Algebrze 1** oraz częściowo zakładane jako znane albo omawiane przy okazji innych przedmiotów.

### Orientacja na zastosowania w AI/ML i informatyce

Każdy nowy syllabus matematyczny zawiera lub zapowiada:
- sekcję zastosowań w informatyce,
- jawne powiązania między przedmiotami,
- większy nacisk na analizę algorytmiczną, optymalizację, reprezentację danych i modele obliczeniowe,
- tematykę rozszerzoną dla grup gwiazdkowych.

---

## 3. Algebra liniowa

### Stary syllabus

Stary plan nie miał jednego kursu algebry liniowej, lecz dwa osobne przedmioty: **Algebra 1** i **Algebra 2**.

#### Stara Algebra 1

Zakres starej **Algebry 1** obejmował przede wszystkim:
- rachunek wektorowy w przestrzeni trójwymiarowej,
- elementy logiki,
- teorię zbiorów,
- relacje,
- zbiory liczbowe i indukcję matematyczną,
- funkcje i ich własności,
- liczby zespolone,
- macierze,
- układy równań liniowych.

Był to więc kurs **bardzo szeroki i hybrydowy**: łączył elementy języka formalnego, algebry elementarnej, rachunku wektorowego i wstępu do macierzy.

#### Stara Algebra 2

Stara **Algebra 2** była już bardziej klasycznym kursem algebry liniowej. Obejmowała:
- przestrzenie liniowe,
- liniową zależność i niezależność,
- bazy i wymiar,
- przekształcenia liniowe,
- jądro i obraz,
- wartości własne i wektory własne,
- formy dwuliniowe i kwadratowe,
- przestrzenie euklidesowe,
- ortogonalizację,
- przekształcenia ortogonalne,
- tensory i formy wieloliniowe.

**Charakterystyczne cechy starego podejścia:**
- Algebra 1 była kursem mieszanym, łączącym wiele niejednorodnych tematów.
- Algebra 2 miała klasyczny, dość abstrakcyjny charakter.
- Nacisk kładziono na aparat matematyczny potrzebny także fizyce i kierunkom technicznym, nie specyficznie informatyce stosowanej.
- Zastosowania informatyczne lub ML były w sylabusach starego planu nieobecne albo co najwyżej domyślne.

### Nowy syllabus

#### Algebra liniowa 1 (semestr I)

Nowa Algebra liniowa 1 skupia się na **wektorach w przestrzeniach euklidesowych** i intuicji geometrycznej:
- działania na wektorach,
- interpretacja geometryczna (proste, płaszczyzny, rzutowania),
- iloczyn skalarny, norma, prostopadłość, rzuty,
- liniowa niezależność, bazy, układ współrzędnych,
- wypukłość i afiniczność,
- zastosowania do reprezentacji danych i geometrii obliczeniowej,
- w grupie gwiazdkowej: przestrzeń Hilberta, rzuty ortogonalne, problemy najmniejszych kwadratów.

#### Algebra liniowa 2 (semestr II)

Nowa Algebra liniowa 2 skupia się na **macierzach jako narzędziu obliczeniowym i modelującym**:
- macierz jako reprezentacja przekształcenia liniowego,
- działania na macierzach,
- eliminacja Gaussa i macierze elementarne,
- wyznacznik, rząd, interpretacja geometryczna,
- macierz odwrotna,
- układy równań liniowych,
- wartości własne, wektory własne, diagonalizacja,
- zastosowania w uczeniu maszynowym i grafice,
- w grupie gwiazdkowej: rozkłady macierzowe, tensory, pytorch, macierze unitarne, programowanie kwantowe.

### Kluczowe zmiany w algebrze

| Aspekt | Stary plan | Nowy plan |
|--------|-----------|-----------|
| Status kursów | Dwa kursy już istniały: Algebra 1 i Algebra 2 | Dwa kursy pozostają, ale są przeprojektowane pod Informatykę Stosowaną |
| Algebra 1 | Mieszanka: wektory + logika + zbiory + relacje + liczby zespolone + macierze | Skupienie na wektorach, geometrii euklidesowej i intuicji |
| Algebra 2 | Klasyczna algebra liniowa: przestrzenie liniowe, przekształcenia, formy, tensory | Macierze jako centralny temat, z mocniejszym komponentem obliczeniowym i zastosowaniowym |
| Logika i zbiory | Obecne w Algebrze 1 | Przeniesione do osobnego kursu wstępnego |
| Liczby zespolone | Obecne w Algebrze 1 | Nie są już osią kursu algebry liniowej |
| Zastosowania w informatyce | Nieeksponowane | Jawne: ML, reprezentacja danych, grafika, least squares, SVD/tensory |
| Intuicja geometryczna | Obecna, ale tylko jako jedna z części | Staje się osią Algebry 1 |

---

## 4. Analiza matematyczna

### Stary syllabus

Stary plan obejmował **dwa osobne kursy: Analizę matematyczną 1 i Analizę matematyczną 2**, ale ich profil był wyraźnie bardziej klasyczny i silniej związany z potrzebami fizyki oraz kierunków technicznych niż z informatyką stosowaną.

#### Stara Analiza matematyczna 1

Stary syllabus **Analizy matematycznej 1** obejmował przede wszystkim:
- liczby i sposoby ich prezentacji,
- funkcje i funkcje elementarne,
- granice ciągów i funkcji,
- ciągłość,
- pochodne i różniczki,
- szereg Taylora,
- całkę nieoznaczoną i oznaczoną,
- równania różniczkowe zwyczajne I i II rzędu,
- podstawowe pojęcia funkcji wielu zmiennych,
- pochodne cząstkowe i różniczkę zupełną,
- metody przybliżone w obliczeniach.

Był to więc kurs, który:
- nie był ograniczony do analizy jednej zmiennej,
- już na pierwszym etapie wprowadzał elementy funkcji wielu zmiennych,
- zawierał równania różniczkowe zwyczajne,
- kładł silny nacisk na techniki rachunkowe i klasyczny aparat analizy.

#### Stara Analiza matematyczna 2

Stary syllabus **Analizy matematycznej 2** miał profil jeszcze mocniej osadzony w klasycznej analizie stosowanej do fizyki, astronomii i kierunków technicznych. Obejmował m.in.:
- całki wielokrotne,
- twierdzenie Fubiniego,
- całkowanie w układach biegunowych, walcowych i sferycznych,
- ogólną zmianę zmiennych i jakobian,
- całki krzywoliniowe,
- całki powierzchniowe,
- twierdzenia Greena, Gaussa i Stokesa,
- szeregi trygonometryczne i szeregi Fouriera,
- splot,
- transformatę Fouriera i jej własności,
- transformatę Laplace’a i jej własności,
- zastosowania transformat do rozwiązywania równań różniczkowych,
- elementy funkcji zmiennej zespolonej,
- w wariancie dla kierunków technicznych także DFT i transformatę Z.

To oznacza, że stara Analiza 2 **nie była po prostu kursem rachunku wielu zmiennych**. Była raczej połączeniem:
- klasycznej analizy wielowymiarowej,
- analizy wektorowej,
- analizy harmonicznej w wersji podstawowej,
- metod transformat,
- oraz elementów analizy zespolonej.

**Charakterystyczne cechy starego podejścia:**
- materiał był szeroki i częściowo heterogeniczny,
- nacisk szedł w stronę narzędzi przydatnych w fizyce, sygnałach i równaniach różniczkowych,
- klasyczna analiza wektorowa (Green, Gauss, Stokes) była ważną częścią kursu,
- obecne były treści transformacyjne (Fourier, Laplace, czasem DFT/Z), które nie należą do podstawowego rdzenia nowej analizy matematycznej dla Informatyki Stosowanej,
- kurs miał bardziej profil matematyczno-techniczny niż optymalizacyjno-informatyczny.

### Nowy syllabus

#### Analiza matematyczna 1 (semestr I)

Nowa Analiza 1 jest bardziej świadomie uporządkowana wokół analizy jednej zmiennej i narzędzi przydatnych także informatycznie. Obejmuje przede wszystkim:
- systemy liczbowe,
- ciągi liczbowe i wektorowe,
- granice, punkty skupienia oraz granice dolne i górne,
- granice niewłaściwe,
- ciągi zadane rekurencyjnie,
- asymptotykę i notację Bachmana-Landaua,
- szeregi liczbowe i kryteria zbieżności,
- granicę i ciągłość funkcji,
- definicje Cauchy'ego i Heinego,
- własność Darboux,
- twierdzenie Weierstrassa o osiąganiu kresów,
- ciągi i szeregi funkcyjne,
- szeregi potęgowe,
- pochodną i jej interpretacje,
- twierdzenia Rolle'a i Lagrange'a,
- regułę de l'Hospitala,
- monotoniczność, ekstrema, pochodne wyższych rzędów,
- wzór Taylora,
- wypukłość i badanie przebiegu zmienności funkcji,
- całkę nieoznaczoną,
- całkę Riemanna funkcji jednej zmiennej,
- podstawowe twierdzenie rachunku różniczkowego i całkowego oraz zmianę zmiennych w całce Riemanna.

W porównaniu ze starym układem kurs jest wyraźniej skoncentrowany na **solidnym fundamencie analizy jednej zmiennej**, bez mieszania go z większym blokiem treści wielowymiarowych i bez rozbudowanego komponentu równań różniczkowych.

#### Analiza matematyczna 2 (semestr II)

Nowa Analiza 2 przejmuje rachunek wielu zmiennych, ale jest zarazem **węższa i lepiej sprofilowana** niż stara Analiza 2. Obejmuje:
- granice i ciągłość funkcji wielu zmiennych,
- różniczkowanie funkcji wielu zmiennych: pochodną Frécheta, pochodną kierunkową i pochodne cząstkowe,
- gradient oraz ekstrema funkcji wielu zmiennych,
- funkcje wypukłe,
- macierz Jacobiego,
- ekstrema warunkowe i metodę współczynników nieoznaczonych,
- zastosowania: oszacowania błędów rachunkowych, metodę najmniejszych kwadratów, metodę najszybszego spadku, autograd,
- rachunek całkowy funkcji wielu zmiennych ograniczony do całek podwójnych, potrójnych i wielokrotnych wraz z twierdzeniem Fubiniego i całkami iterowanymi.

W porównaniu ze starym syllabussem Analizy 2 nowy kurs:
- **rezygnuje z dużej części klasycznej analizy wektorowej**,
- nie obejmuje już w podstawowym opisie całek krzywoliniowych i powierzchniowych,
- nie obejmuje twierdzeń Greena, Gaussa-Ostrogradskiego i Stokesa,
- nie zawiera bloków poświęconych transformatom Fouriera i Laplace’a,
- nie zawiera elementów funkcji zespolonych ani wariantu dyskretnego typu DFT/Z,
- przesuwa środek ciężkości z metod fizyczno-sygnałowych na podstawy potrzebne dla optymalizacji, probabilistyki, statystyki i zastosowań obliczeniowych.

### Kluczowe zmiany w analizie matematycznej

| Aspekt | Stary plan | Nowy plan |
|--------|-----------|-----------|
| Podział na kursy | Analiza 1 i 2 istniały już wcześniej, ale oba miały bardziej klasyczny i techniczny profil | Wyraźny podział: jedna zmienna → wiele zmiennych |
| Analiza 1 | Oprócz rachunku jednej zmiennej zawierała też ODE oraz wstęp do funkcji wielu zmiennych | Zostaje uporządkowana wokół fundamentów analizy jednej zmiennej |
| Analiza 2 | Całki wielokrotne + analiza wektorowa + Fourier/Laplace + elementy zespolone | Skupienie na funkcjach wielu zmiennych, różniczkowaniu, ekstremach, wypukłości i całkach wielokrotnych |
| Równania różniczkowe | Obecne już w Analizie 1, a pośrednio wracały przez Laplace’a w Analizie 2 | Nie są osią nowego opisu analizy |
| Funkcje wielu zmiennych | Obecne częściowo już w Analizie 1, a dalej rozwijane klasycznie w Analizie 2 | Stają się centralnym tematem Analizy 2 |
| Analiza wektorowa | Green, Gauss, Stokes oraz całki krzywoliniowe i powierzchniowe były częścią Analizy 2 | Znika z podstawowego opisu nowego kursu |
| Transformaty | Fourier i Laplace były centralną częścią starej Analizy 2 | Nie należą do podstawowego rdzenia nowego kursu |
| Asymptotyka | Nieeksponowana | Wprowadzona explicite jako narzędzie ważne dla informatyki |
| Zastosowania obliczeniowe | Słabo wyodrębnione lub związane raczej z fizyką i sygnałami | Jawne: least squares, metoda najszybszego spadku, autograd, oszacowania błędów |
| Profil kursu | Fizyka/technika + biegłość rachunkowa + transformaty | Informatyka stosowana + optymalizacja + dobrze uporządkowane fundamenty |

---

## 5. Matematyka dyskretna

### Stary syllabus

Stara **Matematyka dyskretna** nie była po prostu standardowym kursem „logika + kombinatoryka + grafy”, lecz przedmiotem o mocno wyspecjalizowanym profilu. Obejmowała m.in.:
- teorię liczb i obliczeniową teorię liczb,
- ciała, pierścienie i grupy,
- kody liniowe i kody korekcyjne,
- krzywe eliptyczne nad ciałami skończonymi,
- kryptografię z kluczem publicznym,
- algorytmy faktoryzacji i testy pierwszości,
- logarytm dyskretny,
- teorię grafów,
- drzewa,
- problemy Eulera i Hamiltona.

Był to więc kurs o profilu **teoria liczb + algebra dyskretna + kryptografia + grafy**.

**Charakterystyczne cechy starego podejścia:**
- silna obecność teorii liczb i struktur algebraicznych,
- duży nacisk na kryptografię i algorytmy kryptograficzne,
- grafy były tylko jedną z części większego kursu,
- kurs był bardziej matematyczno-kryptograficzny niż algorytmiczno-informatyczny,
- logika i relacje były wymagane wstępnie, ale nie stanowiły już centralnej treści kursu.

### Nowy syllabus

Nowa Matematyka dyskretna ma profil znacznie bliższy potrzebom pierwszych kursów algorytmiki:
- rekurencja i równania rekurencyjne,
- dowody poprawności,
- kombinatoryka,
- asymptotyka i złożoność,
- Master Theorem,
- drzewa binarne,
- teoria grafów,
- problemy Eulera, Hamiltona, kolorowanie,
- ścisłe powiązanie z Wstępem do algorytmów.

Kurs jest przy tym pomyślany jako **kontynuacja Wstępu do matematyki i informatyki**, a więc nie musi już od początku budować aparatu logiczno-zbiorowego.

### Kluczowe zmiany w matematyce dyskretnej

| Aspekt | Stary plan | Nowy plan |
|--------|-----------|-----------|
| Dominujący profil | Teoria liczb, algebra dyskretna, kryptografia, kody, grafy | Rekurencja, kombinatoryka, asymptotyka, drzewa, grafy |
| Teoria liczb | Centralna | Usunięta z osi kursu |
| Kryptografia | Centralna | Usunięta z kursu podstawowego |
| Struktury algebraiczne | Grupy, ciała, pierścienie obecne | Nie stanowią głównego celu kursu |
| Grafy | Jedna z części kursu | Nadal ważne, ale osadzone bardziej algorytmicznie |
| Złożoność obliczeniowa | Obecna punktowo przy analizie algorytmów teorii liczb | Staje się jednym z głównych tematów |
| Powiązanie z algorytmiką | Pośrednie | Bezpośrednie i zamierzone programowo |
| Rola kursu | Kurs specjalistyczno-matematyczny | Kurs fundamentowy dla algorytmiki i informatyki teoretycznej |

---

## 6. Statystyka → Rachunek prawdopodobieństwa + Statystyka

### Stary syllabus

Stary przedmiot nosił nazwę **Statystyka i rachunek prawdopodobieństwa** i był jednym kursem obejmującym zarówno probabilistykę, jak i statystykę matematyczną. Zakres obejmował m.in.:
- podstawy prawdopodobieństwa,
- przestrzeń probabilistyczną i miarę probabilistyczną,
- zdarzenia i zmienne losowe,
- rozkłady dyskretne i ciągłe,
- dystrybuantę i gęstość,
- zdarzenia niezależne,
- zmienne dwuwymiarowe,
- momenty statystyczne,
- twierdzenia graniczne,
- estymację punktową i przedziałową,
- testowanie hipotez,
- p-wartość i nadużycia interpretacyjne,
- prawo propagacji błędu,
- regresję liniową.

Ten kurs był więc merytorycznie całkiem bogaty, ale **łączył w jednym semestrze dwa różne porządki myślenia**: modelowanie losowości oraz wnioskowanie z danych.

**Charakterystyczne cechy starego podejścia:**
- probabilistyka i statystyka były nierozdzielone,
- formalizm teorii miary pojawiał się co najwyżej szczątkowo,
- nacisk był położony na podstawowy aparat potrzebny do analizy danych fizycznych i astronomicznych,
- regresja liniowa i testowanie hipotez były obecne, ale bez szerszego osadzenia w nowoczesnym data/ML workflow.

### Nowy syllabus

#### Rachunek prawdopodobieństwa (semestr III)

Nowy kurs probabilistyki ma wyraźnie mocniejsze fundamenty formalne:
- σ-ciała, miara, przestrzeń mierzalna,
- aksjomaty Kołmogorowa,
- prawdopodobieństwo warunkowe i niezależność,
- wzór Bayesa i jego zastosowania,
- zmienne losowe jako funkcje mierzalne,
- rozkłady i charakterystyki liczbowe,
- w grupie gwiazdkowej: prawa wielkich liczb, CTG, procesy stochastyczne, wektory losowe.

#### Statystyka (semestr IV)

Nowa Statystyka oddziela etap wnioskowania z danych:
- statystyka opisowa,
- wizualizacja danych,
- próba i populacja,
- estymacja punktowa i przedziałowa,
- testowanie hipotez,
- test t-Studenta i test z,
- zastosowania do oceny modeli i eksperymentów,
- w grupie gwiazdkowej: regresja liniowa, overfitting, bias-variance.

### Kluczowe zmiany w statystyce i probabilistyce

| Aspekt | Stary plan | Nowy plan |
|--------|-----------|-----------|
| Struktura | Jeden kurs łączący rachunek prawdopodobieństwa i statystykę | Dwa osobne kursy |
| Fundament formalny | Przestrzeń probabilistyczna i miara probabilistyczna pojawiały się, ale bez pełnego nacisku na teorię miary jako podstawę | σ-ciała i miara stają się jawnie podstawą |
| Statystyka opisowa i inferencja | W jednym kursie obok probabilistyki | Otrzymują osobny kurs i większą klarowność |
| CTG i twierdzenia graniczne | Obecne | Nadal obecne, ale przeniesione do probabilistyki, zwłaszcza w rozszerzeniach |
| Regresja liniowa | Obecna pod koniec kursu | Zachowana jako temat rozszerzony kursu statystyki |
| Wizualizacja danych | Nieeksponowana | Wprost wpisana do nowego opisu statystyki |
| Kontekst zastosowań | Dane fizyczne i astronomiczne | Informatyka, analiza danych, ML, ocena modeli |

---


## 7. Podsumowanie

### Tabela porównawcza — najważniejsze zmiany

| Kategoria | Stary plan | Nowy plan |
|-----------|-----------|-----------|
| **Algebra** | Dwa kursy, ale Algebra 1 była bardzo mieszana, a Algebra 2 klasyczno-abstrakcyjna | Dwa kursy zaprojektowane pod logikę: geometria/wektory → macierze/zastosowania |
| **Analiza** | Dwa kursy istniejące formalnie, ale z mniej wyraźnym profilem informatycznym | Wyraźny podział: jedna zmienna / wiele zmiennych + optymalizacja i zastosowania obliczeniowe |
| **Matematyka dyskretna** | Teoria liczb, kryptografia, kody, grafy | Fundament dla algorytmiki: rekurencja, asymptotyka, drzewa, grafy |
| **Statystyka i prawdopodobieństwo** | Jeden wspólny kurs | Dwa osobne kursy |
| **Język formalny** | Rozproszony po Algebrze 1 i wymaganiach wstępnych | Osobny kurs: Wstęp do matematyki i informatyki |
| **Zastosowania w informatyce** | Słabo wyeksponowane | Jawnie wpisane do opisów |
| **ML/AI** | Brak lub śladowa obecność | Jeden z głównych motywów reformy |
| **Powiązanie z algorytmiką** | Niejednolite | Projektowane explicite między kursami |
| **Grupy zaawansowane** | Niesystematyczne lub nieopisane | Grupy gwiazdkowe wpisane w koncepcję programu |

### Główne powody reformy

1. **Lepsze uporządkowanie materiału** — stare kursy często łączyły treści o bardzo różnym charakterze; nowy plan rozkłada je zgodniej z zależnościami merytorycznymi.
2. **Silniejsze powiązanie z informatyką stosowaną** — matematyka ma prowadzić do rozumienia algorytmów, optymalizacji, danych i ML.
3. **Oddzielenie fundamentów od specjalizacji** — język formalny, algorytmika, probabilistyka i statystyka dostają bardziej przejrzyste miejsca w programie.
4. **Większa motywacja studentów** — zastosowania pokazują, po co dany aparat matematyczny jest potrzebny.
5. **Lepsza spójność całego programu** — przedmioty są projektowane jako system naczyń połączonych, a nie zbiór niezależnych kursów.
6. **Nowoczesny profil studiów** — obok treści matematycznych pojawiają się narzędzia pracy programisty i kultura inżynierska od pierwszego semestru.
