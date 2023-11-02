import pandas as pd
import plotly.express as px

data = pd.read_csv('D:/Python Projects/Shruthi/supply_chain_data.csv')
print(data.head())
print(data.isnull().sum())

demand = data['Lead times']
supply = data['Manufacturing lead time']

profit = data['Revenue generated'] / data['Shipping costs']+data['Costs']

fig = px.scatter(data,x='Manufacturing lead time',y='Lead times',title='Demand and supply analysis', trendline="ols")
fig.update_layout(xaxis_title='Manufacturing lead time (Supply)',yaxis_title='Lead Time(demand')
fig.show()

# Calculate elasticity
avg_demand = data['Lead times'].mean()
avg_supply = data['Manufacturing lead time'].mean()
pct_change_demand = (max(data['Lead times'])-min(data['Lead times'])*avg_demand)*100
pct_change_supply = (max(data['Manufacturing lead time'])-min(data['Manufacturing lead time'])*avg_supply)*100
elasticity  = round(pct_change_demand/pct_change_supply,2)
print('Elasticity of demand with respect to suppy: ',elasticity)

# Profit based on product type
fig2 = px.pie(data,names='Product type',color=profit,hole=0.4)
fig2.show()