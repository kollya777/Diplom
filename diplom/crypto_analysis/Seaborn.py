import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Загрузка данных из файла gapminder.csv
df = pd.read_csv('D:/Urban University/module_19_3/diplom/data/gapminder.csv')

# Линейный график
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Year', y='Price', hue='Currency Name', marker='o')
plt.title('Курс криптовалюты по годам')
plt.xlabel('Год')
plt.ylabel('Курс криптовалюты (USD)')
plt.xticks(rotation=45)
plt.grid()
plt.show()

# Столбчатая диаграмма
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Year', y='Price', hue='Currency Name', ci=None)
plt.title('Курс криптовалюты по годам')
plt.xlabel('Год')
plt.ylabel('Курс криптовалюты (USD)')
plt.xticks(rotation=45)
plt.grid()
plt.show()

# Диаграмма рассеяния
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Year', y='Price', hue='Currency Name', style='Currency Name', s=100)
plt.title('Диаграмма рассеяния: Год vs Курс криптовалюты')
plt.xlabel('Год')
plt.ylabel('Курс криптовалюты (USD)')
plt.xticks(rotation=45)
plt.grid()
plt.show()