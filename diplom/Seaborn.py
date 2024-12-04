import seaborn as sns
import pandas as pd
# Создание данных для DataFrame
data = {
    'Country Name': ['United States', 'Canada', 'Germany', 'United Kingdom', 'France',
                     'Japan', 'China', 'India', 'Brazil', 'South Africa'],
    'gdpPercap': [59939, 46350, 46260, 41180, 39200,
                  40000, 10410, 2170, 9600, 6000],
    'lifeExp': [78.9, 82.3, 81.0, 81.2, 82.5,
                84.6, 76.9, 69.4, 75.7, 64.1],
    'continent': ['North America', 'North America', 'Europe', 'Europe', 'Europe',
                  'Asia', 'Asia', 'Asia', 'South America', 'Africa']
}
# Создание DataFrame
df = pd.DataFrame(data)
# Установка стиля графика
sns.set(style='whitegrid')
# Диаграмма рассеяния для анализа взаимосвязи между ВВП и ожидаемой продолжительностью жизни
scatter_plot = sns.scatterplot(data=df, x='gdpPercap', y='lifeExp', hue='continent', style='continent', palette='deep')
# Добавление заголовка и меток осей
scatter_plot.set_title('Взаимосвязь между ВВП и ожидаемой продолжительностью жизни')
scatter_plot.set_xlabel('ВВП на душу населения')
scatter_plot.set_ylabel('Ожидаемая продолжительность жизни')
# Показ графика
sns.despine()  # Убрать верхнюю и правую границы графика
scatter_plot.figure.tight_layout()  # Автоматическая подгонка макета
scatter_plot.figure.show()  # Отображение графика без использования plt