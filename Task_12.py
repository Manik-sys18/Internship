# ============================================================
# 📊 ADVERTISING SALES PREDICTION USING LINEAR REGRESSION
# ============================================================

# 1. IMPORT REQUIRED LIBRARIES
# ------------------------------------------------------------

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# 2. CREATE THE DATASET
# ------------------------------------------------------------

# Create a small mock dataset containing advertising budget
# and the corresponding product sales.
data = {
    "Advertising_Budget": [10, 20, 30, 40, 50, 60, 70, 80],
    "Sales": [25, 40, 52, 65, 78, 90, 105, 118]
}

# Convert the dictionary into a Pandas DataFrame.
df = pd.DataFrame(data)

print("Dataset:")
print(df)


# 3. PREPARE THE DATA
# ------------------------------------------------------------

# X represents the input feature.
X = df[["Advertising_Budget"]]

# y represents the target variable that we want to predict.
y = df["Sales"]


# 4. SPLIT THE DATA
# ------------------------------------------------------------

# Divide the dataset into training and testing data.
# 80% is used for training and 20% is used for testing.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# 5. CREATE AND TRAIN THE MODEL
# ------------------------------------------------------------

# Create a Linear Regression model.
model = LinearRegression()

# Train the model using the training data.
model.fit(X_train, y_train)

print("\nModel trained successfully!")


# 6. MAKE PREDICTIONS
# ------------------------------------------------------------

# Use the trained model to predict sales for the test data.
y_pred = model.predict(X_test)

print("\nPredicted Sales:")
print(y_pred)


# 7. EVALUATE THE MODEL
# ------------------------------------------------------------

# Calculate Mean Absolute Error.
mae = mean_absolute_error(y_test, y_pred)

# Calculate Mean Squared Error.
mse = mean_squared_error(y_test, y_pred)

# Calculate R² Score.
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation")
print("----------------")
print("MAE:", mae)
print("MSE:", mse)
print("R² Score:", r2)


# 8. PREDICT SALES FOR A NEW ADVERTISING BUDGET
# ------------------------------------------------------------

# Ask the user to enter a new advertising budget.
budget = float(input("\nEnter advertising budget (₹ thousands): "))

# Create a DataFrame with the same feature name used during training.
new_data = pd.DataFrame({
    "Advertising_Budget": [budget]
})

# Predict sales using the trained model.
new_prediction = model.predict(new_data)

print(f"Predicted Sales: ₹{new_prediction[0]:.2f} thousand")


# 9. CONCLUSION
# ------------------------------------------------------------

print("\nConclusion:")
print("The Linear Regression model was trained successfully")
print("and used to predict sales based on advertising budget.")