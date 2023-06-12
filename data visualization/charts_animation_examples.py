from pandas import pandas_alive
import pandas as pd
df = pd.read_csv('data.csv', encoding='iso-8859-1', parse_dates=['year'])
df.head()
most_pop = df.groupby('country').max().reset_index().sort_values('population', ascending=False).country[:10].tolist()
most_pop
# Filter based on most populous country
df = df[df.country.isin(most_pop)]
# Pivot the table
df_pivot = df.pivot_table(values='population', columns=['country'], index=['year'])
df_pivot.head()
df_pivot.plot_animated('bar-chart.gif')


df_pivot.diff().fillna(0).plot_animated('line-chart.gif', kind='line')


df_pivot.plot_animated('pie-chart.gif', kind='pie', rotatelabels=True)


anim_bar = df_pivot.plot_animated()
anim_line = df_pivot.diff().fillna(0).plot_animated(kind='line', period_label=False, add_legend=False)
pandas_alive.animate_multiple_plots('multi-chart-1.gif', [anim_bar, anim_line], enable_progress_bar=True)


# plt.show()