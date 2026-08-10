import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Create house dataset
data = {
    "House_Size": [800, 1000, 1200, 1500, 1800, 2000, 2200, 2500, 2800, 3000],
    
    "Price": [25, 30, 36, 45, 54, 60, 66, 75, 84, 90]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# Feature and target
X = df[["House_Size"]]
y = df["Price"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

print("\nModel trained successfully!")

# Display learned values
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)