import pandas as pd
import matplotlib.pyplot as plt
import random

# Загрузка данных из CSV-файла
data_file = "filtered_gdp_data.csv"
data = pd.read_csv(data_file)

# Убираем строки с пустыми значениями в колонке "2016 [YR2016]"
data = data.dropna(subset=["2016 [YR2016]"])

# Преобразование колонки "2016 [YR2016]" в числовой формат
data["2016 [YR2016]"] = pd.to_numeric(data["2016 [YR2016]"], errors='coerce')

# Выбор случайных 10 стран
random_countries = data.sample(10)

# Извлечение названий стран и значений
labels = random_countries["Country Name"]
values = random_countries["2016 [YR2016]"]

# Построение круговой диаграммы
plt.figure(figsize=(10, 8))
plt.pie(
    values,
    labels=labels,
    autopct='%1.1f%%',  # Подписи в процентах
    startangle=90,
    colors=plt.cm.tab10.colors,  # Цветовая палитра
    wedgeprops={'edgecolor': 'black'}
)

# Настройка заголовка
plt.title("Круговая диаграмма значений 2016 года для 10 случайных стран", fontsize=14)
plt.tight_layout()
plt.show()
