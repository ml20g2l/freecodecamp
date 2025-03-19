import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 5))

    # Scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], color="blue", label="Data")

    # return plt

    # First line of best fit (1880 - 2014)
    slope1, intercept1, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended = pd.Series(range(1880, 2051))
    sea_levels_extended = slope1 * years_extended + intercept1
    plt.plot(years_extended, sea_levels_extended, color="red", label="Best Fit: 1880-2014")

    # Second line of best fit (2000 - 2014)
    df_recent = df[df["Year"] >= 2000]
    slope2, intercept2, _, _, _ = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent = pd.Series(range(2000, 2051))
    sea_levels_recent = slope2 * years_recent + intercept2
    plt.plot(years_recent, sea_levels_recent, color="green", linestyle="dashed", label="Best Fit: 2000-2014")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()