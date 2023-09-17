import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

diabetes_df = pd.read_csv('../data/diabetes_clean.csv')
print(diabetes_df.head())

X = diabetes_df.drop("glucose", axis=1).values
y = diabetes_df["glucose"].values

X_bmi = X[:, 3]
print(y.shape, X_bmi.shape)

X_bmi = X_bmi.reshape(-1, 1)
print(X_bmi.shape)

plt.scatter(X_bmi, y)
# plt.ylabel("Blood Glucose (mg/dl)")
# plt.xlabel("Body Mass Index")
# plt.show()

reg = LinearRegression()
reg.fit(X_bmi, y)
predictions = reg.predict(X_bmi)
plt.plot(X_bmi, predictions, color='black')
plt.ylabel("Blood Glucose (mg/dl)")
plt.xlabel("Body Mass Index")
plt.show()
