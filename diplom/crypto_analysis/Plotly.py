import pandas as pd
import plotly.express as px

# Загрузка данных из файла gapminder.csv
df = pd.read_csv('D:/Urban University/module_19_3/diplom/data/gapminder.csv')

# Линейный график
fig_line = px.line(df,
                   x='Year', y='Price', color='Currency Name',
                   title='Изменение курса криптовалюты по годам')
fig_line.write_html("line_plot.html")

# Гистограмма
fig_bar = px.bar(df,
                 x='Currency Name', y='Price',
                 title='Курс криптовалюты по странам',
                 color='Currency Name')
fig_bar.write_html("bar_plot.html")

# Диаграмма рассеяния
fig_scatter = px.scatter(df,
                         x='Year', y='Price',
                         color='Currency Name',
                         title='Диаграмма рассеяния: Год vs Курс криптовалюты')
fig_scatter.write_html("scatter_plot.html")

# Круговая диаграмма
average_price = df.groupby('Currency Name')['Price'].mean().reset_index()
fig_pie = px.pie(average_price,
                 values='Price', names='Currency Name',
                 title='Средний курс криптовалюты по странам')
fig_pie.write_html("pie_chart.html")