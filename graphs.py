import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd



def bar_graph(data, years,title, x_label, y_label):

    # get years with increment of 5
    year_columns = [str(years) for years in range(1990, 2016, 5)]
    # Plot bar graph
    df_bar = data[data['Indicator Name'].isin([title])]

    # create a new data frame for plotting
    df_pivot = df_bar.pivot(index='Country Name', columns='Indicator Name', values=year_columns)
    # Define the graph
    ax = df_pivot.plot(kind='bar', rot=0)
    plt.title(title)
    plt.xlabel(x_label)
    # legend labels
    handles, labels = ax.get_legend_handles_labels()
    new_labels = [label.split(',')[0][1:] for label in labels]
    plt.legend(handles, new_labels, title='Year')
    plt.show()
    

def heatmap(data,country,indicators,colors):
    
    
    df_sub_heat = data[(data['Country Name'] == country) & (data['Indicator Name'].isin(indicators))]

    pivot_table = pd.pivot_table(df_sub_heat, columns='Indicator Name')

    pivot_table.fillna(pivot_table.mean(), inplace=True)

    # correlation matrix
    corr_matrix = pivot_table.corr()

    # Create a heatmap of the correlation matrix
    sns.heatmap(corr_matrix, cmap=colors, annot=True, fmt='.2f', square=True)

    plt.title(country)
    plt.xticks(rotation=90, fontsize=8)
    plt.yticks(rotation=0, fontsize=8)
    plt.show()