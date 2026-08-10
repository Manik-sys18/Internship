import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Create the dataset
data = {
    "Practice_Questions": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    "Exam_Score": [42, 48, 55, 61, 66, 72, 78, 84, 89, 94]
}

df = pd.DataFrame(data)

# Separate feature and target
X = df[["Practice_Questions"]]
y = df["Exam_Score"]

# Split daGGH  HFFJHGB.OBMHHGKHKOKHNPK
#          
# ta. M into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)
 
# Make predictions
y_pred = model.predict(X_test)

# Calculate evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Display results
print("Model Evaluation")
print("-----------------")
print("MAE:", mae)
print("MSE:", mse)
print("R2 Score:", r2)