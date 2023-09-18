import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pylab import *
import plotly.express as px
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator


data = pd.read_csv("D:/Python Projects/Shruthi/Data_Insta/Instagram data.csv", encoding='latin1')
#print(data.head())
#print(data.isnull().sum())
#If null found in your data next step is to drop null
#data=data.dropna()   # optional
#data.info()   #information on data collected

######Lets Analyse impressions from Home tab in insta#######
sns.set(rc={"figure.figsize": (8, 4)})
plt.title("Distribution of impression from Home")
ax = sns.distplot(data['From Home'])
plt.show()

######Lets Analyse impressions from Hashtags tab in insta#######
sns.set(rc={"figure.figsize": (8, 4)})
plt.title("Distribution of impression from Hashtags")
a = sns.distplot(data['From Hashtags'])
plt.show()

######Lets Analyse impressions from Explorer tab in insta#######
sns.set(rc={"figure.figsize": (8, 4)})
plt.title("Distribution of impression from Explorer")
b = sns.distplot(data['From Explore'])
plt.show()

#######Percentage of Impressions from various sources#############
Home = data["From Home"].sum()
Hashtags = data["From Hashtags"].sum()
Explore = data["From Explore"].sum()
Other = data["From Other"].sum()

labels = ['From Home','From Hashtags','From Explore','Other']
values = [Home, Hashtags, Explore, Other]

fig = px.pie(data, values=values, names=labels, title='Percentage of Impressions from various sources',hole=0.5)
fig.show()


##########Analyze most used words in insta caption############
text = " ".join(i for i in data.Caption)
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
plt.style.use('classic')
plt.figure(figsize=(12,10))
plt.imshow(wordcloud, interpolation='bilinear')   #bilinear provides better reading that check for near pixes
plt.axis("off")
plt.show()


####Analyze most used word in Hashtags##########3
text = " ".join(i for i in data.Hashtags)
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color='white').generate(text)
plt.style.use('classic')
plt.figure(figsize=(15,13))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


#analyze relationship between likes and impression#
figure = px.scatter(data_frame=data,x="Impressions",y="Likes",size="Likes",trendline='ols',title="Relationship Between Likes and Impressions")
figure.show()
#analyze relationship between Comments and impression#
figure = px.scatter(data_frame=data,x="Impressions",y="Comments",size="Comments",trendline='ols',title="Relationship Between comments and Impressions")
figure.show()

#########Analyzing Conversion Rate###########
conversion_rate = (data["Follows"].sum() / data["Profile Visits"].sum()) * 100
print(conversion_rate)
figure = px.scatter(data_frame = data, x="Profile Visits",
                    y="Follows", size="Follows", trendline="ols",
                    title = "Relationship Between Profile Visits and Followers Gained")
figure.show()
figure = px.scatter(data_frame=data,x="Impressions",y="Shares",size="Shares",trendline='ols',title="Relationship Between Shares and Impressions")
figure.show()