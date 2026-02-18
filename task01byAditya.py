import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from prophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_squared_error
import seaborn as sns
from datetime import datetime
import matplotlib.ticker as ticker
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import nbformat

print("Developer: Aditya mehta")
print("Project: Sales Forecasting System")

sales_data = pd.read_csv('sales_data_sample.csv', encoding='unicode_escape')
sales_data['ORDERDATE'] = pd.to_datetime(sales_data['ORDERDATE'])

daily_revenue = sales_data.groupby('ORDERDATE')['SALES'].sum().reset_index()
daily_revenue.columns = ['ds', 'y']

forecasting_model = Prophet(yearly_seasonality=True, daily_seasonality=False)
forecasting_model.fit(daily_revenue)

future_dates = forecasting_model.make_future_dataframe(periods=90)
forecast_results = forecasting_model.predict(future_dates)

plt.figure(figsize=(12, 6))
plt.plot(daily_revenue['ds'], daily_revenue['y'], color= "magenta", label='Actual')
plt.plot(forecast_results['ds'], forecast_results['yhat'], color="#0df00d", label='Predicted')
plt.fill_between(forecast_results['ds'], forecast_results['yhat_lower'], forecast_results['yhat_upper'], color='gray', alpha=0.2)
plt.title(f"Analysis by Aashish Ayan")
plt.legend()
plt.show()