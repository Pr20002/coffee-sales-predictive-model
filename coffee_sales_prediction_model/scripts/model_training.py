import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import os

# Load the cleaned transaction dataset from the 'data' folder
data_path = os.path.join("..", "data", "clean_coffee_shop_sales.csv")
df = pd.read_csv(data_path)

# Ensures proper date formatting for time-based analysis
df['date'] = pd.to_datetime(df['date'])

# Save original columns before encoding (for Power BI output)
original_dates = df['date']
original_store_locations = df['store_location']
original_day_of_week = df['day_of_week']

# One-hot encoding: converts 'day_of_week' and 'store_location' into binary columns
if 'day_of_week' in df.columns:
    df = pd.get_dummies(df, columns=['day_of_week'], drop_first=True)

if 'store_location' in df.columns:
    df = pd.get_dummies(df, columns=['store_location'], drop_first=True)

# Drop columns not used in prediction, and set 'total_sales' as target
X = df.drop(columns=['date', 'store_id', 'total_sales'])
y = df['total_sales']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#  Align original columns with test set for report formatting
date_test = original_dates.loc[X_test.index]
store_location_test = original_store_locations.loc[X_test.index]
day_of_week_test = original_day_of_week.loc[X_test.index]

# Fit a linear regression model to the training data
model = LinearRegression()
model.fit(X_train, y_train)

# Use the trained model to predict on the test set
predictions = model.predict(X_test)

# Evaluate the model performance
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

# Print evaluation metrics
print(f"Model Evaluation:\n-------------------\nMSE: {mse:.2f}\nR² Score: {r2:.2f}")

# Save metrics to DataFrame
metrics_df = pd.DataFrame({
    'metric': ['R^2', 'MSE'],
    'value': [r2, mse]
})

# Combine predictions with actual values and error analysis
results = X_test.copy()
results['date'] = date_test.values
results['actual_sales'] = y_test.values
results['predicted_sales'] = predictions
results['prediction_error'] = results['actual_sales'] - results['predicted_sales']
results['abs_error'] = results['prediction_error'].abs()
results['store_location'] = store_location_test.values
results['day_of_week'] = day_of_week_test.values


# Define Export Paths
output_dir = os.path.join("..", "output")
os.makedirs(output_dir, exist_ok=True)

# Export results and metrics to CSV
output_file = "predicted_sales.csv"
metrics_file = "model_metrics.csv"

results.to_csv(os.path.join(output_dir, output_file), index=False)
metrics_df.to_csv(os.path.join(output_dir, metrics_file), index=False)