import pandas as pd
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go
pio.templates.default = 'plotly_white'

data = pd.read_csv('D:/Python Projects/Shruthi/customer_acquisition_cost_dataset.csv')
#print(data.head())
#print(data.info())
#print(data.describe())

#Calculating customer Acquisation cost
data['CAC'] = data['Marketing_Spend']/data['New_Customers']
'''fig1 = px.bar(data,x='Marketing_Channel',y='CAC',title='CAC by Marketing channel')
fig1.show()
print(data['CAC'])'''

#fig2 = px.scatter(data,x='New_Customers',y='CAC',color='Marketing_Channel',title='New Customers vs. CAC',trendline='ols')
#fig2.show()

#calculate conversion rate of marketing campaign
data['Conversion_Rate'] = data['New_Customers'] / data['Marketing_Spend'] * 100
# Conversion Rates by Marketing Channel
'''fig = px.bar(data, x='Marketing_Channel',
             y='Conversion_Rate',
             title='Conversion Rates by Marketing Channel')
fig.show()
'''
data['Break_Even_Customers'] = data['Marketing_Spend'] / data['CAC']
'''
fig = px.bar(data, x='Marketing_Channel',
             y='Break_Even_Customers',
             title='Break-Even Customers by Marketing Channel')
fig.show()
'''
#compare the actual customers acquired with the break-even customers for each marketing channel
fig = go.Figure()

# Actual Customers Acquired
fig.add_trace(go.Bar(x=data['Marketing_Channel'], y=data['New_Customers'],name='Actual Customers Acquired', marker_color='royalblue'))
# Break-Even Customers
fig.add_trace(go.Bar(x=data['Marketing_Channel'], y=data['Break_Even_Customers'],name='Break-Even Customers', marker_color='lightcoral'))
# Update the layout
fig.update_layout(barmode='group', title='Actual vs. Break-Even Customers by Marketing Channel',
                  xaxis_title='Marketing Channel', yaxis_title='Number of Customers')
fig.show()

