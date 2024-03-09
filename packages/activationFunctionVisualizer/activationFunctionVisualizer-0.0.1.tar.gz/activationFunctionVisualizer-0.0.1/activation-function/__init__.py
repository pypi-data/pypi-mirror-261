import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
     return 1 / (1 + np.exp(-x))
   
def tanh(x):
    return  np.tanh(x)


def relu(x):
    return np.maximum(0, x)


def plot_activation(x_values, activation_function, label, color='blue', title=None):
    """Plots a given activation function.

    Args:
        x_values: An array or a single value for the x-axis.
        activation_function: The activation function to plot (sigmoid, tanh, or relu).
        label: The label for the plot.
        color: The color of the line (default: blue).
        title: Optional title for the plot.
    """
    if isinstance(x_values, (int, float)):  # Check if it's a single value
        x_values = np.array([x_values])  # Convert to a NumPy array

    plt.plot(x_values, activation_function(x_values), label=label, color=color)
    if title is None:
        title = f'{label} Activation Function' 
    plt.title(title)
    plt.xlabel('Input')
    plt.ylabel('Output')
    plt.legend()
    plt.show()


# x = np.linspace(-5, 5, 100)
# plot_activation(x,relu,'relu',None)
# plot_activation(x,tanh,'tanh',None)
