import matplotlib.pyplot as plt
import pandas as pd

# Загрузка данных
df = pd.read_csv('gapminder.csv')

# Проверка наличия нужных столбцов
print("Столбцы в DataFrame:", df.columns)

# Проверка наличия данных за 2000 и 2002 годы
if '2000' not in df.columns or '2002' not in df.columns:
    print("Ошибка: Не найдены данные для годов 2000 и 2002.")
else:
    print("Данные за 2000 и 2002 годы найдены.")

# Выбор годов для отображения
years = ['2000', '2001', '2002']

# Линейный график ВВП на душу населения за несколько лет
plt.figure(figsize=(12, 8))
for year in years:
    plt.plot(df['Country Name'], df[year], marker='o', label=f'Год {year}')

plt.title('ВВП на душу населения за несколько лет')
plt.xlabel('Страны')
plt.ylabel('ВВП на душу населения')
plt.xticks(rotation=90)  # Поворачиваем названия стран для лучшей читаемости
plt.legend()
plt.grid()
plt.tight_layout()  # Улучшает размещение элементов
plt.show()

# Гистограмма ВВП на душу населения в 2002 году
plt.figure(figsize=(12, 8))
plt.bar(df['Country Name'], df['2002'], color='skyblue')
plt.title('Гистограмма ВВП на душу населения в 2002 году')
plt.xlabel('Страны')
plt.ylabel('ВВП на душу населения')
plt.xticks(rotation=90)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Диаграмма рассеяния: ВВП на душу населения в 2000 и 2002 годах
if '2000' in df.columns and '2002' in df.columns:
    plt.figure(figsize=(12, 8))
    plt.scatter(df['2000'], df['2002'], color='orange', alpha=0.7)
    plt.title('Диаграмма рассеяния: ВВП на душу населения (2000 vs 2002)')
    plt.xlabel('ВВП на душу населения в 2000 году')
    plt.ylabel('ВВП на душу населения в 2002 году')

    # Добавление аннотаций для каждой точки
    for i in range(len(df)):
        plt.annotate(df['Country Name'][i], (df['2000'][i], df['2002'][i]), fontsize=8, alpha=0.7)

    plt.grid()
    plt.tight_layout()
    plt.show()
else:
    print("Ошибка: Не найдены данные для годов 2000 и 2002.")

# Круговая диаграмма: средний ВВП на душу населения по странам в 2002 году
average_gdp = df.groupby('Country Name')['2002'].mean()
plt.figure(figsize=(10, 10))
plt.pie(average_gdp, labels=average_gdp.index, autopct='%1.1f%%', startangle=140)
plt.title('Средний ВВП на душу населения по странам в 2002 году')
plt.axis('equal')  # Чтобы круговая диаграмма была круглой
plt.show()
