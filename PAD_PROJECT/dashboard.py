import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Wczytanie danych
df = pd.read_csv("data/airplane_price_dataset.csv")

# Poprawienie nazw kolumn
df.columns = [
    "Model", "Production_Year", "Num_Engines", "Engine_Type", "Capacity",
    "Range_km", "Fuel_Consumption_L_per_hour", "Hourly_Maintenance_Cost",
    "Age", "Sales_Region", "Price_USD"
]

# Słownik do zamiany nazw regionów
region_translation = {
    "Asya": "Asia",
    "Avrupa": "Europe",
    "Avustralya": "Australia",
    "Güney Amerika": "South America",
    "Afrika": "Africa",
    "Kuzey Amerika": "North America"
}
df["Sales_Region"] = df["Sales_Region"].replace(region_translation)
df["Age"] = 2023 - df["Production_Year"]

# Konwersja danych kategorycznych na liczby
df = pd.get_dummies(df, columns=["Engine_Type", "Sales_Region"], drop_first=True)

# Cechy do modelu
features = ["Age", "Num_Engines", "Capacity", "Range_km", "Fuel_Consumption_L_per_hour",
            "Hourly_Maintenance_Cost", "Engine_Type_Turbofan", "Sales_Region_Asia",
            "Sales_Region_Europe", "Sales_Region_Australia", "Sales_Region_South America",
            "Sales_Region_North America"]

X = df[features]
y = df["Price_USD"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Trening modelu
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


st.title("Przewidywanie ceny samolotu")

# Formularz do wprowadzania specyfikacji samolotu
st.sidebar.header("Wprowadź dane samolotu")
age = st.sidebar.slider("Wiek samolotu (lata)", 0, 50, 10)
num_engines = st.sidebar.selectbox("Liczba silników", [1, 2, 3, 4])
capacity = st.sidebar.slider("Pojemność pasażerska", 1, 500, 150)
range_km = st.sidebar.slider("Zasięg (km)", 500, 20000, 5000)
fuel_consumption = st.sidebar.slider("Zużycie paliwa (L/h)", 1.0, 50.0, 10.0)
hourly_maintenance = st.sidebar.slider("Koszt serwisu ($/h)", 100, 50000, 5000)
engine_type = st.sidebar.radio("Typ silnika", ["Turbofan", "Piston"])
sales_region = st.sidebar.selectbox("Region sprzedaży", ["Asia", "Europe", "Australia", "South America", "North America"])

# Tworzenie wejścia dla modelu
input_data = pd.DataFrame([[age, num_engines, capacity, range_km, fuel_consumption, hourly_maintenance,
                            1 if engine_type == "Turbofan" else 0,
                            1 if sales_region == "Asia" else 0,
                            1 if sales_region == "Europe" else 0,
                            1 if sales_region == "Australia" else 0,
                            1 if sales_region == "South America" else 0,
                            1 if sales_region == "North America" else 0]],
                          columns=features)

# Przewidywanie ceny
predicted_price = model.predict(input_data)[0]

# Wyświetlenie wyniku
st.subheader("Przewidywana cena samolotu:")
st.write(f"$ **{predicted_price:,.2f} USD**")

# Filtrowanie danych
filtered_df = df[
    (df["Age"] >= age - 10) & (df["Age"] <= age + 10) &
    (df["Num_Engines"] == num_engines)
    ]

if filtered_df.empty:
    st.warning("Brak dokładnych dopasowań! Pokazujemy podobne samoloty.")

    df["Similarity_Score"] = (
            abs(df["Age"] - age) +
            abs(df["Capacity"] - capacity) +
            abs(df["Range_km"] - range_km)
    )

    # Sortujemy według najmniejszej różnicy
    filtered_df = df.nsmallest(10, "Similarity_Score")
    filtered_df = filtered_df.drop(columns=["Similarity_Score"])

# Wyświetlenie przefiltrowanych danych
st.subheader("Podobne samoloty w bazie")
st.write(f"**Liczba wyników:** {filtered_df.shape[0]}")
st.dataframe(filtered_df[["Model", "Age", "Num_Engines", "Capacity", "Range_km", "Price_USD"]].head(10))


