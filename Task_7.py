import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Create a supervised learning dataset
data = {
    "Study_Hours": [1, 2, 3, 4, 5],
    "Score": [35, 45, 55, 65, 75]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# Separate input (X) and output (y)
X = df[["Study_Hours"]]
y = df["Score"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining Data:")
print(X_train)

print("\nTesting Data:")
print(X_test)

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

print("\nModel trained successfully!")
print("ML fundamentals understood!")