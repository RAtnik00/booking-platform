# System Rezerwacji Zajęć z Korepetytorami

## Spis treści

1. [Opis projektu](#opis-projektu)  
2. [Funkcjonalności](#funkcjonalności)  
3. [Instrukcja uruchomienia aplikacji](#instrukcja-uruchomienia-aplikacji)  
   - [Lokalnie (bez Dockera)](#lokalnie-bez-dockera)  
   - [Przez Docker](#przez-docker)  
4. [Struktura aplikacji (MVC)](#struktura-aplikacji-mvc)  
5. [Przykładowe dane](#przykładowe-dane)  

---

## Opis projektu

Aplikacja umożliwia studentom rezerwację zajęć z wybranymi korepetytorami. System pozwala na przeglądanie listy dostępnych nauczycieli, przegląd profili, a także rezerwowanie i zarządzanie spotkaniami. Została zaimplementowana autoryzacja użytkowników z wyborem roli: student lub korepetytor.

Projekt został zrealizowany w technologii Django (Python) z użyciem wzorca architektonicznego **MVC**.

---

## Funkcjonalności

- Rejestracja i logowanie użytkowników z wyborem roli (student / korepetytor)
- Przeglądanie listy dostępnych korepetytorów
- Strona profilu korepetytora (widok szczegółowy)
- Rezerwacja spotkań z korepetytorami
- Historia i zarządzanie rezerwacjami
- Filtrowanie rezerwacji według statusu
- Możliwość ponownego rezerwowania spotkań
- Obsługa sesji użytkownika
- Uruchamianie aplikacji lokalnie oraz w kontenerze Docker

---

## Instrukcja uruchomienia aplikacji

### Lokalnie (bez Dockera)

1. Zainstaluj zależności:
   ```bash
   pip install -r requirements.txt
