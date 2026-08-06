import matplotlib.pyplot as plt

day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"] # Days of the week
ice_creams = [30, 50, 65, 45, 70, 55, 85] # Number of ice creams sold each day
temperature = [22.2, 23.9, 26.7, 25.6, 28.9, 30.5, 32.4] # Temperature for each day in degrees Celsius
profit = [2500, 3200, 2800, 4100, 3500, 3900, 4500] # Profit for each day in rupees

plt.scatter(temperature, profit, marker = 'o', color = 'b', label = 'Profit vs Temperature') # temperature vs profit scatter plot
plt.xlabel('Temperature (°C)')
plt.ylabel('Profit (₹)')
plt.title('Ice Cream Sales Analysis')
plt.legend()
plt.grid(True)
plt.show()

plt.bar(day, ice_creams, color = 'red', label = 'Ice Creams Sold') # bar chart for ice creams sold each day
plt.xlabel('Days of the Week')
plt.ylabel('Number of Ice Creams Sold')
plt.title('Ice Cream Sales Analysis')
plt.legend()
plt.grid(False)
plt.show()

plt.plot(day, temperature, color = 'green', marker = 'o', label = 'Temperature') # line chart for temperature over the days of the week
plt.xlabel('Days of the Week')
plt.ylabel('Temperature (°C)')
plt.axhline(y=25, color='r', linestyle='--', label='Average Temperature (25°C)')
plt.title('Temperature Analysis')
plt.legend()
plt.grid(True)
plt.show()

print("Basic charts created")
print("Data visualization completed!")