import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('Sample - Superstore.csv',encoding = 'latin-1')

print(df.head())
df.describe()
df.info()
df['Order Date']=pd.to_datetime(df['Order Date'])
df['Ship Date']=pd.to_datetime(df['Ship Date'])
df['Order Month']=df['Order Date'].dt.month
df['Order Year']=df['Order Date'].dt.year
df['Order Day of Week']=df['Order Date'].dt.dayofweek
print(df.head())

#Monthly Sales Analysis
sales_by_month= df.groupby('Order Month')['Sales'].sum().reset_index()
plt.figure(figsize=(10,6))
plt.plot(sales_by_month['Order Month'],sales_by_month['Sales'])
plt.title('Monthly Sales Analysis')
plt.xlabel('Order Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

#Sales By Category
sales_by_category= df.groupby('Category')['Sales'].sum().reset_index()
plt.figure(figsize=(8,8))
plt.pie(sales_by_category['Sales'],labels=sales_by_category['Category'],autopct='%1.1f%%',startangle=90)
plt.title('Sales Analysis By Category')
plt.show()

#Sales By SubCategory
sales_by_subcategory= df.groupby('Sub-Category')['Sales'].sum().reset_index()
plt.figure(figsize=(10,6))
plt.bar(sales_by_subcategory['Sub-Category'],sales_by_subcategory['Sales'])
plt.xlabel('Sub-Category')
plt.ylabel('Sales')
plt.title('Sales Analysis By SubCategory')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Monthly Profit Analysis
profit_by_month = df.groupby('Order Month')['Profit'].sum().reset_index()
plt.figure(figsize=(10,6))
plt.plot(profit_by_month['Order Month'],profit_by_month['Profit'])
plt.title('Monthly Profit Analysis')
plt.xlabel('Order Month')
plt.ylabel('Profit')
plt.show()

#Profit By Category
profit_by_category= df.groupby('Category')['Profit'].sum().reset_index()
plt.figure(figsize=(8,8))
plt.pie(profit_by_category['Profit'],labels=profit_by_category['Category'],autopct='%1.1f%%',startangle=90)
plt.title('Profit Analysis By Category')
plt.show()

#profit By SubCategory
profit_by_subcategory= df.groupby('Sub-Category')['Profit'].sum().reset_index()
plt.figure(figsize=(10,6))
plt.bar(profit_by_subcategory['Sub-Category'],profit_by_subcategory['Profit'])
plt.xlabel('Sub-Category')
plt.ylabel('Profit')
plt.title('Profit Analysis By SubCategory')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Sales and Profit Analysis By Customer Segment
sales_profit_by_segment= df.groupby('Segment').agg({'Sales':'sum','Profit':'sum'}).reset_index()
fig,ax =plt.subplots(figsize=(10,6))
bar_width=0.35
index=np.arange(len(sales_profit_by_segment['Segment']))
ax.bar(index,sales_profit_by_segment['Sales'],bar_width,label='Sales')
ax.bar(index+bar_width,sales_profit_by_segment['Profit'],bar_width,label='Profit')
ax.set_xlabel('Customer Segment')
ax.set_ylabel('Amount')
ax.set_title('Sales and Profit Analysis By Customer Segment')
ax.set_xticks(index + bar_width/2)
ax.set_xticklabels(sales_profit_by_segment['Segment'])
ax.legend()
plt.tight_layout()
plt.show()

#Sales to Profit Ratio
sales_profit_by_segment= df.groupby('Segment').agg({'Sales':'sum','Profit':'sum'}).reset_index()
sales_profit_by_segment['sales_to_profit_ratio']=sales_profit_by_segment['Sales']/sales_profit_by_segment['Profit']
print(sales_profit_by_segment[['Segment','sales_to_profit_ratio']])