import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Function to calculate the mean
def mean(values):
    return sum(values) / len(values)

# Function to calculate the coefficients of the simple linear regression
def linear_regression(X, Y):
    n = len(X)
    mean_X = mean(X)
    mean_Y = mean(Y)
    
    # Calculating the numerator and denominator for the slope (b1)
    numerator = sum((X[i] - mean_X) * (Y[i] - mean_Y) for i in range(n))
    denominator = sum((X[i] - mean_X) ** 2 for i in range(n))
    
    b1 = numerator / denominator
    b0 = mean_Y - b1 * mean_X
    
    return b0, b1

# Function to calculate the coefficient of determination (R^2)
def r_squared(X, Y, b0, b1):
    y_mean = mean(Y)
    ss_tot = sum((Y[i] - y_mean) ** 2 for i in range(len(Y)))
    ss_res = sum((Y[i] - (b0 + b1 * X[i])) ** 2 for i in range(len(X)))
    r2 = 1 - (ss_res / ss_tot)
    return r2

# Read and format the data
with open('data.txt', 'r') as file:
    content = file.read()

content_dot = content.replace(',', '.')

split_content = content_dot.split()

number_of_lines = int(len(split_content) / 4)

formatted_content = [float(i) for i in split_content]

# Assuming the data is organized as described
temperature = formatted_content[0 * number_of_lines: 1 * number_of_lines]
prototype_ap = formatted_content[1 * number_of_lines: 2 * number_of_lines]
prototype_bp = formatted_content[2 * number_of_lines: 3 * number_of_lines]
prototype_c = formatted_content[3 * number_of_lines: 4 * number_of_lines]

prototypes = [prototype_ap, prototype_bp, prototype_c]
prototypes_names = ['Prototype A', 'Prototype B', 'Prototype C']

# Determine the number of rows and columns for subplots
num_prototypes = len(prototypes)
num_cols = 2
num_rows = (num_prototypes + 1) // num_cols  # Add 1 to round up

# Create a single figure with two columns
fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(12, 6*num_rows))

# Plot the initial graph in the first subplot
initial_ax = axes[0, 0]
initial_ax.scatter(temperature, prototype_ap, color='blue', label='Data')

# Perform linear regression for Prototype A
b0, b1 = linear_regression(temperature, prototype_ap)
initial_ax.plot(temperature, [b0 + b1 * x for x in temperature], color='red', label='Trendline')

initial_ax.set_title('Initial Graph')
initial_ax.set_xlabel('Temperature')
initial_ax.set_ylabel('Prototype A')
initial_ax.legend()
initial_ax.grid(True)

for i, (prototype, name) in enumerate(zip(prototypes, prototypes_names)):
    # Calculate the position in the subplot grid
    row = (i + 1) // num_cols
    col = (i + 1) % num_cols
    
    # Perform linear regression
    b0, b1 = linear_regression(temperature, prototype)
    
    # Calculate R^2
    r2 = r_squared(temperature, prototype, b0, b1)
    
    # Make predictions
    predictions = [b0 + b1 * x for x in temperature]
    
    # Plot scatter plot
    ax = axes[row, col]
    ax.scatter(temperature, prototype, color='blue', label='Data')
    ax.plot(temperature, predictions, color='red', label='Linear Regression')
    ax.set_title(f'Scatter Plot and Linear Regression for {name}')
    ax.set_xlabel('Temperature')
    ax.set_ylabel(f'Prototype {name[-1]}')
    ax.legend()
    ax.grid(True)

    # Output R^2
    print(f'R^2 for {name}: {r2:.4f}')

    # Perform hypothesis test for regression
    slope, intercept, r_value, p_value, std_err = stats.linregress(temperature, prototype)
    print(f'p-value for hypothesis test for regression for {name}: {p_value:.4f}')

    # Estimate the degree of malleability at 30 °C
    maleability_at_30 = b0 + b1 * 30
    print(f'Estimated malleability at 30°C for {name}: {maleability_at_30:.4f}')

# Adjust layout and display plot
plt.tight_layout()
plt.show()
