## Sieci Komputerowe

Kurs wprowadza podstawowe koncepcje sieci komputerowych, protokołów komunikacyjnych oraz praktycznych aspektów budowy i zarządzania sieciami. Szczególny nacisk kładziony jest na model TCP/IP i protokoły internetowe.

### Tematyka kursu:

1. **Wprowadzenie do sieci**
   - Historia i ewolucja sieci komputerowych
   - Modele warstwowe: OSI i TCP/IP
   - Topologie sieci (gwiazda, magistrala, pierścień, mesh)
   - Typy sieci: LAN, WAN, MAN, PAN
   - Media transmisyjne (kable, WiFi, fiber)

2. **Warstwa fizyczna i łącza danych**
   - Kodowanie sygnału
   - Ethernet i standardy IEEE 802
   - MAC addressing
   - Switching i VLANy
   - Wykrywanie i korekcja błędów
   - ARP (Address Resolution Protocol)

3. **Warstwa sieciowa (IP)**
   - Adresowanie IPv4 i IPv6
   - Podsieci i maski sieciowe (CIDR)
   - Routing: statyczny i dynamiczny
   - Protokoły routingu: RIP, OSPF, BGP
   - ICMP i narzędzia diagnostyczne (ping, traceroute)
   - NAT i PAT
   - Quality of Service (QoS)

4. **Warstwa transportowa**
   - TCP: niezawodna transmisja
     - Three-way handshake
     - Flow control i congestion control
     - Okna przesuwne
   - UDP: szybka transmisja bez gwarancji
   - Porty i sockety
   - Porównanie TCP vs UDP - kiedy co używać

5. **Warstwa aplikacji**
   - HTTP/HTTPS i web
   - DNS (Domain Name System)
   - SMTP, POP3, IMAP (poczta elektroniczna)
   - FTP i SFTP
   - SSH i bezpieczny dostęp zdalny
   - WebSockets
   - REST APIs

6. **Bezpieczeństwo sieci**
   - Zagrożenia i ataki (DDoS, Man-in-the-Middle, Spoofing)
   - Firewalle i ACLs
   - VPN (Virtual Private Networks)
   - Szyfrowanie: SSL/TLS
   - IPSec
   - Bezpieczne protokoły (HTTPS, SSH, SFTP)

7. **Sieci bezprzewodowe**
   - WiFi (802.11 a/b/g/n/ac/ax)
   - Bezpieczeństwo WiFi (WPA2, WPA3)
   - Bluetooth i inne technologie PAN
   - Cellular networks (4G, 5G)

8. **Praktyczne aspekty**
   - Konfiguracja routerów i switchów
   - Wireshark - analiza ruchu sieciowego
   - Programowanie sieciowe (sockets w C/Python)
   - Docker networking
   - Virtualization i Software-Defined Networking (SDN)
   - Cloud networking (AWS, Azure, GCP)

9. **Projekt praktyczny**
   - Zaprojektowanie i implementacja prostej sieci
   - Konfiguracja usług (DNS, DHCP, Web server)
   - Implementacja prostego protokołu komunikacyjnego
   - Lub: aplikacja klient-serwer z protokołem własnym

### Zależności:

**Wymagane wcześniejsze zagadnienia:**
- Teoria grafów (routing jako problem znajdowania ścieżek)
- Podstawy programowania (sockety, I/O)
- System Unix/Linux (konfiguracja, skrypty)
- Podstawy algorytmów (algorytmy grafowe dla routingu)

**Przygotowuje do:**
- Systemów rozproszonych
- Cloud computing
- Cybersecurity
- IoT (Internet of Things)
- DevOps i Site Reliability Engineering

### Cele edukacyjne:

- Zrozumienie modeli warstwowych i zasad komunikacji sieciowej
- Praktyczna znajomość protokołów TCP/IP
- Umiejętność diagnozowania problemów sieciowych
- Znajomość podstaw bezpieczeństwa sieciowego
- Umiejętność konfiguracji podstawowych usług sieciowych
- Programowanie aplikacji sieciowych
- Zrozumienie routingu i przełączania

### Połączenie ze specjalizacjami:

- **Networking**: Podstawowy kurs specjalizacji
- **Web Development**: Zrozumienie jak działają aplikacje webowe
- **Cybersecurity**: Fundament dla bezpieczeństwa
- **Cloud Computing**: Podstawa infrastruktury chmurowej
- **IoT**: Komunikacja między urządzeniami
- **Gaming**: Gry multiplayer i sieciowe

### Laboratorium:

Praktyczne zajęcia obejmują:
- Konfiguracja sieci w środowisku wirtualnym (GNS3, Packet Tracer)
- Analiza ruchu sieciowego z Wireshark
- Programowanie socketów w C/Python
- Konfiguracja serwerów (Apache, nginx, DNS, DHCP)
- Budowa prostej aplikacji klient-serwer
- Testy penetracyjne i security audits

Kurs przygotowuje do pracy jako network administrator, DevOps engineer lub specjalista ds. bezpieczeństwa sieciowego.
