import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Create the dataset
data = {
    "Engine_Size": [1.0, 1.2, 1.5, 1.8, 2.0, 2.2, 2.5, 3.0, 3.5, 4.0],

    "Car_Price": [5, 6, 8, 10, 12, 14, 17, 22, 28, 35]
}

df = pd.DataFrame(data)

# Feature and target
X = df[["Engine_Size"]]
y = df["Car_Price"]

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# New engine sizes for prediction
new_cars = pd.DataFrame({
    "Engine_Size": [1.6, 2.7, 3.2]
})

# Make predictions
predictions = model.predict(new_cars)

# Display predictions
for engine, price in zip(new_cars["Engine_Size"], predictions):
    print(f"Engine Size: {engine} L → Predicted Price: ₹{price:.2f} Lakhs")

print("Predictions generated successfully!")