# Programowanie wpółbieżne

Celem przedmiotu jest rozwój głębokiego zrozumienia programowania równoległego w modelu pamięci współdzielonej – 
kluczowego w erze AI, gdzie generowanie kodu staje się trywialne, ale weryfikacja poprawności, debugowanie i optymalizacja wymagają eksperckiej wiedzy o problemach współbieżności. 
Poza niezbędną wiedzą i teorią studenci poznają rozwiązania w najnowszych standardach C++ (C++20/23/26) (np. std::jthread, std::atomic_ref) oraz nauczą się zaawansowane mechanizmów bez blokad (CAS, hazard pointers).

## **FAZA 1: FUNDAMENTY TEORETYCZNE (tygodnie 1-4) + KOLOKWIUM**

#### 1. Wprowadzenie + Prawo Amdahla
- Wątek vs proces, współbieżność vs równoległość  
- **Prawo Amdahla**.
- Visibility, cache coherence (intuicja).  
- **Memory reordering**: kompilator/CPU out-of-order.
- Uruchamianie wątków: std::jthread.
- Pierwszy data race: licznik  

#### 2. Podstawowe problemy współbieżności
- Wyścigi danych (data races): utrata aktualizacji, niespójne odczyty.
- Zakleszczenia (deadlock): warunki Coffmana, przykłady grafowe.
- Głód (starvation), żywość (liveness) vs bezpieczeństwo (safety).
- Hazardy: WAR/WAW/RAW – analiza przepływu danych.
- **False sharing** + cache line padding: std::hardware_destructive_interference_size

#### 6. **mutex** 
- motywacja: algorytm Petersona oraz Bakery algorithm  Lamporta.
- std::mutex + RAII + podstawowe problemy np. - **Contention**: dlaczego 100 wątków blokuje się na mutexie ?
- rozwiązywanie problemów przy użyciu **std::mutex**



#### 7. **CONDITION_VARIABLE** 
- motywacja: Ograniczenia mutexa, producent-konsument
- **std::condition_variable** + **unique_lock**: producer-consumer  
- **Spurious wakeups** – dlaczego `while(predicate)`?  
- **Lost signal**: notify przed wait + race condition
- rozwiązywanie problemów przy użyciu **std::conditional_variable**


#### 2. Model pamięci współdzielonej


#### 3. **Memory barriers** – fundament synchronizacji
- **Full barrier, acquire, release, relaxed** – definicje + diagramy.  
- **Happens-before relationship**, synchronization points.  
- **Przykład**: dlaczego licznik wymaga barrier?  

#### 4. Klasyczne algorytmy synchronizacji (**używające barriers**)

- Peterson's algorithm: wzajemne wykluczanie dla 2 wątków (test&set na zmiennych).
-


## **FAZA 2: NOWOCZESNE C++20/23 W PRAKTYCE (tygodnie 5-13)**

#### 5. Pierwsze wątki: **std::jthread** (C++20)
- **jthread** + **stop_token** – graceful shutdown.  
- **Pierwszy data race**: licznik (teoria → praktyka).  

#### 6. Muteksy C++20 – ewolucja Petersona
- **std::scoped_lock**, **unique_lock** – RAII (implicit barriers).  
- Thread-safe queue + **false sharing**.  

#### 7. Zakleszczenia w C++
- **std::lock** + hierarchia blokad.  
- **std::shared_mutex** reader-writer.  

#### 8. Koordynacja: **condition_variable** + **stop_token**
- Producer-consumer, **cancellation-aware wait**.  

#### 9. **C++20 synchronizatory**
- **std::barrier** + callback.  
- **std::latch**, **std::semaphore**.  

#### 10. Atomiki C++20/23 – **memory_order w akcji**
- **std::atomic_ref**, **CAS** (strong/weak).  
- **memory_order_seq_cst vs acq_rel vs relaxed** – mapowanie z Faz1.  

#### 11. Lock-free struktury
- **Treiber stack**, **Michael-Scott queue**.  
- **ABA problem**.  

#### 12. Hazard pointers + memory reclamation
- **Dangling pointers** – rozwiązanie z **atomic_ref**.  

#### 13. Thread pools + projekt
- **Work-stealing pool** + **projekt**: task scheduler (TSan clean).
