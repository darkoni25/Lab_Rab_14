import numpy as np
import matplotlib.pyplot as plt

# Годы
x = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]

# Количество игроков в видеоигры (например, в миллионах) для Украины
y = [2.3, 2.5, 2.8, 3.0, 3.5, 4.0, 4.5, 5.0, 5.2, 5.5, 5.8, 6.0, 6.2, 6.5, 6.8, 7.0]

# Количество игроков в видеоигры для Албании
z = [0.5, 0.6, 0.7, 0.8, 1.0, 1.2, 1.5, 1.8, 2.0, 2.2, 2.5, 2.7, 3.0, 3.3, 3.5, 3.8]

# Преобразование данных в numpy-массивы
x = np.array(x)
y = np.array(y)
z = np.array(z)

# Построение графиков
plt.plot(x, y, label='Ukraine', color='blue')   # График для Украины
plt.plot(x, z, label='Albania', color='green')  # График для Албании

# Настройка графика
plt.title('Number of Gamers by Year', fontsize=15)   # Название графика
plt.xlabel('Year', fontsize=12, color='black')      # Подпись оси X
plt.ylabel('Number of Gamers (millions)', fontsize=12, color='black')  # Подпись оси Y
plt.legend()                                        # Легенда
plt.grid(True)                                      # Сетка

# Отображение графика
plt.show()
