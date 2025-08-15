# Import necessary libraries
import matplotlib.pyplot as plt


def create_histogram(df):
    # Create a new figure and axes object
    fig, ax = plt.subplots()

    # Set the window title
    fig.canvas.manager.set_window_title("Intraday Analysis")

    # Plot the DataFrame on the specified axes
    df.plot(kind='bar', ax=ax)

    # Set the plot title and axis labels
    ax.set_title("Intraday Trading Volume Histogram", fontsize=14)
    ax.set_xlabel("Hour", fontsize=12)
    ax.set_ylabel("Total Size", fontsize=12)

    # Add grid lines
    ax.grid(True)

    # Adjust layout
    plt.tight_layout()

    # Show the plot
    plt.show()
