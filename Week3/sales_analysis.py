import pandas as pd

#Reading csv file
df = pd.read_csv("D:\\Data_science\\Developers_Arena\\Week3\\sales_data.csv")
#print(csv_1)

print("\nFirst 3 Rows:")
print(df.head(3))

#Check missing values
print("Missing values:\n")
print(df.isnull().sum())

#Handle missing values
df['Quantity'].fillna(df['Quantity'].median())
df['Product'].fillna(df['Product'].mode()[0])


#Remove duplicate records
df.drop_duplicates(inplace=True)


#Calculate Total Revenue
total_revenue = df['Total_Sales'].sum()
print("Total Revenue:", total_revenue)

#Find Best-Selling Product (by Revenue)
product_revenue = df.groupby('Product')['Total_Sales'].sum()
best_product = product_revenue.idxmax()

print(product_revenue)
print("Best Product:", best_product)

#Top 5 Products by Revenue
top_products = product_revenue.sort_values(ascending=False)
print(top_products)

#Revenue by Region (Extra Insight)
region_sales = df.groupby('Region')['Total_Sales'].sum()
print(region_sales)

#Create Report
df['Revenue_Check'] = df['Quantity'] * df['Price']

#Summary Report DataFrame
report = pd.DataFrame({
    'Metric': ['Total Revenue', 'Best Product'],
    'Value': [total_revenue, best_product]
})

print(report)

#Key Business Insights
print("INSIGHTS:")
print(f"- Total revenue generated: ₹{total_revenue:,}")
print(f"- Best performing product: {best_product}")
print(f"- {best_product} contribute the highest revenue")

