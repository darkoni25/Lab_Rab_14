import pandas as pd
import matplotlib.pyplot as plt
import random
import matplotlib.pyplot as plt
# Загрузка данных из CSV-файла
data_file = "filtered_gdp_data.csv"
data = pd.read_csv(data_file)

# Фильтрация данных для Украины и США
ukraine_data = data[data['Country'] == 'Ukraine']
usa_data = data[data['Country'] == 'United States']

# Сортировка данных по году (на случай, если они не отсортированы)
ukraine_data = ukraine_data.sort_values('Year')
usa_data = usa_data.sort_values('Year')

# Извлечение данных для построения графиков
years_ukraine = ukraine_data['Year']
values_ukraine = ukraine_data['Value']

years_usa = usa_data['Year']
values_usa = usa_data['Value']

# Построение графиков
plt.figure(figsize=(10, 6))
plt.plot(years_ukraine, values_ukraine, label="Ukraine", marker='o', color='blue')
plt.plot(years_usa, values_usa, label="USA", marker='o', color='red')

# Настройка графика
plt.title("Динаміка показника 'Children out of school, primary'", fontsize=14)
plt.xlabel("Рік", fontsize=12)
plt.ylabel("Кількість дітей", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)
plt.tight_layout()

# Отображение графика
plt.show()
