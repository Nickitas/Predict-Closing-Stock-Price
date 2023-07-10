# -*- coding: utf-8 -*-
"""Predict the closing stock price.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xK9H68ioUFFCkeSiRyKT3GvIPvyCYJmo

# Predict the closing stock price
"""

# Description: This program uses an artificial recurrent network called Long Short Term Memory to predict the closing stock price fo a corporation using the past 60 day stock price

import math
import yfinance as yf
import numpy as np
import pandas as pd
import datetime as dt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#  Get the stock quote
company = 'AAPL'
start = dt.datetime(2020,1,1)
end =  dt.datetime(2022,1,1)
df = yf.download(company, start , end)
df

df.shape

# Visualize the closing price history
plt.figure(figsize=(16, 8))
plt.title('Close Price History')
plt.plot(df['Close'])
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price USD, ($)', fontsize=18)
plt.show()

# Dataframe with only 'Close' column
data = df.filter(['Close'])
dataset = data.values # convert to numpy array
training_data_len = math.ceil(len(dataset) * .8) # get the number of rows to train the model on 80% of datas

training_data_len

#  Scale the data (normalize)
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(dataset)

scaled_data

# Create the training data set
train_data = scaled_data[0:training_data_len , :]
x_train = []
y_train = []

for i in range(60, len(train_data)):
  x_train.append(train_data[i-60:i, 0])
  y_train.append(train_data[i, 0])

  if i <= 61:
    print(x_train)
    print(y_train)
    print('\n')

#  Convert the x_train and y_train to numpy array
x_train, y_train = np.array(x_train), np.array(y_train)

# Reshape the data
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
x_train.shape

# LSTM Modael
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))

# Comile the model
model.compile(
    optimizer='adam',
    loss='mean_squared_error'
)

# Train the model
model.fit(x_train, y_train, batch_size=1, epochs=5)

#  Create the testing data set
test_data = scaled_data[training_data_len - 60: , :]
x_test = []
y_test = dataset[training_data_len:, :]

for i in range(60, len(test_data)):
  x_test.append(test_data[i-60:i, 0])

# Convert the data to numpy array
x_test = np.array(x_test)

# Reshape the data
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

# Get the models predicted price values
predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)

# Get the root mean squared error (RMSE)
rmse = np.sqrt( np.mean(predictions - y_test)**2 )
rmse

# Plot the data
train = data[:training_data_len]
valid = data[training_data_len:]
valid['Predictions'] = predictions

plt.figure(figsize=(16, 8))
plt.title('Model')
plt.xlabel('Data', fontsize=18)
plt.ylabel('Close Price USD ($)', fontsize=18)
plt.plot(train['Close'])
plt.plot(valid[['Close', 'Predictions']])
plt.legend(['Train', 'Val', 'Predictions'], loc='lower right')
plt.show()

# Show the valid and predicted peices
valid

# Get the quote
company = 'AAPL'
start = dt.datetime(2020,1,1)
end =  dt.datetime(2022,1,1)
quote = yf.download(company, start, end)

new_df = quote.filter(['Close'])
last_60_days = new_df[-60:].values
last_60_days_scaled = scaler.transform(last_60_days)

X_test = []
X_test.append(last_60_days_scaled)

X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
pred_price = model.predict(X_test)
pred_price = scaler.inverse_transform(pred_price)

print(pred_price)

# Get the quote
# company = 'AAPL'
# start = dt.datetime(2023,7,1)
# end =  dt.datetime(2023,7,2)
# quote2 = yf.download(company, start, end)
# print(quote2['Close'])