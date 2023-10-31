#RFM stands for recency, frequency, and monetary value, which are three key metrics that provide information about customer engagement, loyalty, and value to a business.
'''recency (the date they made their last purchase)
frequency (how often they make purchases)
and monetary value (the amount spent on purchases)'''
import pandas as pd
import plotly.express as px
import plotly.io as pio
import numpy as np
pio.templates.default ='plotly_white'

data = pd.read_csv("D:/Python Projects/Shruthi/rfm_data.csv")
#print(data.head())

#Calculate Recency,Frequency and Monetary values
from datetime import datetime

#convert PurchaseDate to datetime
data['PurchaseDate'] = pd.to_datetime(data['PurchaseDate'])

#Calculate Recency
data['Recency'] = (datetime.now().date() - data['PurchaseDate'].dt.date)  / np.timedelta64(1, 'D')

#Calculate Frequency
freq_data = data.groupby('CustomerID')['OrderID'].count().reset_index()
freq_data.rename(columns={'OrderID':'Frequency'},inplace=True)
data = data.merge(freq_data,on='CustomerID',how='left')

#Calculate Monetary value
monetary_data = data.groupby('CustomerID')['TransactionAmount'].count().reset_index()
monetary_data.rename(columns={'TransactionAmount': 'MonetaryValue'}, inplace=True)
data = data.merge(monetary_data,on='CustomerID',how='left')
print(data.head())

#Define scoring criteria for each RFM value
recency_score = [5,4,3,2,1]
freq_score = [1,2,3,4,5]
monetary_score = [1,2,3,4,5]

#calculate RFM score
data['RecencyScore'] = pd.cut(data['Recency'], bins=5, labels=recency_score)
data['FrequencyScore'] = pd.cut(data['Frequency'], bins=5, labels=freq_score)
data['MonetaryScore'] = pd.cut(data['MonetaryValue'], bins=5, labels=monetary_score)

# Convert RFM scores to numeric type
data['RecencyScore'] = data['RecencyScore'].astype(int)
data['FrequencyScore'] = data['FrequencyScore'].astype(int)
data['MonetaryScore'] = data['MonetaryScore'].astype(int)

# Calculate RFM score by combining the individual scores
data['RFM_Score'] = data['RecencyScore'] + data['FrequencyScore'] + data['MonetaryScore']

#Create RFM segment based on RFM score
label = ['Low-value','Mid-Value','High-value']
data['Value Segment'] = pd.qcut(data['RFM_Score'],q=3,labels=label)

#print(data.head())
# RFM Segment Distribution
segment_counts = data['Value Segment'].value_counts().reset_index()
segment_counts.columns = ['Value Segment', 'Count']

pastel_colors = px.colors.qualitative.Pastel

# Create the bar chart
fig_segment_dist = px.bar(segment_counts, x='Value Segment', y='Count',
                          color='Value Segment', color_discrete_sequence=pastel_colors,
                          title='RFM Value Segment Distribution')

# Update the layout
fig_segment_dist.update_layout(xaxis_title='RFM Value Segment',
                              yaxis_title='Count',
                              showlegend=False)

# Show the figure
fig_segment_dist.show()

# Create a new column for RFM Customer Segments
data['RFM Customer Segments'] = ''

# Assign RFM segments based on the RFM score
data.loc[data['RFM_Score'] >= 9, 'RFM Customer Segments'] = 'Champions'
data.loc[(data['RFM_Score'] >= 6) & (data['RFM_Score'] < 9), 'RFM Customer Segments'] = 'Potential Loyalists'
data.loc[(data['RFM_Score'] >= 5) & (data['RFM_Score'] < 6), 'RFM Customer Segments'] = 'At Risk Customers'
data.loc[(data['RFM_Score'] >= 4) & (data['RFM_Score'] < 5), 'RFM Customer Segments'] = "Can't Lose"
data.loc[(data['RFM_Score'] >= 3) & (data['RFM_Score'] < 4), 'RFM Customer Segments'] = "Lost"

# Print the updated data with RFM segments
print(data[['CustomerID', 'RFM Customer Segments']])

segment_product_counts = data.groupby(['Value Segment', 'RFM Customer Segments']).size().reset_index(name='Count')

segment_product_counts = segment_product_counts.sort_values('Count', ascending=False)

fig_treemap_segment_product = px.treemap(segment_product_counts,
                                         path=['Value Segment', 'RFM Customer Segments'],
                                         values='Count',
                                         color='Value Segment', color_discrete_sequence=px.colors.qualitative.Pastel,
                                         title='RFM Customer Segments by Value')
fig_treemap_segment_product.show()
