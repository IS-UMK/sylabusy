## Grafika Komputerowa i Wizualizacja

Kurs wprowadza podstawowe i zaawansowane zagadnienia grafiki komputerowej, ze szczególnym uwzględnieniem matematycznych podstaw transformacji 3D, renderingu i wizualizacji.

### Tematyka kursu:

1. **Podstawy matematyczne grafiki**
   - Wektory i operacje wektorowe w R² i R³
   - Macierze transformacji 2D i 3D
   - Przestrzenie współrzędnych
   - Współrzędne jednorodne
   - Kwaterniony (zaawansowane: rotacje bez gimbal lock)

2. **Transformacje geometryczne**
   - Translacja, rotacja, skalowanie
   - Kompozycja transformacji
   - Macierze widoku (view matrix)
   - Macierze projekcji (perspektywiczna, ortogonalna)
   - Pipeline graficzny: Model → View → Projection

3. **Reprezentacja obiektów 2D i 3D**
   - Prymitywy geometryczne (punkty, linie, trójkąty)
   - Mesh'e i reprezentacja powierzchni
   - Krzywe Béziera i splajny
   - Powierzchnie parametryczne
   - Reprezentacje objętościowe (voxels)

4. **Algorytmy rasteryzacji**
   - Algorytm Bresenhama (linie)
   - Wypełnianie wielokątów
   - Rasteryzacja trójkątów
   - Z-buffer i usuwanie niewidocznych powierzchni
   - Clipping (Cohen-Sutherland, Liang-Barsky)
   - Antyaliasing

5. **Oświetlenie i cieniowanie**
   - Modele oświetlenia: Phong, Blinn-Phong
   - Ambient, diffuse, specular
   - Cieniowanie: flat, Gouraud, Phong shading
   - Cienie: shadow mapping, ray tracing
   - Global illumination (podstawy)

6. **Teksturowanie i materiały**
   - Mapowanie tekstur (UV mapping)
   - Mipmapping i filtrowanie
   - Normal mapping i bump mapping
   - Environment mapping (refleksje)
   - Proceduralne tekstury

7. **Kolory i przestrzenie barw**
   - RGB, HSV, HSL
   - Gamma correction
   - Tone mapping i HDR
   - Zarządzanie kolorem

8. **Ray Tracing (zaawansowane)**
   - Podstawy ray tracingu
   - Przecięcia promień-obiekt
   - Odbicia i refrakcje
   - Rekursywny ray tracing
   - Path tracing (wprowadzenie)

9. **GPU i programowanie shaderów**
   - Architektura GPU
   - Pipeline graficzny w OpenGL/Vulkan/DirectX
   - Vertex shaders
   - Fragment shaders
   - Compute shaders
   - GLSL/HLSL

10. **Praktyczne zastosowania**
    - OpenGL/WebGL - podstawy
    - Rendering w czasie rzeczywistym
    - Poziomy szczegółowości (LOD)
    - Culling i optymalizacje
    - Particle systems
    - Post-processing effects

11. **Wizualizacja danych**
    - Wizualizacja danych naukowych
    - Volume rendering
    - Graficzne przedstawienie danych wysokowymiarowych
    - Interaktywne wizualizacje

### Zależności:

**Wymagane wcześniejsze zagadnienia:**
- Algebra liniowa I i II (wektory, macierze, transformacje liniowe)
- Podstawy programowania (C++ lub Python)
- Geometria analityczna
- Podstawy analizy matematycznej (dla oświetlenia i krzywych)

**Przygotowuje do:**
- Tworzenia gier komputerowych
- Symulacji i wizualizacji naukowej
- Computer Vision
- Augmented Reality / Virtual Reality
- Filmów animowanych i VFX

### Cele edukacyjne:

- Zrozumienie matematycznych podstaw transformacji 3D
- Praktyczna znajomość pipeline'u graficznego
- Umiejętność implementacji podstawowych algorytmów graficznych
- Znajomość technik renderingu i oświetlenia
- Umiejętność programowania shaderów
- Zrozumienie optymalizacji w grafice czasu rzeczywistego
- Praktyczna umiejętność tworzenia scen 3D

### Połączenie ze specjalizacjami:

- **Gaming**: Kluczowy przedmiot - silniki graficzne w grach
- **AI/Computer Vision**: Zrozumienie jak reprezentowane są obrazy
- **Wizualizacja Naukowa**: Przedstawianie wyników badań
- **VR/AR**: Fundamenty dla rzeczywistości rozszerzonej
- **Filmy i Animacja**: Rendering i efekty specjalne

### Projekt praktyczny:

Studenci wybierają jeden z projektów:
1. **Mini silnik 3D**
   - Podstawowy renderer z oświetleniem Phonga
   - Wczytywanie i wyświetlanie mesh'y
   - Kamera FPS z kontrolą myszą/klawiaturą
   
2. **Ray tracer**
   - Implementacja podstawowego ray tracera
   - Odbicia, refrakcje, cienie
   - Różne materiały i kształty
   
3. **Wizualizacja danych**
   - Interaktywna wizualizacja dużego datasetu
   - Różne widoki i projekcje
   - Filtry i animacje

4. **Shader playground**
   - Kolekcja ciekawych efektów shaderowych
   - Proceduralne tekstury
   - Post-processing

### Narzędzia i biblioteki:

- OpenGL/GLFW/GLAD
- GLM (matematyka dla OpenGL)
- WebGL (dla projektów webowych)
- Three.js lub Babylon.js
- Unity/Unreal (dla projektów z silnikami)
- Blender (modelowanie i UV mapping)

Kurs łączy teorię matematyczną z praktycznym programowaniem, przygotowując do pracy w przemyśle gier, VR/AR lub wizualizacji naukowej.
