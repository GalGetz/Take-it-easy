import matplotlib.pyplot as plt

# Example datasets (replace with your actual data)
# Let's assume these are the y-values for the four points on your line
y_values = [138.617, 138.397, 141.508, 142.5, 144.83,147.5]  # Replace this with your data
x_values = [1, 2, 3, 4, 5, 6]  # x-axis positions

# Create the plot
plt.figure(figsize=(8, 6))

# Plot the line with error bars
plt.plot(x_values, y_values, marker='o', linestyle='--', color='blue')

# If you have error bars, you can include them like this:
# Assuming errors (you can replace this with actual error data)
errors = [33.77, 34.78645413088262, 35.142195947322364, 33.52, 32.59, 28]
plt.errorbar(x_values, y_values, yerr=errors, fmt='o', color='blue', capsize=5)

# Customize the plot
plt.xlabel('Max Depth', fontsize=14)
plt.ylabel('Score', fontsize=14)
plt.title('Expectimax performance by Max Depth', fontsize=16)
plt.xticks(x_values, ['1', '2', '3', '4', '5', '6'])  # Custom labels if needed
plt.ylim(70, 210)  # Adjust based on your data range
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)

# Show the plot
plt.show()