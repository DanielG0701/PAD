# PAD_PROJECT – Przewidywanie cen samolotów
### Daniel Gruszkowski | s34326
## Opis projektu
Projekt przewidywania ceny samolotu na podstawie jego specyfikacji technicznej.  
W którym użyto **regresji Random Forest**, aby określić wartość samolotu w zależności od takich czynników jak **wiek, liczba silników, pojemność pasażerska, zasięg, zużycie paliwa i region sprzedaży**.

Wykorzystane technologie:
- **Python** 
- **Jupyter Notebook** (Analiza danych i modelowanie)
- **Streamlit** (Interaktywny dashboard do przewidywania cen)
- **Conda** (Zarządzanie środowiskiem)

---

## Struktura projektu

### **Opis plików:**
- `data/` – Folder zawierający **zbiór danych o samolotach**.
- `airplane_price.ipynb` – Notebook **z analizą danych, przygotowaniem modelu i oceną wyników**.
- `dashboard.py` – **Interaktywna aplikacja Streamlit**, pozwalająca użytkownikowi przewidzieć cenę samolotu na podstawie wybranych parametrów.
- `environment.yml` – **Plik dla Condy**, umożliwiający szybkie stworzenie środowiska.

---

## **Instrukcja uruchomienia**
Aby uruchomić projekt, wykonaj poniższe kroki:

### 1. **Instalacja przy użyciu Conda**
```bash
conda env create -f environment.yml
conda activate pad_project
```

### 2. Uruchomienie analizy danych w Jupyter Notebook

```bash
jupyter notebook airplane_price.ipynb
```

### 3.  Uruchomienie interaktywnego dashboardu Streamlit

```bash
streamlit run dashboard.py
```

---
## Źródło danych 
Dane uzyskane z strony **kaggle.com**,
link do danych:
- https://www.kaggle.com/datasets/asinow/airplane-price-dataset/data










