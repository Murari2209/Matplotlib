### Task -1: Line Plot (Sales Trend)
####################################################################################################
import pandas as pd
import matplotlib.pyplot as plt 

## Load the dataset
df = pd.read_csv('sales_data.csv')  
print(df.head())

## convert sales to numeric format
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')

print(df.dtypes)
## convert 'Order Date' column to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)

## extract month from 'Order Date' column
df['Month'] = df['Order Date'].dt.month

## Calculate Monthly Sales
monthly_sales = df.groupby('Month')['Sales'].sum()

## plotting the monthly sales
plt.plot(monthly_sales.index, monthly_sales.values)

# Label
plt.title('Monthly Sales')
plt.xlabel('Month')   
plt.ylabel('Sales')

plt.show()




###################################################################################################### Task -2: Scatter Plot


## In this dataset, i dont have any column which is suitable for scatter plot, so i am using Row ID and Sales for scatter plot.
## Scatter Plot (Sales vs. Row ID)

plt.scatter(df['Row ID'], df['Sales'])
plt.title('Sales vs. Row ID')
plt.xlabel('Row ID')
plt.ylabel('Sales')
plt.show()



###################################################################################################### Task -3: Bar Plot


## aggregate sales by category
category_sales = df.groupby('Category')['Sales'].sum()

# vertical bar plot
plt.bar(category_sales.index, category_sales.values)
plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Sales')
plt.show()


# horizontal bar plot
plt.barh(category_sales.index, category_sales.values)
plt.title('Sales by Category')
plt.xlabel('Sales')
plt.ylabel('Category')
plt.show()



###################################################################################################### Task -4: Multiple bar plot

## extract year from 'Order Date' column
df['Year'] = df['Order Date'].dt.year

# calculate total sales per year
yearly_sales = df.groupby('Year')['Sales'].sum()

years = yearly_sales.index
sales = yearly_sales.values

# multiple bar plot
plt.bar(years, sales)
plt.title('Sales comparison by Year')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.xticks(years)  # Set x-ticks to be the years
plt.show()


###################################################################################################### Task -5: Stacked Bar chart


sales_by_category_year = df.groupby(['Year', 'Category'])['Sales'].sum().unstack()

categories = sales_by_category_year.columns

sales_2016 = sales_by_category_year.loc[2016]
sales_2017 = sales_by_category_year.loc[2017]

plt.bar(categories, sales_2016, label='2016')
plt.bar(categories, sales_2017, bottom=sales_2016, label='2017')
plt.title('Stacked Sales by Category')
plt.xlabel('Category')
plt.ylabel('Sales')
plt.legend()
plt.show()  



###################################################################################################### Task -6: Histogram

plt.hist(df['Sales'], bins=100)
plt.title('Distribution of Sales')  
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()




###################################################################################################### Task -7: Pie Chart

plt.pie(category_sales.values, labels=category_sales.index, autopct='%1.1f%%')
plt.title('Market share by Category')
plt.show()  
