# Sales Data Analysis Report

## Objective
Clean the sales dataset, handle missing values accurately, analyze product-wise performance, and generate clear business insights using **Pandas**.

---

## Dataset Overview
- Records: Sales transactions
- Key Columns:
  - `Product`
  - `Quantity`
  - `Price`
  - `Total_Sales`

---

## Data Cleaning

### Missing Values Handling
To preserve product-level patterns and avoid bias from global statistics, **group-wise median imputation** was applied to the `Quantity` column.

```python
df['Quantity'] = df.groupby('Product')['Quantity'].transform(
    lambda x: x.fillna(x.median())
)
```

**Why this approach?**
- Median is robust to outliers
- Group-wise filling respects product-specific sales behavior
- Maintains original DataFrame shape using `transform()`

### Duplicates
```python
df.drop_duplicates(inplace=True)
```

---

## Sales Analysis

### Revenue Calculation
```python
df['Revenue'] = df['Quantity'] * df['Price']
```

### Total Revenue
```python
total_revenue = df['Revenue'].sum()
```

### Best Performing Product
```python
best_product = (
    df.groupby('Product')['Revenue']
      .sum()
      .idxmax()
)
```

---

## Key Insights
- Group-wise median imputation improved data reliability without distorting trends
- High-priced products generate significant revenue even with lower quantities
- Product-level analysis provides more actionable insights than global aggregation

---

## Conclusion
Using Pandas enabled a **reproducible, accurate, and scalable** analysis workflow. Group-wise median handling ensured fair treatment of missing values, leading to more trustworthy revenue insights.

---

## Tools Used
- Python
- Pandas

---

*This report is suitable for analytics documentation, interviews, and data pipeline references.*

