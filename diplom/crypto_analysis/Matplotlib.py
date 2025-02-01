import matplotlib.pyplot as plt
import pandas as pd

# Загрузка данных из файла gapminder.csv
df = pd.read_csv('D:/Urban University/module_19_3/diplom/data/gapminder.csv')

# Проверка наличия нужных столбцов
print("Столбцы в DataFrame:", df.columns)

# Линейный график курса криптовалюты за несколько лет
plt.figure(figsize=(12, 8))
for year in df['Year'].unique():
    plt.plot(df[df['Year'] == year]['Currency Name'],
             df[df['Year'] == year]['Price'],
             marker='o', label=f'Год {year}')

plt.title('Курс криптовалюты за несколько лет')
plt.xlabel('Криптовалюты')
plt.ylabel('Курс криптовалюты (USD)')
plt.xticks(rotation=90)
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# Гистограмма курса криптовалюты в 2020 году
plt.figure(figsize=(12, 8))
df_2020 = df[df['Year'] == 2020]
plt.bar(df_2020['Currency Name'], df_2020['Price'], color='skyblue')
plt.title('Гистограмма курса криптовалюты в 2020 году')
plt.xlabel('Криптовалюты')
plt.ylabel('Курс криптовалюты (USD)')
plt.xticks(rotation=90)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Круговая диаграмма: средний курс криптовалюты за период
average_price = df.groupby('Currency Name')['Price'].mean()
plt.figure(figsize=(10, 10))
plt.pie(average_price, labels=average_price.index, autopct='%1.1f%%', startangle=140)
plt.title('Средний курс криптовалюты за период')
plt.axis('equal')
plt.show()