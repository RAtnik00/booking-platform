# System Rezerwacji Zajęć z Korepetytorami

## Spis treści

1. [Opis projektu](#opis-projektu)  
2. [Technologie i biblioteki](#technologie-i-biblioteki)  
3. [Funkcjonalności](#funkcjonalności)  
4. [Instrukcja uruchomienia aplikacji](#instrukcja-uruchomienia-aplikacji)  
   - [Lokalnie (bez Dockera)](#lokalnie-bez-dockera)  
   - [Przez Docker](#przez-docker)  
5. [Architektura aplikacji (MVC)](#architektura-aplikacji-mvc)  
6. [Przykładowe dane](#przykładowe-dane)  
7. [Autorzy](#autorzy)  

---

## Opis projektu

Aplikacja umożliwia rezerwację indywidualnych zajęć z korepetytorami. Użytkownicy (studenci) mogą przeglądać listę nauczycieli, sprawdzać ich profile oraz rezerwować spotkania online. Korepetytorzy mogą zarządzać swoją dostępnością i zatwierdzać lub odrzucać rezerwacje.

Projekt stworzony został z użyciem frameworka **Django** i wzorca architektonicznego **MVC**, z wykorzystaniem **Docker** i podziałem ról użytkowników.

---

## Technologie i biblioteki

- **Python 3.12+**
- **Django** — framework backendowy oparty na MVC
- **PostgreSQL** — relacyjna baza danych
- **Docker & Docker Compose** — konteneryzacja i łatwe uruchamianie środowiska
- **HTML5 + CSS3 + Bootstrap** — stylizacja i responsywny frontend
- **Django Templates** — dynamiczne szablony HTML
- **Django Auth** — system logowania i zarządzania użytkownikami
- **Role-based Access Control** — różne widoki i akcje zależne od roli użytkownika
- **Custom Forms + Validation** — własne formularze z walidacją po stronie serwera
- **Filtrowanie danych w widokach** — filtrowanie rezerwacji po statusie
- **Panel administratora Django** — zarządzanie danymi przez admina
- **Django Messages Framework** — komunikaty systemowe (np. sukces, błąd)
- **Periodic Timer / Cron (opcjonalnie)** — automatyczne odświeżanie list (jeśli dotyczy)
- **pytest / Django TestCase (opcjonalnie)** — możliwość testowania

---

## Funkcjonalności

- ✅ Rejestracja i logowanie z wyborem roli (student / korepetytor)
- ✅ Panel użytkownika z listą rezerwacji
- ✅ Filtrowanie rezerwacji według statusu
- ✅ Profil korepetytora z opisem i szczegółami
- ✅ Formularz rezerwacji zajęć
- ✅ Potwierdzanie / odrzucanie rezerwacji przez korepetytora
- ✅ Możliwość ponownej rezerwacji spotkania
- ✅ Obsługa sesji użytkownika i ograniczenie dostępu
- ✅ Stylizacja widoków z Bootstrap
- ✅ Uruchamianie aplikacji w kontenerze Docker

---

## Instrukcja uruchomienia aplikacji

### Lokalnie (bez Dockera)

1. Zainstaluj zależności:
   ```bash
   pip install -r requirements.txt

