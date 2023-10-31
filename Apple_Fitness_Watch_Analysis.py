import matplotlib.pyplot as plt
import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go
pio.templates.default = 'plotly_white'
import plotly.express as px


data = pd.read_csv('D:/Python Projects/Shruthi/Apple-Fitness-Data.csv')
#print(data.head())

#check if data contains any null values
print(data.isnull().sum())

#Step count over time
fig1 = px.line(data,x='Time',y='Step Count',title='Step count over time')
fig1.show()

#Distance covered over time
fig2 = px.line(data,x='Time',y='Distance',title='Distance covered over time')
fig2.show()

#Energy burned over time
fig3 = px.line(data,x='Time',y='Energy Burned',title='Energy Burned Over Time')
fig3.show()

# Walking Speed Over Time
fig4 = px.line(data, x="Time",y="Walking Speed",title="Walking Speed Over Time")
fig4.show()

#Calculate average step count per day
avg_step_count = data.groupby("Date")['Step Count'].mean().reset_index()
fig5 = px.bar(avg_step_count,x='Date',y='Step Count',title='Average Step Count Per Day')
fig5.update_xaxes(type='category')
fig5.show()

#Create Time intervals
time_interval = pd.cut(pd.to_datetime(data['Time']).dt.hour,bins=[0,12,18,24],labels=['Morning','Afternoon','Night'],right=False)
data['Time Interval'] = time_interval
print(data.head())
fig7 = px.scatter(data, x="Step Count",y="Walking Speed",color="Time Interval",title="Step Count and Walking Speed Variations by Time Interval",trendline='ols')
fig7.show()
