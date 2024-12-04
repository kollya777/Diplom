import pandas as pd
import plotly.express as px

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

# Линейный график для отображения изменений ожидаемой продолжительности жизни по странам
fig = px.line(df[df['country'].isin(['United States', 'China', 'India'])],
              x='year', y='lifeExp', color='country',
              title='Изменение ожидаемой продолжительности жизни по странам')

# Обновление макета графика
fig.update_layout(xaxis_title='Год', yaxis_title='Ожидаемая продолжительность жизни')

# Отображение графика
# Сохранение графика как HTML файл
fig.write_html("life_expectancy_plot.html")