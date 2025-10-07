## Programowanie Obiektowe (C++ lub Java)

Kurs wprowadza paradygmat programowania obiektowego z wykorzystaniem języka C++ lub Java. Nacisk kładziony jest na zrozumienie zasad OOP i ich praktyczne zastosowanie w tworzeniu większych systemów.

### Tematyka kursu:

1. **Podstawy programowania obiektowego**
   - Czym jest programowanie obiektowe?
   - Klasy i obiekty
   - Enkapsulacja
   - Abstrakcja
   - Dziedziczenie
   - Polimorfizm

2. **Klasy i obiekty (C++)**
   - Definicja klasy: pola i metody
   - Konstruktory i destruktory
   - Inicjalizacja obiektów
   - `this` pointer
   - Const methods i const objects
   - Static members
   - Friend functions i classes

3. **Dziedziczenie**
   - Hierarchie klas
   - Dziedziczenie publiczne, chronione, prywatne
   - Konstruktory i destruktory w hierarchii
   - Funkcje wirtualne
   - Klasy abstrakcyjne i interfejsy
   - Wielodziedziczenie (C++) i jego pułapki
   - Virtual inheritance

4. **Polimorfizm**
   - Wiązanie statyczne vs dynamiczne
   - Virtual functions i virtual table
   - Override i final (C++11)
   - Pure virtual functions
   - Runtime Type Information (RTTI)
   - dynamic_cast, static_cast

5. **Przeciążanie operatorów (C++)**
   - Operator overloading
   - Przeciążanie operatorów arytmetycznych
   - Przeciążanie operatorów porównania
   - Przeciążanie << i >> dla I/O
   - Zasady dobrego przeciążania

6. **Szablony (C++) / Generics (Java)**
   - Function templates
   - Class templates
   - Template specialization
   - Variadic templates (C++11)
   - Type traits i metaprogramming (zaawansowane)
   - STL i kontenery generyczne

7. **Standard Template Library (C++)**
   - Kontenery: vector, list, deque, map, set, unordered_map
   - Iteratory
   - Algorytmy: sort, find, transform, accumulate
   - Function objects i lambdy
   - Smart pointers: unique_ptr, shared_ptr, weak_ptr

8. **Zarządzanie pamięcią**
   - Stack vs Heap
   - new i delete
   - Resource Acquisition Is Initialization (RAII)
   - Move semantics (C++11)
   - Perfect forwarding
   - Copy elision i RVO

9. **Wyjątki**
   - Try-catch-throw
   - Hierarchia wyjątków
   - Exception safety guarantees
   - Kiedy używać wyjątków?
   - noexcept (C++11)

10. **Wzorce projektowe (Design Patterns)**
    - Creational: Singleton, Factory, Builder
    - Structural: Adapter, Decorator, Facade
    - Behavioral: Observer, Strategy, Iterator
    - Kiedy i jak stosować wzorce

11. **Zasady projektowania**
    - SOLID principles:
      - Single Responsibility Principle
      - Open-Closed Principle
      - Liskov Substitution Principle
      - Interface Segregation Principle
      - Dependency Inversion Principle
    - DRY (Don't Repeat Yourself)
    - KISS (Keep It Simple, Stupid)

12. **Nowoczesny C++ (C++11/14/17/20)**
    - Auto i type inference
    - Range-based for loops
    - Lambdy i closures
    - Move semantics i rvalue references
    - Smart pointers
    - Concepts (C++20)
    - Modules (C++20)

### Zależności:

**Wymagane wcześniejsze zagadnienia:**
- Programowanie w C (wskaźniki, struktury, pamięć dynamiczna)
- Podstawy algorytmów i struktur danych
- Git i dobre praktyki programowania

**Przygotowuje do:**
- Zaawansowanych projektów w C++
- Silników gier (Unreal Engine)
- Systemów wysokowydajnych
- Embedded systems
- Projektów open-source

### Cele edukacyjne:

- Głębokie zrozumienie paradygmatu OOP
- Praktyczna znajomość C++ lub Java
- Umiejętność projektowania hierarchii klas
- Znajomość wzorców projektowych i zasad SOLID
- Efektywne zarządzanie pamięcią w C++
- Znajomość STL i umiejętność jej wykorzystania
- Pisanie bezpiecznego i wydajnego kodu OOP

### Połączenie ze specjalizacjami:

- **C++ i Programowanie Systemowe**: Podstawowy kurs specjalizacji
- **Gaming**: Kluczowe dla Unreal Engine i innych silników C++
- **Embedded Systems**: OOP w systemach wbudowanych
- **High-Performance Computing**: Efektywny C++
- **Open Source**: Większość dużych projektów C++

### Projekt praktyczny:

Studenci realizują większy projekt (2000-3000 linii kodu):

**Opcja 1: System zarządzania**
- Biblioteka, sklep, rezerwacje
- Hierarchia obiektów (użytkownicy, przedmioty)
- Perzystencja danych (pliki lub baza)
- GUI lub CLI

**Opcja 2: Gra**
- Prosta gra (roguelike, tower defense)
- Hierarchia obiektów gry (entities, items, enemies)
- Game loop i zarządzanie stanem
- Collision detection

**Opcja 3: Silnik lub framework**
- Mini silnik gry 2D
- Framework do testowania
- Parser lub interpreter
- Data structure library

**Wymagania projektu:**
- Zastosowanie dziedziczenia i polimorfizmu
- Wykorzystanie STL
- Co najmniej 3 wzorce projektowe
- Testy jednostkowe
- Dokumentacja (Doxygen)
- Code review na GitHub

### Narzędzia:

- Kompilatory: GCC, Clang, MSVC
- Build systems: CMake, Make
- IDE: CLion, Visual Studio, VS Code
- Debuggers: GDB, LLDB, Visual Studio Debugger
- Static analysis: clang-tidy, cppcheck
- Testing: Google Test, Catch2
- Documentation: Doxygen

Kurs przygotowuje do profesjonalnego programowania w C++/Java i pracy nad złożonymi projektami wymagającymi dobrego projektu architektury.
