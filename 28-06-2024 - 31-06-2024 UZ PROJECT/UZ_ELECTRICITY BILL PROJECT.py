import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Task 1: Import data from CSV file
data = pd.read_csv('UZ_Electricity_consumption.csv')

# Task 2: Create Monthly Energy Consumption Graphs
data['Date'] = pd.to_datetime(data['Date'] + ' ' + data['Time'], format='%d/%m/%Y %H:%M:%S')
monthly_consumption = data.groupby(pd.Grouper(key='Date', freq='ME'))['Active Power [W]'].sum().reset_index()
monthly_consumption['Active Power (kW)'] = monthly_consumption['Active Power [W]'] / 1000
months = ['Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr']
fig, ax = plt.subplots()
ax.bar(months[6:], monthly_consumption['Active Power (kW)'][6:])
ax.set_title('Monthly Energy Consumption')
ax.set_xlabel('Month')
ax.set_ylabel('Energy Consumption (kWh)')
plt.show(block=False)

# Task 3: Monthly Maximum Demand Graphs
def get_max_demand(month_data):
    month_data = month_data.resample('15min', on='Date')['Active Power [W]'].max()
    return month_data.max() / 1000

monthly_max_demand = monthly_consumption.copy()
monthly_max_demand['Maximum Demand (kW)'] = monthly_max_demand['Date'].apply(lambda x: get_max_demand(data[data['Date'].dt.month == x.month]))
fig, ax = plt.subplots()
ax.bar(months[6:], monthly_max_demand['Maximum Demand (kW)'][6:])
ax.set_title('Monthly Maximum Demand')
ax.set_xlabel('Month')
ax.set_ylabel('Maximum Demand (kW)')
plt.show(block=False)

# Task 4: Monthly Bill Calculation
rates = {'Peak': 0.25, 'Mid-Peak': 0.20, 'Off-Peak': 0.15}
data['Time Zone'] = pd.cut(pd.to_datetime(data['Time'], format='%H:%M:%S').dt.hour, bins=[-1, 7, 17, 24], labels=['Off-Peak', 'Peak', 'Mid-Peak'])
monthly_bill = data.groupby([data['Date'].dt.month, 'Time Zone'])['Active Power [W]'].sum().reset_index()
monthly_bill['Energy Charge'] = monthly_bill.apply(lambda x: (x['Active Power [W]'] / 1000) * rates[x['Time Zone']], axis=1)
monthly_bill = monthly_bill.groupby(level=0).agg({'Energy Charge': sum, 'Active Power [W]': max}).reset_index()
monthly_bill['Maximum Demand Charge'] = (monthly_bill['Active Power [W]'] / 1000) * 10
monthly_bill['Reactive Energy Charge'] = (monthly_bill['Active Power [W]'] / 1000) * 0.05
fig, ax = plt.subplots()
ax.pie([monthly_bill['Energy Charge'].sum(), monthly_bill['Maximum Demand Charge'].sum(), monthly_bill['Reactive Energy Charge'].sum()], labels=['Energy Charge', 'Maximum Demand Charge', 'Reactive Energy Charge'], autopct='%1.1f%%')
ax.set_title('Distribution of Charges')
plt.show(block=False)

# Task 5: Pie Chart for Consumption Pattern
consumption_pattern = data.groupby('Time Zone')['Active Power [W]'].sum().reset_index()
fig, ax = plt.subplots()
ax.pie(consumption_pattern['Active Power [W]'], labels=consumption_pattern['Time Zone'], autopct='%1.1f%%')
ax.set_title('Energy Consumption Pattern')
plt.show(block=False)

# Task 6: Distribution of energy consumption by month in terms of peak, off-peak, and standard
monthly_consumption = data.groupby([data['Date'].dt.month, 'Time Zone'])['Active Power [W]'].sum().reset_index()
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(18, 5))
for i, zone in enumerate(['Off-Peak', 'Peak', 'Mid-Peak']):
    ax[i].bar(months[6:], monthly_consumption[monthly_consumption['Time Zone'] == zone]['Active Power [W]'][6:] / 1000)
    ax[i].set_title(f'Energy Consumption ({zone})')
    ax[i].set_xlabel('Month')
    ax[i].set_ylabel('Energy Consumption (kWh)')
plt.tight_layout()
plt.show(block=False)

power_factor = data.groupby(pd.Grouper(key='Date', freq='ME'))['Power Factor'].mean().reset_index()
fig, ax = plt.subplots()
ax.plot(months[6:], power_factor['Power Factor'][6:])
ax.set_title('Monthly Power Factor')
ax.set_xlabel('Month')
ax.set_ylabel('Power Factor')
plt.show()

print(data.columns)