import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Создание данных для DataFrame
data = {
    'country': ['United States', 'United States', 'United States', 'United States', 'United States',
                'China', 'China', 'China', 'China', 'China',
                'India', 'India', 'India', 'India', 'India'],
    'year': [2000, 2005, 2010, 2015, 2020,
             2000, 2005, 2010, 2015, 2020,
             2000, 2005, 2010, 2015, 2020],
    'lifeExp': [76.8, 78.2, 78.7, 79.1, 78.9,
                 71.4, 73.6, 75.2, 76.2, 77.3,
                 63.6, 65.3, 66.7, 67.9, 69.4]
}

# Создание DataFrame
df = pd.DataFrame(data)

# Линейный график
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='year', y='lifeExp', hue='country', marker='o')
plt.title('Life Expectancy over Years by Country')
plt.xlabel('Year')
plt.ylabel('Life Expectancy')
plt.xticks(rotation=45)
plt.show()

# Столбчатая диаграмма
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='year', y='lifeExp', hue='country', ci=None)
plt.title('Life Expectancy by Year and Country')
plt.xlabel('Year')
plt.ylabel('Life Expectancy')
plt.xticks(rotation=45)
plt.show()
