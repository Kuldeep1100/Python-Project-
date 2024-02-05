#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import datetime
from datetime import date , timedelta

import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio

pio.templates.default = "plotly_white"


# In[3]:


data = pd.read_csv('TWTR.csv')
print(data.head())

print(data.tail())


# In[4]:


print(data.info())


# In[6]:


print(data.isnull().sum())


# In[8]:


data = data.dropna()
print(data)


# #Twitter Stock Market Prices Over the Years

# In[11]:



figure = go.Figure(data=[go.Candlestick(x = data["Date"] , 
                                       open = data["Open"] ,
                                       high = data["High"] , 
                                       low = data["Low"] , 
                                       close = data["Close"])])

figure.update_layout(title = "Twitter Stock Market Prices Over the Years" , 
                    xaxis_rangeslider_visible = False)

figure.show()


# In[12]:


figure = px.bar(data , 
               x = "Date" , 
               y = "Close" , 
               color = "Close")

figure.update_xaxes(rangeslider_visible = True)
figure.show()


# In[13]:


figure = px.bar(data , 
               x = "Date" , 
               y = "Open" , 
               color = "Open")

figure.update_xaxes(rangeslider_visible = True)
figure.show()


# In[16]:


figure = px.bar(data , 
               x = "Date" , 
               y = "Open" , 
               color = "Open")

figure.update_xaxes(rangeslider_visible = True)
figure.update_layout(title = "Twitter Stock Prices Over the Years" , 
                    xaxis_rangeslider_visible = False)

figure.update_xaxes(
    rangeselector = dict(
        buttons = list([
            
            dict(count =1  , label = "1m" , step="month" , stepmode = "backward") , 
            dict(count =6  , label = "6m" , step="month" , stepmode = "backward") ,
            dict(count =3  , label = "3m" , step="month" , stepmode = "backward") ,
            dict(count =1  , label = "1y" , step="year" , stepmode = "backward") ,
            dict(count =2  , label = "2y" , step="year" , stepmode = "backward") , 
            dict(step = "all")
            
            
        ])
    )
)
figure.show()


# In[22]:


data["Date"] = pd.to_datetime(data["Date"] , format = '%Y-%m-%d')

data["Year"] = data['Date'].dt.year

data["Month"] = data['Date'].dt.month


# In[29]:


fig = px.line(data , 
             x = "Month" , 
             y = "Close" , 
             color = "Month" , 
             title = "Complete Timeline of Twitter Stock Market")

fig.show()


# In[27]:


fig = px.line(data , 
             x = "Date" , 
             y = "Open" , 
             color = "Year" , 
             title = "Complete Timeline of Twitter Stock Market")

fig.show()


# In[28]:


fig = px.line(data , 
             x = "Month" , 
             y = "Open" , 
             color = "Year" , 
             title = "Complete Timeline of Twitter Stock Market")

fig.show()


# In[32]:


import statistics as st
from statsmodels.stats import weightstats as stests


opens = data['Open']
print('Data = ' ,opens)

open_mean = st.mean(opens)
print('Mean of Opening day of the share :' , open_mean)

std_open = st.stdev(opens)
print("Standard deviation  of the Open Share:"  , std_open)


ztest  , pval = stests.ztest(opens , value = 30)
print('Z-test Score' , ztest)

print("P-Value:" ,pval)


alpha = 0.05
if(pval<alpha):
    print("Reject the null hypothesis")
    
else:
    print("Accept the Null hypothesis")
    
    
    


# In[34]:



from scipy.stats import ttest_1samp
import statistics as st
#from statsmodels.stats import weightstats as stests


opens = data['Open']
print('Data = ' ,opens)

open_mean = st.mean(opens)
print('Mean of Opening day of the share :' , open_mean)

std_open = st.stdev(opens)
print("Standard deviation  of the Open Share:"  , std_open)


ttest  , pval = ttest_1samp(opens , 30)
print('Z-test Score' , ztest)

print("P-Value:" ,pval)


alpha = 0.05
if(pval<alpha):
    print("Reject the null hypothesis")
    
else:
    print("Accept the Null hypothesis")
    


# In[38]:


from scipy.stats import chisquare

datas = data[['Open' , 'Close']]


print(datas)
chisq  , p = chisquare(datas)
print("P-Value:" ,p)
print('Chi-Square:' , chisq)


alpha = 0.05
if(pval<alpha):
    print("Reject the null hypothesis")
    
else:
    print("Accept the Null hypothesis")
    


# In[50]:


import scipy.stats
opens = pd.unique(data.Open.values)
print(opens)

#data = {opens:data['Open'][data.opens = Open] for opens in opens}
opens = data['Open']
print(opens.head())

close = data['Close']
print(close.head())

high = data['High']
print(high.head())

low = data['Low']
print(low .head())


datas  = data[['Open',  'Close', 'High' , 'Low']]
print(datas.head(10))

F , p = scipy.stats.f_oneway(data['Open'] , data['Close'] ,data['High'] , data['Low'])
print('F-Value :' ,F)

print('P-Value:' , p)


# In[51]:



import matplotlib.pyplot as plt
fig = plt.figure(figsize = (10 , 10))
ax = plt.axes(projection = '3d')
ax.scatter3D(data['Open'] , data['Close']  , data['High'] ,edgecolor = 'black');
ax.set_xlabel('Open')
ax.set_ylabel('Close')
ax.set_zlabel('High')
plt.show()



# In[52]:


import plotly.figure_factory as ff
import numpy as np

np.random.seed(1)
X = np.random.rand(15 , 12)

fig = ff.create_dendrogram(X)

fig.update_layout({'plot_bgcolor':'White'})

fig.show()



# In[ ]:




