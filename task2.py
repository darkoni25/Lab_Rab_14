import pandas as pd
import matplotlib.pyplot as plt
import random

# Завантаження даних із CSV-файлу
data_file = "filtered_gdp_data.csv"
data = pd.read_csv(data_file)

# Видаляємо рядки з відсутніми значеннями у стовпчику "2016 [YR2016]"
data = data.dropna(subset=["2016 [YR2016]"])

# Перетворення стовпчика "2016 [YR2016]" у числовий формат
data["2016 [YR2016]"] = pd.to_numeric(data["2016 [YR2016]"], errors='coerce')

# Вибір 10 випадкових країн
random_countries = data.sample(10)

# Отримання назв країн і значень
labels = random_countries["Country Name"]
values = random_countries["2016 [YR2016]"]

# Побудова кругової діаграми
plt.figure(figsize=(10, 8))
plt.pie(
    values,
    labels=labels,
    autopct='%1.1f%%',  # Відображення значень у відсотках
    startangle=90,  # Початковий кут для діаграми
    colors=plt.cm.tab10.colors,  # Кольорова палітра
    wedgeprops={'edgecolor': 'black'}  # Межі секторів
)

# Налаштування заголовка
plt.title("Кругова діаграма показників за 2016 рік для 10 випадкових країн", fontsize=14)
plt.tight_layout()
plt.show()
