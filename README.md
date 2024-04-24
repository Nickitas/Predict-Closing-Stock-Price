# Predicting Closing Stock Price using Long Short Term Memory (LSTM) Network

## Description

This program utilizes an artificial recurrent neural network known as Long Short Term Memory (LSTM) to predict the closing stock price of a corporation based on the past 60 days' stock prices.

## Usage

- Ensure you have the necessary libraries installed: `yfinance`, `numpy`, `pandas`, `scikit-learn`, `keras`, and `matplotlib`.
- Adjust the parameters such as the company ticker symbol, start and end dates for data retrieval, and model training epochs if necessary.
- Run the program to fetch historical stock price data, preprocess the data, build and train the LSTM model, make predictions, and visualize the results.

## Requirements

- Python 3.x
- yfinance
- numpy
- pandas
- scikit-learn
- keras
- matplotlib

## How to Use

1. Set the desired company ticker symbol, start date, and end date for data retrieval.
2. Run the program to train the LSTM model using historical stock price data.
3. The model will then predict the closing stock prices for the specified company.
4. Visualizations of the historical and predicted stock prices will be displayed.

## Example

```python
# Set the company ticker symbol and date range
company = 'AAPL'
start = dt.datetime(2020, 1, 1)
end =  dt.datetime(2022, 1, 1)

# Fetch historical stock price data
df = yf.download(company, start, end)

# Train the LSTM model and make predictions
# ...

# Visualize the historical and predicted stock prices
# ...
```

## Acknowledgements
This program was adapted from a Colab notebook available here.
The LSTM model implementation is based on the Keras library.
