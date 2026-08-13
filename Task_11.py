import pandas as pd
from sklearn.linear_model import LinearRegression

# Create a small dataset
data = {
    "Screen_Time": [1, 2, 3, 4, 5, 6, 7, 8],
    "Battery_Used": [8, 16, 25, 34, 43, 52, 61, 70]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# X is the input feature (Screen Time)
X = df[["Screen_Time"]]

# y is the target/output (Battery Used)
y = df["Battery_Used"]

# Create the Linear Regression model
model = LinearRegression()

# Train the model using the dataset
model.fit(X, y)

# Take the input as int
screen_time = input("Enter your screen time in hours: ")

# Convert the input to a float
screen_time = float(screen_time)

# Predict battery consumption
new_data = pd.DataFrame({
    "Screen_Time": [screen_time]
})

prediction = model.predict(new_data)

# Display the predicted battery consumption
print(f"Predicted Battery Consumption: {prediction[0]:.2f}%")