
- [Cele studiów inżynierskich](#cele-studiów-inżynierskich)
- [Organizacja studiów inżynierskich](#organizacja-studiów-inżynierskich)
- [Graf zależności](#graf-zależności)
- [Ścieżki specjalizacyjne](#ścieżki-specjalizacyjne)
- [Kalendarz](#kalendarz)
  - [Semestr I](#semestr-i)
  - [Semestr II](#semestr-ii)
  - [Semestr III](#semestr-iii)
  - [Semestr IV](#semestr-iv)
  - [Semestry V-VII - Specjalizacje](#semestry-v-vii---specjalizacje)


# Cele studiów inżynierskich

- kształtowanie intuicji związanej z obiektami teoretycznymi: na przykład poprzez związanie ich z intuicją przestrzenną, ich zobrazowaniem przykładami, zastosowaniami. Ułatwi to zrozumienie pojęć, uchwycenie współzależności między nimi oraz ich efektywne zapamiętywanie.
- kształtowanie umiejętności znajdowania rozwiązań problemów zdefiniowanych modelami matematycznymi za pomocą modeli obliczeniowych w postaci programów komputerowych.
- kształtowanie kultury współpracy wedle zasady: pisać kod w taki sposób, aby osoba go czytająca włożyła tyle wysiłku w jego zrozumienie ile to konieczne, ale nie więcej. Ujmując to inaczej: tworzyć kod na tyle złożony na ile to konieczne, ale nie bardziej.. 
- kształtowanie efektywnych praktyk kodowania i rozwijania projektów wedle zasady: wkładanie tyle wysiłku w rozwiązywanie problemów ile to konieczne, ale nie więcej.
- motywowanie do wytężonego wysiłku intelektualnego poprzez jasno sprecyzowaną perspektywę nabycia umiejętności rozwiązywania problemów z użyciem algorytmów sztucznej inteligencji.

# Organizacja studiów inżynierskich

- przez pierwsze dwa lata studiów student nabywa wiedzę i doświadczenie w rozwiązywaniu problemów niezbędne każdemu wykształconemu informatykowi. Zakres wiedzy i doświadczeń jest na tyle szeroki, aby każdy ze studentów mógł możliwie świadomie wybrać drogę dalszej specjalizacji, która mu najbardziej odpowiada.
- **od pierwszego semestru studenci poznają połączenia między przedmiotami a ścieżkami specjalizacyjnymi**, dzięki czemu rozumieją PO CO uczą się poszczególnych zagadnień i jak przygotowują się do przyszłej kariery
- podczas ostatniego 1.5 roku studiów student robi specjalizację (jedną lub więcej) oraz pisze pracę inżynierską. Wśród specjalizacji do wyboru:
    - **Sztuczna Inteligencja** - uczenie maszynowe, deep learning, computer vision, NLP
    - **Gaming i Grafika Komputerowa** - silniki gier, grafika 3D, game design
    - **Sieci i Systemy Rozproszone** - infrastruktura sieciowa, cloud computing, cybersecurity
    - **C++ i Programowanie Systemowe** - niskopoziomowe programowanie, systemy wbudowane, HPC
    - **Web Development** - full-stack development, frameworki webowe, DevOps
    - **Data Science** - analiza danych, wizualizacja, big data
- uatrakcyjnieniem ścieżek rozwoju mogłyby być długofalowe projekty, w których studenci brali by aktywny udział, przyczyniając się do rozwoju KIS poprzez automatyzację biurokracji, ułatwianie dydaktyki, wsparcie dla badań naukowych, na przykład: rozszerzanie funkcjonalności systemu dydaktycznego Michała Pierzchalskiego, w tym zarówno ścieżka sieciowa (rozwijanie GitHub App) lub automatyzacja pewnych czynności (uczenie maszynowe) jak np. AI recenzent, które mogłoby być częścią tego systemu; rozwijanie/ kontrybuowanie /tworzenie narzędzi do neuronauk lub szerzej do analizy sygnału.
- dodatkowym uatrakcyjnieniem byłoby zapewnienie wynagrodzenia przynajmniej tym najbardziej obiecującym studentom.
- w ramach każdego przedmiotu istnieje co najmniej jedna grupa gwiazdkowa, aby zapewnić odpowiedni poziom/ofertę lepszym lub/i zainteresowanym studentom.
- ujednolicenie systemu oceniania/robienia zadań/kolokwiów/egzaminów, np. kolokwia robimy wspólne dla wszystkich studentów danego przedmiotu. Wyjątkiem mogą być grupy gwiazdkowe, które rządziłyby się własnymi prawami. Podobnie reguły by obowiązywały dla zadań/projektów zaliczeniowych. Miałoby to poprawić przejrzystość i sprawiedliwość oceniania.
- dążenie do zwiększenia poziomu kształcenia (stąd też niezbędna jest zmiana sylabusów) oraz wymagań stawianych studentom. Pozwoli nam to uzyskać renomę oraz docelowo pozyskać najlepszych studentów, których moglibyśmy wciągnąć w pracę naukową.

# Graf zależności

Program studiów został zaprojektowany z uwzględnieniem **grafu zależności między zagadnieniami i przedmiotami**. Graf ten zapewnia, że:
- **Studenci nie uczą się zagadnień, których nie są w stanie zrozumieć** z powodu braku podstaw
- **Kolejność zagadnień w programie jest logiczna**: np. indukcja matematyczna (sem. 1) przed rekurencją (sem. 2)
- **Zależności między przedmiotami są jawne**: każdy przedmiot wymienia wymagane wcześniejsze zagadnienia

Szczegółowy graf zależności dostępny jest w pliku [`graf_zaleznosci.json`](graf_zaleznosci.json). Graf zawiera:
- **Pojęcia (concepts)**: poszczególne zagadnienia z przypisaniem do przedmiotów i semestrów
- **Zależności**: jakie pojęcia są wymagane przed nauką danego pojęcia
- **Kursy (courses)**: przedmioty z ich zależnościami
- **Specjalizacje (specializations)**: ścieżki kariery z kluczowymi pojęciami

**Przykłady kluczowych zależności:**
- `Indukcja matematyczna` (sem. 1) → `Rekurencja` (sem. 2) → `Algorytmy rekurencyjne` (sem. 2)
- `Wektory` (sem. 1) → `Macierze` (sem. 2) → `Uczenie maszynowe` (sem. 2+)
- `Pochodne` (sem. 1) → `Gradient` (sem. 2) → `Optymalizacja` (sem. 2) → `ML/AI` (sem. 3+)
- `Drzewa binarne` (sem. 2) → `DOM w JavaScript` (sem. 2)

# Ścieżki specjalizacyjne

Od pierwszego semestru studenci są informowani o połączeniach między przedmiotami a przyszłymi specjalizacjami:

## Sztuczna Inteligencja
**PO CO uczę się tego?** Aby budować systemy AI/ML rozwiązujące rzeczywiste problemy.

**Kluczowe przedmioty podstawowe:**
- Algebra liniowa I i II (wektory, macierze - reprezentacja danych i modeli)
- Analiza matematyczna II (gradient, optymalizacja - trenowanie modeli)
- Prawdopodobieństwo i statystyka (modelowanie niepewności)
- Python dla AI (praktyczne narzędzia ML)

**Przedmioty specjalizacyjne:** Machine Learning, Deep Learning, Computer Vision, NLP, Reinforcement Learning

## Gaming i Grafika Komputerowa
**PO CO uczę się tego?** Aby tworzyć gry i aplikacje 3D.

**Kluczowe przedmioty podstawowe:**
- Algebra liniowa I i II (transformacje 3D, wektory)
- Programowanie obiektowe (architektura silników)
- Grafika komputerowa (rendering, shaders)

**Przedmioty specjalizacyjne:** Unity/Unreal Engine, Grafika 3D zaawansowana, Fizyka w grach, Game Design, VR/AR

## Sieci i Systemy Rozproszone
**PO CO uczę się tego?** Aby budować infrastrukturę internetową i systemy skalowalne.

**Kluczowe przedmioty podstawowe:**
- Matematyka dyskretna (teoria grafów - routing)
- Wstęp do systemu Unix (administracja)
- Sieci komputerowe (protokoły, TCP/IP)

**Przedmioty specjalizacyjne:** Cloud Computing, Cybersecurity, Systemy rozproszone, DevOps, Kubernetes

## C++ i Programowanie Systemowe
**PO CO uczę się tego?** Aby pisać wydajny kod niskopoziomowy dla systemów krytycznych.

**Kluczowe przedmioty podstawowe:**
- Programowanie proceduralne (C, wskaźniki)
- Programowanie obiektowe (C++, STL)
- Wstęp do algorytmów (struktury danych)

**Przedmioty specjalizacyjne:** Zaawansowany C++, Systemy operacyjne, Kompilatory, Embedded systems, HPC

## Web Development
**PO CO uczę się tego?** Aby tworzyć nowoczesne aplikacje webowe.

**Kluczowe przedmioty podstawowe:**
- Wstęp do HTML/CSS/JavaScript
- Bazy danych (backend)
- Programowanie obiektowe (architektura aplikacji)

**Przedmioty specjalizacyjne:** React/Angular/Vue, Node.js, REST APIs, GraphQL, DevOps, Microservices

## Data Science
**PO CO uczę się tego?** Aby analizować dane i wyciągać z nich wnioski.

**Kluczowe przedmioty podstawowe:**
- Prawdopodobieństwo i statystyka (testy, modelowanie)
- Algebra liniowa (operacje na danych)
- Python dla AI (Pandas, NumPy, Matplotlib)

**Przedmioty specjalizacyjne:** Advanced Statistics, Big Data, Wizualizacja danych, Time Series, Causal Inference

# Kalendarz

## Semestr I

Wszystkie poniższe przedmioty są obowiązkowe.

- `Wstęp do matematyki i informatyki`. Patrz [tutaj](https://github.com/IS-UMK/sylabusy/blob/master/wst%C4%99p_do_matematyki_i_informatyki.md). Obejmuje podstawowe pojęcia matematyczne i informatyczne niezbędne każdemu informatykowi.
- `Wstęp do systemu Unix`. Patrz [tutaj](https://github.com/IS-UMK/sylabusy/blob/master/wst%C4%99p_do_systemu_unix.md). Kurs ten ma sprawić, aby student swobodnie się czuł i poruszał w środowisku Unix. W szczególności pozna podstawową strukturę systemu,  nauczy się terminala (w tym różnych komend oraz pisania prostych skryptów. W skrócie pozna wszystko to, co może mu ułatwić oraz usprawnić pracę nad projektami.
- `Wstęp do programowania`. Patrz [tutaj](https://github.com/IS-UMK/sylabusy/blob/master/wst%C4%99p_do_programowania.md). Kurs koncentruje się na przygotowaniu studenta do programowania pod kątem uniwersalnych (niezależnych od konkretnego języka programowania) zasad programowania. W szczególności przygotowania środowiska pracy (w tym git, Github, dobór edytora/ide), zasad dobrego programowania, zasad testowania, umiejętności recenzowania z użyciem Githuba, pracy w grupie oraz umiejętności zaplanowania realizacji projektu (np. zasada "od ogółu od szczegółu"). Ponadto przedmiot wprowadza studenta w temat dobóru narzędzi ułatwiający utrzymanie kodu na przykładzie dwóch języków `c` (kompilowany), `python` (skryptowy): sztuczna inteligencja (generowanie kodu, testów, ocena kodu) oraz klasyczne lintery, formattery. Może również zostać omówiony system GitHubowego CI-CD. 
- `Wstęp do algorytmów I`. Patrz [tutaj](https://github.com/IS-UMK/sylabusy/blob/master/wst%C4%99p_do_algorytm%C3%B3w.md) Przedmiot prowadzony w języku `c` mający na celu wprowadzenie studenta w świat algorytmiki. Poza praktyczną częścią w c, podczas której student będzie implementował zadania zaliczeniowe, student też poznaje metody sprawdzania poprawności działania programu (np. niezmienniki pętli) oraz podstawowe struktury danych takie jak tablice wraz z algorytmami z nimi związanymi.
- `Analiza matematyczna I`. Patrz [tutaj](https://github.com/IS-UMK/sylabusy/blob/master/analiza_matematyczna.md). Przedmiot ten wprowadza studenta w podstawowe pojęcia analizy matematycznej funkcji jednej zmiennej, które są niezbędne m.in. do zrozumienia algorytmów sztucznej inteligencji. Ponadto omawanie takie pojęcia jak supremum infimum (niezbędne dla postawienia problemu optymilizacji), ciągi, szeregi, granice.
- `Algebra liniowa I`. Patrz [tutaj](https://github.com/IS-UMK/sylabusy/blob/master/algebra_liniowa.md). Przedmiot ten dotyczy głownie pojęcia wektora w przestrzeni euklidesowej.Kładziony jest nacisk na intuicje geometryczne. W grupach gwiazdkowych możliwe jest również przestawienie podstawowych problemów uczenia maszynowego np. regresja liniowa, svm oraz wprowadzenie ogólnego pojęcia przestrzeni wektorowej.

## Semestr II

Wszystkie przedmioty obowiązkowe. Być może należy scalić `Wstęp do algorytmów I i II` w jeden kurs robiony w tym semestrze a wyrzucony z semestru I. Po pierwsze odciąża pierwszy semestr. Po drugie dzieki matematyce dyskretnej możliwe już jest omawianie rekurencyjnych struktur danych takich jak listy czy drzewa binarne.

- `Projektowy c`. Pierwsze większe projekty zaliczeniowe ok. 1000 lini kodu.
- `Wstęp do html, css, javascript`.
- `Matematyka dyskretna`. Patrz [tutaj](https://github.com/IS-UMK/sylabusy/blob/master/matematyka_dyskretna.md). Kontynuacja wstępu do matematyki i informatyki. Omawiane są bardziej złożone zagadnienia takie jak rekurencja, złożoności programów, kombinatoryka, drzewa, grafy, itp.
- `Wstęp do algorytmów II`. Patrz [tutaj](https://github.com/IS-UMK/sylabusy/blob/master/wst%C4%99p_do_algorytm%C3%B3w.md) . Wprowadzane są bardziej złożone stuktury danych takie jak listy, drzewa binarne i algorytmy z nimi związane. Do implementacji może zostać użyty  `c++` (zamiast czystego `c`), który jest dużo bardziej naturalny dla struktur danych (np. naturalne encapsulation poprzez `class` i `struct`).
- `Analiza matematyczna II`. Patrz [tutaj](https://github.com/IS-UMK/sylabusy/blob/master/analiza_matematyczna.md). Omawiany jest rachunek funkcji wielu zmiennych oraz zastosowania np. w uczeniu maszynowym np. spadek gradientowy. Pojawia się też pojęcie miary, w tym miara Lebesgue'a.
- `Algebra liniowa II`. Patrz [tutaj](https://github.com/IS-UMK/sylabusy/blob/master/algebra_liniowa.md) Omawiane są macierze. Jako zastosowania przedstawiany jest np. model feedforward. Ponadto pojawia się pojęcie tensora. Możliwość skorzystania np. pytorch dla praktyki w operawaniu na tensorach.

`Wstęp do html, css, javascript` mógłby pojawić się dopiero na 2 roku. Jest to uzasadnione z perspektywy programowej, gdyż dla pełnego zrozumienia, jak działa `js`, potrzebne są takie pojęcia jak event loop, a dla zrozumienia czym jest DOM ogólne drzewo - a te pojęcia dopiero są usystematyzowane na 2 roku). Kolejnym argumentem za może być to, że na MIMUW te zagadnienia też pojawiają się dopiero na 4 semestrze.


## Semestr III

**Cel:** Programowanie obiektowe, bazy danych, pierwsze kroki w specjalizacjach. Student może rozpocząć naukę zaawansowanych technologii zgodnych z wybraną ścieżką.

Przedmioty obowiązkowe:

- `Programowanie obiektowe (C++ lub Java)` (6 ECTS). Patrz [tutaj](programowanie_obiektowe.md). OOP, klasy, dziedziczenie, polimorfizm, wzorce projektowe, SOLID, STL/Collections.
  - **Zależności:** Wstęp do algorytmów II, znajomość C
  - **Połączenie ze specjalizacjami:** **Kluczowy dla C++/Systems, Gaming**, ważny dla wszystkich

- `Prawdopodobieństwo i Statystyka` (6 ECTS). Patrz [tutaj](prawdopodobienstwo_i_statystyka.md). Teoria prawdopodobieństwa, zmienne losowe, rozkłady, estymacja, testy hipotez, regresja.
  - **Zależności:** Analiza matematyczna I (całki), Algebra liniowa
  - **Połączenie ze specjalizacjami:** **Fundamentalny dla AI i Data Science**, ważny dla wszystkich (A/B testing)

- `Bazy danych` (5 ECTS). Patrz [tutaj](bazy_danych.md). Model relacyjny, SQL, normalizacja, transakcje, wprowadzenie do NoSQL.
  - **Zależności:** Teoria zbiorów, podstawy programowania
  - **Połączenie ze specjalizacjami:** Kluczowy dla Web Development, ważny dla AI (dane treningowe)

- `Systemy operacyjne` (6 ECTS). Procesy, wątki, synchronizacja, zarządzanie pamięcią, systemy plików, scheduling.
  - **Zależności:** Programowanie w C, wskaźniki, Unix
  - **Połączenie ze specjalizacjami:** **Kluczowy dla C++/Systems**, ważny dla Networking

Przedmioty do wyboru (wybór 1-2, suma 6-8 ECTS):

- `Python dla AI` (4 ECTS). Patrz [tutaj](python_dla_ai.md). NumPy, Pandas, Matplotlib, Scikit-learn, TensorFlow/PyTorch.
  - **Dla ścieżki:** AI, Data Science

- `Grafika komputerowa` (6 ECTS). Patrz [tutaj](grafika_komputerowa.md). Transformacje 3D, rendering, shaders, OpenGL.
  - **Dla ścieżki:** Gaming, Graphics

- `Sieci komputerowe` (6 ECTS). Patrz [tutaj](sieci_komputerowe.md). TCP/IP, routing, protokoły, bezpieczeństwo.
  - **Dla ścieżki:** Networking, Web Development

**Suma ECTS:** ~29-31

## Semestr IV

**Cel:** Pogłębianie specjalizacji, zaawansowane projekty. Student pracuje nad dużym projektem zespołowym (3000+ linii).

Przedmioty obowiązkowe:

- `Algorytmy i struktury danych (zaawansowane)` (6 ECTS). Algorytmy grafowe, drzewa zrównoważone, algorytmy zachłanne, programowanie dynamiczne.
  - **Zależności:** Matematyka dyskretna, Wstęp do algorytmów II

- `Inżynieria oprogramowania` (5 ECTS). Metodyki (Agile, Scrum), wzorce architektoniczne, testowanie, CI/CD, dokumentacja.
  - **Zależności:** Programowanie obiektowe, doświadczenie projektowe

- `Projekt zespołowy` (6 ECTS). Duży projekt (3000+ linii) w grupach 3-4 osobowych, zgodny z wybraną specjalizacją.
  - **Dla ścieżki:** Wszystkie

Przedmioty do wyboru (specjalizacyjne, 9-12 ECTS):

**Ścieżka AI:**
- Machine Learning (6 ECTS)
- Computer Vision (4 ECTS)
- Natural Language Processing (4 ECTS)

**Ścieżka Gaming:**
- Unity/Unreal Engine (6 ECTS)
- Fizyka w grach (4 ECTS)
- Game Design (4 ECTS)

**Ścieżka Networking:**
- Cloud Computing (6 ECTS)
- Cybersecurity (4 ECTS)
- Systemy rozproszone (4 ECTS)

**Ścieżka C++/Systems:**
- Zaawansowany C++ (6 ECTS)
- Kompilatory (4 ECTS)
- Embedded Systems (4 ECTS)

**Ścieżka Web:**
- Frameworki frontendowe (React/Angular) (6 ECTS)
- Node.js i backend (4 ECTS)
- DevOps i Kubernetes (4 ECTS)

**Ścieżka Data Science:**
- Advanced Statistics (6 ECTS)
- Big Data (4 ECTS)
- Time Series Analysis (4 ECTS)

**Suma ECTS:** ~26-29

## Semestry V-VII - Specjalizacje

**Cel:** Głęboka specjalizacja, praca inżynierska, przygotowanie do kariery lub studiów magisterskich.

Student wybiera jedną lub więcej specjalizacji i realizuje zaawansowane przedmioty specjalistyczne (po 6-8 ECTS każdy).

**Semestr V-VI:** Przedmioty specjalizacyjne (po 4-5 przedmiotów, ~24-28 ECTS/sem)

**Semestr VII:** Praca inżynierska (15 ECTS) + przedmioty specjalizacyjne (10-15 ECTS)

### Przykładowe przedmioty zaawansowane

**AI/ML:**
- Deep Learning zaawansowany
- Reinforcement Learning
- Generative AI
- MLOps
- AI Ethics

**Gaming:**
- Advanced Graphics
- VR/AR
- Procedural Generation
- Multiplayer Networking
- AI w grach

**Networking/Cloud:**
- Kubernetes i orkiestracja
- Network Security Advanced
- Distributed Systems
- Site Reliability Engineering

**C++/Systems:**
- High Performance Computing
- Real-time Systems
- Operating Systems Design
- Hardware-Software Interface

**Web/Full-stack:**
- Microservices Architecture
- GraphQL
- Progressive Web Apps
- Mobile Development (React Native)

**Data Science:**
- Causal Inference
- Bayesian Methods
- Neural Networks for Time Series
- Interpretable ML

---

# Program studiów - szczegóły semestrów

Poniżej przedstawiono szczegółowy program studiów oparty na oficjalnych opisach przedmiotów.

## Semestr I (22 ECTS)

Wszystkie przedmioty obowiązkowe.

| Przedmiot | ECTS | Opis |
|-----------|------|------|
| [Algebra liniowa I](algebra_liniowa_1.md) | 5 | Wektory, liniowa niezależność, iloczyn skalarny, logika, zbiory, relacje, indukcja matematyczna |
| [Analiza matematyczna I](analiza_matematyczna_1.md) | 6 | Funkcje elementarne, granice, ciągi, różniczkowanie, całkowanie |
| [Programowanie proceduralne](programowanie_proceduralne.md) | 5 | Podstawy programowania w języku C |
| [Wstęp do systemu UNIX](unix.md) | 3 | Podstawy pracy w systemie Unix/Linux, bash |
| [Wprowadzenie do studiowania](wprowadzenie_do_studiowania.md) | 1 | Organizacja studiów |
| [Język angielski I](jezyk_angielski_1.md) | 2 | Język angielski dla nauk technicznych |

## Semestr II (21 ECTS)

Wszystkie przedmioty obowiązkowe.

| Przedmiot | ECTS | Opis |
|-----------|------|------|
| [Matematyka dyskretna](matematyka_dyskretna.md) | 6 | Teoria liczb, teoria grafów, kombinatoryka, rekurencja |
| [Programowanie obiektowe I](programowanie_obiektowe_1.md) | 6 | Wprowadzenie do OOP (C++/Java) |
| [Fizyka dla informatyków I](fizyka_1.md) | 4 | Podstawy fizyki |
| [Technika komputerowa](technika_komputerowa.md) | 3 | Architektura komputera |
| [Język angielski II](jezyk_angielski_2.md) | 2 | Kontynuacja języka angielskiego |

## Semestr III (40 ECTS)

Wszystkie przedmioty obowiązkowe.

| Przedmiot | ECTS | Opis |
|-----------|------|------|
| [Algorytmy i struktury danych](algorytmy_i_struktury_danych.md) | 6 | Listy, drzewa, grafy, sortowanie |
| [Bazy danych I](bazy_danych_1.md) | 5 | Model relacyjny, SQL, normalizacja |
| [Programowanie obiektowe II](programowanie_obiektowe_2.md) | 6 | Zaawansowane OOP, wzorce projektowe |
| [Sieci komputerowe](sieci_komputerowe.md) | 6 | TCP/IP, routing, protokoły |
| [Systemy operacyjne](systemy_operacyjne.md) | 6 | Procesy, synchronizacja, zarządzanie pamięcią |
| [Technika cyfrowa](technika_cyfrowa.md) | 4 | Układy logiczne, automaty |
| [Metody numeryczne](metody_numeryczne.md) | 4 | Aproksymacja, interpolacja, całki numeryczne |
| [Podstawy elektroniki](podstawy_elektroniki.md) | 3 | Podstawy elektroniki |
| [Języki programowania](jezyki_programowania.md) | 4 | Paradygmaty programowania |

## Semestr IV (23 ECTS)

Wszystkie przedmioty obowiązkowe.

| Przedmiot | ECTS | Opis |
|-----------|------|------|
| [Bazy danych II](bazy_danych_2.md) | 4 | NoSQL, bazy rozproszone |
| [Inżynieria oprogramowania](inzynieria_oprogramowania.md) | 5 | Metodyki, Agile, CI/CD, testowanie |
| [Pracownia programowania zespołowego](programowanie_zespolowe.md) | 6 | Projekty zespołowe, Git, code review |
| [Mikroprocesory](mikroprocesory.md) | 4 | Architektura mikroprocesora, assembler |
| [Przetwarzanie sygnałów](przetwarzanie_sygnalow.md) | 4 | Transformata Fouriera, filtracja |

## Semestr V (20 ECTS)

Przedmioty obowiązkowe i wybieralne.

| Przedmiot | ECTS | Typ | Opis |
|-----------|------|-----|------|
| [Pracownia inżynierska I](pracownia_inzynierska_1.md) | 6 | Obowiązkowy | Projekt inżynierski |
| [Ochrona praw autorskich](ochrona_praw_autorskich.md) | 2 | Obowiązkowy | Prawo autorskie |
| [Sztuczna inteligencja](sztuczna_inteligencja.md) | 6 | Wybieralny | ML, sieci neuronowe |
| [Wstęp do data mining](data_mining.md) | 4 | Wybieralny | Eksploracja danych, klasyfikacja |
| [Serwisy sieciowe I](serwisy_sieciowe_1.md) | 6 | Wybieralny | Web development, HTTP, HTML/CSS |

## Semestr VI (14 ECTS)

Przedmioty obowiązkowe i wybieralne.

| Przedmiot | ECTS | Typ | Opis |
|-----------|------|-----|------|
| [Pracownia inżynierska II](pracownia_inzynierska_2.md) | 6 | Obowiązkowy | Kontynuacja projektu |
| [Podstawy przedsiębiorczości](podstawy_przedsiebiorczosci.md) | 2 | Obowiązkowy | Przedsiębiorczość |
| [Serwisy sieciowe II](serwisy_sieciowe_2.md) | 6 | Wybieralny | Frameworki webowe, REST API |

## Semestr VII (6 ECTS)

| Przedmiot | ECTS | Opis |
|-----------|------|------|
| [Seminarium inżynierskie](seminarium_inzynierskie.md) | 2 | Seminarium dyplomowe |
| [Praktyka inżynierska](praktyka_inzynierska.md) | 4 | Praktyka zawodowa (4 tygodnie) |

**Praca inżynierska:** 15 ECTS

---

## Ścieżki specjalizacyjne (zaktualizowane)

Program studiów oferuje 5 głównych ścieżek specjalizacyjnych:

### 1. Sztuczna Inteligencja i Data Science
**Kluczowe kursy:**
- Sztuczna inteligencja (sem. 5)
- Wstęp do data mining (sem. 5)
- Matematyka dyskretna, Algorytmy i struktury danych (fundamenty)

**Perspektywy:** AI engineer, Data Scientist, ML engineer

### 2. Web Development i Sieci
**Kluczowe kursy:**
- Opracowywanie serwisów sieciowych I i II (sem. 5-6)
- Sieci komputerowe (sem. 3)
- Bazy danych I i II (sem. 3-4)

**Perspektywy:** Full-stack developer, Backend developer, Network engineer

### 3. Systemy Wbudowane i Mikroprocesory
**Kluczowe kursy:**
- Mikroprocesory i technika mikroprocesorowa (sem. 4)
- Technika cyfrowa (sem. 3)
- Podstawy elektroniki (sem. 3)

**Perspektywy:** Embedded systems developer, Hardware engineer

### 4. Inżynieria Oprogramowania
**Kluczowe kursy:**
- Inżynieria oprogramowania (sem. 4)
- Pracownia programowania zespołowego (sem. 4)
- Języki programowania (sem. 3)

**Perspektywy:** Software engineer, DevOps engineer, Architect

### 5. Przetwarzanie Sygnałów
**Kluczowe kursy:**
- Podstawy i algorytmy przetwarzania sygnałów (sem. 4)
- Metody numeryczne (sem. 3)
- Fizyka dla informatyków (sem. 2)

**Perspektywy:** Signal processing engineer, Audio/Video engineer

