import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Data")

    # Create first line of best fit (all data)
    res_all = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended = pd.Series(range(1880, 2051))
    sea_level_pred_all = res_all.slope * years_extended + res_all.intercept
    plt.plot(years_extended, sea_level_pred_all, 'r', label="Best Fit: 1880–2050")

    # Create second line of best fit (data from 2000 onward)
    df_recent = df[df["Year"] >= 2000]
    res_recent = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent_extended = pd.Series(range(2000, 2051))
    sea_level_pred_recent = res_recent.slope * years_recent_extended + res_recent.intercept
    plt.plot(years_recent_extended, sea_level_pred_recent, 'green', label="Best Fit: 2000–2050")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Save plot and return for tests
    plt.savefig("sea_level_plot.png")
    return plt.gca()
