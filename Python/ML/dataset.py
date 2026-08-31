import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression as LR

# Fetches datas
df = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/manhattan.csv")

# Define data points
x = df[["bedrooms", "bathrooms", "size_sqft", "min_to_subway", "floor", "building_age_yrs", "no_fee", "has_roofdeck",
        "has_washer_dryer", "has_doorman", "has_elevator", "has_dishwasher", "has_patio", "has_gym"]]
y = df[["rent"]]

# Split data
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, test_size = 0.2, random_state = 6)

# Train model and display the result
mlr = LR()
mlr.fit(x_train, y_train)
y_predict = mlr.predict(x_test)
print(f"Predicted rent: ${y_predict[0][0]:.2f}")

plt.axis()
plt.xlabel("Prices")
plt.ylabel("Predicted prices")
plt.title("Actual Rent vs Predicted Rent")

plt.scatter(y_test, y_predict, alpha = 0.4)
plt.show()