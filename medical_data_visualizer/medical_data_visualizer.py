import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1 load the dataset
df = pd.read_csv("medical_examination.csv")

# 2 add an overweight column
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2) > 25
df['overweight'] = df['overweight'].astype(int)  # Convert boolean to integer (0 or 1)

# 3 normalise cholesterol & glucose
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


# 4 draw the categorical plot
def draw_cat_plot():
    # 5 convert data into long format using pd.melt()
    df_cat = pd.melt(df, 
                     id_vars=['cardio'], 
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6 group and reformat the data for count visualisation
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')    

    # 7 draw a seaborn catplot
    cat_plot = sns.catplot(data=df_cat, 
                      x='variable', y='total', hue='value', kind='bar', col='cardio')

    # 8 convert the FaceGrid to a figure
    fig = cat_plot.fig

    # 9 save the figure
    fig.savefig('catplot.png')
    return fig


# 10 draw the heatmap
def draw_heat_map():
    # 11 Clean data based on given conditions
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
                 (df['height'] >= df['height'].quantile(0.025)) & 
                 (df['height'] <= df['height'].quantile(0.975)) & 
                 (df['weight'] >= df['weight'].quantile(0.025)) & 
                 (df['weight'] <= df['weight'].quantile(0.975))]

    # 12 Compute the correlation matrix
    corr = df_heat.corr()

    # 13 Create a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14 Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 8))

    # 15 Draw the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", cmap="coolwarm", linewidths=0.5)

    # 16 save the figure 
    fig.savefig('heatmap.png')
    return fig