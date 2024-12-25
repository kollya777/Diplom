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

# Линейный график
fig_line = px.line(df[df['country'].isin(['United States', 'China', 'India'])],
                   x='year', y='lifeExp', color='country',
                   title='Изменение ожидаемой продолжительности жизни по странам')
fig_line.write_html("line_plot.html")

# Гистограмма
fig_bar = px.bar(df[df['country'].isin(['United States', 'China', 'India'])],
                 x='country', y='lifeExp',
                 title='Ожидаемая продолжительность жизни по странам',
                 color='country')
fig_bar.write_html("bar_plot.html")

# Диаграмма рассеяния
fig_scatter = px.scatter(df,
                         x='year', y='lifeExp',
                         color='country',
                         title='Диаграмма рассеяния: Год vs Ожидаемая продолжительность жизни')
fig_scatter.write_html("scatter_plot.html")

# Круговая диаграмма
fig_pie = px.pie(df.groupby('country')['lifeExp'].mean().reset_index(),
                 values='lifeExp', names='country',
                 title='Средняя ожидаемая продолжительность жизни по странам')
fig_pie.write_html("pie_chart.html")
