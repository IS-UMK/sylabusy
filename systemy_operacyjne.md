## Systemy Operacyjne

Kurs wprowadza fundamentalne koncepcje projektowania i implementacji systemów operacyjnych. Student poznaje zarówno teoretyczne podstawy, jak i praktyczne aspekty implementacji.

### Tematyka kursu:

1. **Wprowadzenie do systemów operacyjnych**
   - Rola i funkcje systemu operacyjnego
   - Historia: od batch processing do wielozadaniowości
   - Typy systemów operacyjnych
   - Architektura: monolityczna vs mikrokernel vs hybrydowa
   - Wywołania systemowe (system calls)

2. **Procesy i wątki**
   - Proces: definicja, cykl życia, PCB (Process Control Block)
   - Tworzenie procesów: fork(), exec()
   - Kontekst procesu i przełączanie kontekstu
   - Wątki: różnica między procesem a wątkiem
   - Implementacja wątków (user-level vs kernel-level)
   - Modele wielowątkowości
   - Przykłady: POSIX threads (pthreads)

3. **Szeregowanie procesów (Scheduling)**
   - Cele algorytmów szeregowania
   - Metryki: czas odpowiedzi, przepustowość, fairness
   - Algorytmy:
     - FCFS (First-Come, First-Served)
     - SJF (Shortest Job First)
     - Round Robin
     - Priority Scheduling
     - Multilevel Queue
     - Completely Fair Scheduler (CFS) w Linuxie
   - Szeregowanie wieloprocesorowe
   - Szeregowanie w czasie rzeczywistym

4. **Synchronizacja i współbieżność**
   - Problem sekcji krytycznej
   - Race conditions i deadlocki
   - Mechanizmy synchronizacji:
     - Semafory (Dijkstra)
     - Muteksy i locki
     - Zmienne warunkowe (condition variables)
     - Monitory
   - Klasyczne problemy synchronizacji:
     - Producer-Consumer
     - Readers-Writers
     - Dining Philosophers
   - Wykrywanie i unikanie deadlocków

5. **Zarządzanie pamięcią**
   - Przestrzeń adresowa procesu
   - Partycjonowanie pamięci
   - Paging (stronicowanie):
     - Page tables
     - TLB (Translation Lookaside Buffer)
     - Page faults
   - Segmentacja
   - Pamięć wirtualna:
     - Demand paging
     - Page replacement algorithms: FIFO, LRU, Clock
     - Thrashing i working set
   - Alokacja pamięci:
     - malloc/free implementation
     - Buddy allocator
     - Slab allocator

6. **Systemy plików**
   - Abstrakcja pliku i katalogu
   - Implementacja systemu plików:
     - inode
     - Directory structure
     - Block allocation: contiguous, linked, indexed
   - Przykłady: ext4, NTFS, FAT
   - Buforowanie i cache
   - Dziennikowanie (journaling)
   - Virtual File System (VFS)
   - Uprawnienia i bezpieczeństwo

7. **Wejście/wyjście (I/O)**
   - Urządzenia I/O
   - Device drivers
   - I/O buffering
   - DMA (Direct Memory Access)
   - Asynchroniczne I/O
   - Spooling

8. **Bezpieczeństwo i ochrona**
   - Uwierzytelnianie i autoryzacja
   - Access Control Lists (ACL)
   - Capability-based security
   - Izolacja procesów
   - Ataki: buffer overflow, race conditions
   - Sandboxing

9. **Wirtualizacja**
   - Typy wirtualizacji
   - Hypervisory: Type 1 vs Type 2
   - Paravirtualization
   - Kontenery vs VM (Docker, LXC)
   - Przykład: KVM, VirtualBox

10. **Praktyczne aspekty**
    - Programowanie w kernel space vs user space
    - Debugging kernel code
    - Budowanie własnego kernela
    - Kernel modules w Linuxie
    - Analiza wydajności (profiling)

### Projekt praktyczny:

Studenci implementują elementy systemu operacyjnego:

**Opcja 1: Mini OS**
- Prosty kernel bootujący się (bootloader)
- Obsługa przerwań
- Prosty scheduler
- Zarządzanie pamięcią (podstawowe)
- Możliwe platformy: x86, ARM, RISC-V w emulatorze (QEMU)

**Opcja 2: Kernel module**
- Moduł kernela Linuxa
- System plików w user space (FUSE)
- Device driver
- Scheduler plugin

**Opcja 3: Synchronizacja**
- Implementacja semaforów/mutexów od zera
- Rozwiązanie klasycznych problemów synchronizacji
- Multi-threaded aplikacja z zaawansowaną synchronizacją

### Zależności:

**Wymagane wcześniejsze zagadnienia:**
- Programowanie w C (wskaźniki, pamięć dynamiczna)
- Wstęp do systemu Unix (podstawy pracy w terminalu)
- Architektura komputerów (opcjonalne, ale pomocne)
- Podstawy algorytmów i struktur danych

**Przygotowuje do:**
- Programowania systemowego
- Embedded systems
- Kernel development
- Cloud infrastructure (zrozumienie jak działają kontenery)
- Cybersecurity (rozumienie ataków na poziomie OS)

### Cele edukacyjne:

- Zrozumienie roli i struktury systemu operacyjnego
- Umiejętność programowania wielowątkowego z synchronizacją
- Znajomość algorytmów szeregowania i zarządzania zasobami
- Zrozumienie pamięci wirtualnej i stronicowania
- Praktyczna znajomość systemów plików
- Umiejętność debugowania problemów związanych z OS
- Podstawy kernel programming

### Połączenie ze specjalizacjami:

- **C++/Programowanie Systemowe**: Fundamentalny przedmiot
- **Embedded Systems**: Zrozumienie RTOS
- **Networking**: Jak OS obsługuje sieć (sockets, TCP/IP stack)
- **Cybersecurity**: Wektory ataków na poziomie OS
- **Cloud/DevOps**: Kontenery, wirtualizacja, resource management

### Laboratorium:

- Programowanie multi-threaded (pthreads)
- Implementacja algorytmów szeregowania (symulacja)
- Synchronizacja: rozwiązywanie producer-consumer
- Analiza page replacement algorithms
- Budowanie prostego systemu plików
- Tworzenie kernel module w Linuxie
- Debugging z GDB (procesy, wątki)

### Narzędzia:

- Linux kernel source code (do analizy)
- QEMU (emulator)
- GDB dla kernel debugging
- Valgrind (memory leaks, race conditions)
- strace, ltrace (system calls tracing)
- perf (profiling)

Kurs przygotowuje do pracy na niskim poziomie abstrakcji i jest fundamentem dla każdego, kto chce rozumieć JAK NAPRAWDĘ działa komputer.
