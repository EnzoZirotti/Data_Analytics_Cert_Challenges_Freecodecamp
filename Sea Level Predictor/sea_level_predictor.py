import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], s=15)

    # Get the slope and y-intercept of the line of best fit
    slope, intercept, rvalue, pvalue, stderr = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create line of best fit for all the data
    x_pred = pd.Series([i for i in range(1880, 2051)])
    y_pred = intercept + slope*x_pred
    plt.plot(x_pred, y_pred, 'r', label='All Data')

    # Create line of best fit for data after year 2000
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, rvalue_recent, pvalue_recent, stderr_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred_recent = pd.Series([i for i in range(2000, 2051)])
    y_pred_recent = intercept_recent + slope_recent*x_pred_recent
    plt.plot(x_pred_recent, y_pred_recent, 'g', label='Recent Data')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()