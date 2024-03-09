# Kutty Package

Kutty is a Python package developed for simplifying the processes of data cleaning, visualization, and time series analysis. It aims to provide user-friendly interfaces for handling missing values, detecting and treating outliers, creating interactive visualizations, and conducting comprehensive analysis on time series data.

## Installation

To install Kutty, ensure you have Python and pip installed on your system. Then, run the following command:

```sh
pip install kutty
```

## Features

Kutty is composed of three main modules:

### Cleaning Module

- **handle_missing_values_advanced**: Automatically handles missing values in a DataFrame using various strategies including mean, median, mode, and dropping missing values.
- **detect_and_treat_outliers**: Detects and treats outliers in a DataFrame using Z-score or IQR methods.

### Visualization Module

- **create_interactive_scatter_advanced**: Generates an interactive scatter plot with extensive customization options.
- **create_interactive_time_series**: Creates an interactive time series plot, allowing for the highlighting of significant data points.

### Time Series Module

- **calculate_moving_average**: Calculates moving averages, supporting simple, weighted, and exponential types.
- **detect_anomalies**: Identifies anomalies in time series data using a simple statistical approach.

## Usage

Here's how to use the Kutty package in your Python projects:

```python
from kutty.cleaning import handle_missing_values_advanced, detect_and_treat_outliers
from kutty.visualization import create_interactive_scatter_advanced, create_interactive_time_series
from kutty.timeseries import calculate_moving_average, detect_anomalies

import pandas as pd

# Loading your dataset
df = pd.read_csv('your_dataset.csv')

# Cleaning Data
df_cleaned = handle_missing_values_advanced(df, strategy='mean')
df_no_outliers = detect_and_treat_outliers(df_cleaned, method='z_score', threshold=3)

# Visualization
create_interactive_scatter_advanced(df_no_outliers, 'x_column', 'y_column', 'color_column')
create_interactive_time_series(df_no_outliers, 'time_column', 'value_column', title='My Time Series Plot')

# Time Series Analysis
moving_average = calculate_moving_average(df_no_outliers['your_time_series_column'], window=10, type='simple')
anomalies = detect_anomalies(df_no_outliers['your_time_series_column'])
```

Enhancements and New Features
-----------------------------

1. Cleaning Module Enhancements:

   - preprocess_data_for_ml: Function introduced for preprocessing data, including feature scaling and
     encoding, preparing the dataset for machine learning models.

2. Visualization Module Enhancements:

   - create_multi_variable_plot: Function for creating complex plots that visualize relationships between
     multiple variables.

3. Time Series Module Enhancements:

   - arima_forecast: A new function is added for time series forecasting using the ARIMA model.
   - prophet_forecast: Function introduced for forecasting using the Prophet model, suitable for datasets
     with strong seasonal effects.

Usage
-----

Here are brief examples showing how to use the new functionalities:

# Preprocess data for machine learning
from kutty.cleaning import preprocess_data_for_ml
df_processed = preprocess_data_for_ml(df)

# Create a multi-variable plot
from kutty.visualization import create_multi_variable_plot
create_multi_variable_plot(df, 'category_column', ['feature1', 'feature2', 'feature3'])

# Forecasting with ARIMA
from kutty.timeseries import arima_forecast
forecast = arima_forecast(series, order=(1, 1, 1), steps=5)

# Forecasting with Prophet
from kutty.timeseries import prophet_forecast
forecast_df = prophet_forecast(df[['ds', 'y']], periods=5, freq='D')

Dependencies
------------

Kutty depends on the following Python libraries: pandas, scipy, numpy, plotly, statsmodels, sklearn, and fbprophet. Ensure these are installed in your environment.

## Contributing

Contributions to the Kutty package are welcome! Please feel free to fork the repository, make your changes, and submit a pull request.

## License

Kutty is released under the MIT License. See the LICENSE file in the project repository for more details.