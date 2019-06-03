import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
import Matplotlib.pyplot as plt
dataset = pd.read_csv(’Salary_Data.csv’)
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[’:,1].values
X_train, X_test, y_train, y_test = train test split(x, y, test_size = 1/3, random_state �= 0)
Regressor = LinearRegression()
Regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
plt.scatter(X_train, y_train, color = color)
plt.plot(X_train, regressor.predict(X_train), color =‘blue’)
plt.show()