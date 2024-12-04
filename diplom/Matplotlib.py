import matplotlib.pyplot as plt
import pandas as pd

# Загрузка данных
df = pd.read_csv('dan/gapminder.csv')

# Проверка наличия нужных столбцов
print(df.columns)

# Выбор годов для отображения
years = ['2000', '2001', '2002']

# Создание графика
plt.figure(figsize=(12, 8))

# Проход по выбранным годам и построение графиков
for year in years:
    plt.plot(df['Country Name'], df[year], marker='o', label=f'Год {year}')

plt.title('ВВП на душу населения за несколько лет')
plt.xlabel('Страны')
plt.ylabel('ВВП на душу населения')
plt.xticks(rotation=90)  # Поворачиваем названия стран для лучшей читаемости
plt.legend()
plt.grid()
plt.show()

