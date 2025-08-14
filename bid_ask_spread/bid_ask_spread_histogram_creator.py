# bid_ask_spread_histogram_creator.py

# Import necessary libraries
import matplotlib.pyplot as plt


def create_histogram(df):
    # Create a new figure and axes object
    fig, ax = plt.subplots()

    # Set the window title
    fig.canvas.manager.set_window_title("Intraday Analysis")

    # Plot the DataFrame on the specified axes
    df.plot(kind='bar', ax=ax, color='green')

    # Set the plot title and axis labels
    ax.set_title("Intraday Bid-Ask Spread Histogram", fontsize=14)
    ax.set_xlabel("Hour", fontsize=12)
    ax.set_ylabel("Bid-Ask Spread", fontsize=12)

    # Add grid lines
    ax.grid(True)

    # Adjust layout
    plt.tight_layout()

    # Show the plot
    plt.show()
