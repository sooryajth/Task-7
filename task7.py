
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

df_csv = pd.read_csv("Online Sales Data.csv")


conn = sqlite3.connect("sales_data.db")


df_csv.to_sql("sales", conn, if_exists="replace", index=False)

# Step 2: Run the SQL query
query = """
SELECT 
    Product_Category AS product, 
    SUM(Units_Sold) AS total_qty, 
    SUM(Total_Revenue) AS revenue 
FROM 
    sales 
GROUP BY 
    Product_Category
"""

df = pd.read_sql_query(query, conn)


conn.close()


print(df)


df.plot(kind='bar', x='product', y='revenue', color='skyblue', edgecolor='black')
plt.title("Revenue by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45)
plt.tight_layout()


plt.savefig("sales_chart.png")


plt.show()