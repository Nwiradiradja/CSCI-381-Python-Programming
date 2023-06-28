import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv('data.csv') # load data set

# Filter out rows with non-numeric values in the second column
data = data.apply(pd.to_numeric, errors='coerce').dropna()

X = data.iloc[:, 1].values.reshape(-1, 1)  # values converts it into a numpy array
Y = data.iloc[:, 0].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column

linear_regressor = LinearRegression()  # create object for the class
linear_regressor.fit(X, Y)  # perform linear regression
Y_prediction = linear_regressor.predict(X)  # make predictions

plt.scatter(X, Y)
plt.plot(X, Y_prediction, color='red')
plt.xlabel('Years')
plt.ylabel('ANOMALY(1901-2000 BASE PERIOD)')
plt.title('Sea Level over Time 1880-2015 (in mm)')
fig1 = plt.gcf()
plt.show()
