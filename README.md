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
7. [Autor](#autor)  
8. [Stan projektu i rekomendacje](#stan-projektu-i-rekomendacje)  

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
- **HTML5 + CSS3 + Tailwind** — stylizacja i responsywny frontend
- **Django Templates** — dynamiczne szablony HTML
- **Django Auth** — system logowania i zarządzania użytkownikami
- **Role-based Access Control** — różne widoki i akcje zależne od roli użytkownika
- **Custom Forms + Validation** — własne formularze z walidacją po stronie serwera i klienta
- **Filtrowanie danych w widokach** — filtrowanie rezerwacji po statusie
- **Panel administratora Django** — zarządzanie danymi przez admina
- **Django Messages Framework** — komunikaty systemowe
- **Unit testy** — podstawowe testy formularzy i modeli

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
- ✅ Stylizacja widoków z TailwindCSS
- ✅ Uruchamianie aplikacji w kontenerze Docker
- ✅ Przykładowe dane testowe (fixture)
- ✅ Walidacja danych w formularzach po stronie klienta i serwera
- ✅ Testy jednostkowe: `TutorProfile`, formularze

---

## Instrukcja uruchomienia aplikacji

### Lokalnie (bez Dockera)

1. Utwórz i aktywuj środowisko wirtualne:

```bash
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate    # Windows
```

2. Zainstaluj wymagane biblioteki:

```bash
pip install -r requirements.txt
```

3. Wykonaj migracje bazy danych:

```bash
python manage.py migrate
```

4. (Opcjonalnie) Załaduj przykładowe dane:

```bash
python manage.py loaddata example_data.json
```

5. Uruchom serwer deweloperski:

```bash
python manage.py runserver
```

Aplikacja będzie dostępna pod adresem:  
http://localhost:8000/

### Przez Docker

```bash
docker-compose up --build
```

Aplikacja dostępna będzie pod adresem:  
http://localhost:8000/

---

## Architektura aplikacji (MVC)

- **Model (M)** – `CustomUser`, `TutorProfile`
- **View (V)** – szablony HTML: listy korepetytorów, formularze, panel rezerwacji
- **Controller (C)** – widoki funkcjonalne i klasowe Django (`views.py`)

---

## Przykładowe dane

Aby załadować przykładowych użytkowników do bazy danych, wykonaj:

```bash
python manage.py loaddata example_data.json
```

Zostaną dodani trzej użytkownicy:

- 👨‍🏫 `jan_tutor` – rola: *korepetytor*
- 👩‍🎓 `anna_student` – rola: *student*
- 👨‍🎓 `piotr_student` – rola: *student*

Dla użytkownika `jan_tutor` zostanie automatycznie utworzony profil nauczyciela (`TutorProfile`), dzięki mechanizmowi sygnałów Django (`signals.py`).

---

## Autor

Autor projektu:  
- Dmytro Yaremenko

---

## Stan projektu i rekomendacje

Projekt spełnia wszystkie wymagania podstawowe oraz zawiera rozszerzenia, które pozwalają na uzyskanie wyższej oceny:

✅ Architektura MVC (Model–View–Controller)  
✅ Obsługa ról użytkowników (student / tutor)  
✅ Filtrowanie i historia rezerwacji  
✅ Formularze z walidacją po stronie serwera i klienta  
✅ Stylizacja Tailwind CSS  
✅ Konteneryzacja z Docker i docker-compose  
✅ Fixture z przykładowymi użytkownikami  
✅ Testy jednostkowe (formularz + profil nauczyciela)

🎯 Rekomendujemy przed obroną:
- Pokazać działanie formularzy i walidacji
- Pokaż w adminie utworzonych użytkowników z fixture
- Jeśli możliwe — zademonstrować działanie Dockera
- Zaznaczyć, że `TutorProfile` tworzy się automatycznie dzięki `signals.py`
