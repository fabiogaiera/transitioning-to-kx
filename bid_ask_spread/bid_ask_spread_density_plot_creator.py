# bid_ask_spread_density_plot_creator.py

import matplotlib.pyplot as plt
import seaborn as sns


def create_density_plot(df):
    # Create a figure and axes object for plotting
    fig, ax = plt.subplots()

    # Set the window title of the figure (works only in some GUI backends)
    fig.canvas.manager.set_window_title("Intraday Analysis")

    # Plot the Kernel Density Estimate (KDE) of the 'bid_ask_spread' column
    sns.kdeplot(df['bid_ask_spread'], fill=True, color='purple', linewidth=2, ax=ax)

    # Set the plot title and axis labels with specific font sizes
    ax.set_title("Density Plot of Effective Bid-Ask Spread (%)", fontsize=14)
    ax.set_xlabel("Effective Bid-Ask Spread (%)", fontsize=12)
    ax.set_ylabel("Density", fontsize=12)

    # Add grid lines to the plot for better readability
    ax.grid(True)

    # Automatically adjust layout to prevent overlap of elements
    fig.tight_layout()

    # Display the plot
    plt.show()
