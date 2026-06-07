import os
from datetime import datetime, timedelta
import pandas as pd

with open("log.txt", "a") as f:
    f.write(f"Script ran at: {datetime.now()}\n")

# Load data
orders = pd.read_csv(r'C:\Users\ashis\OneDrive\문서\Projects\Novakart Pvt Ltd\orders.csv', parse_dates=['order_date'])
products = pd.read_csv(r'C:\Users\ashis\OneDrive\문서\Projects\Novakart Pvt Ltd\products.csv')

df = pd.merge(orders, products, on='product_id', how='left')

# Filter last 7 days
today = datetime.today()
last_week = today - timedelta(days=7)
df_last_week = df[df['order_date'] >= last_week]

# Summaries
city_summary = df_last_week.groupby('city')['revenue'].sum().sort_values(ascending=False)
top_products = df_last_week.groupby(['product_id', 'category'])['revenue'].sum().sort_values(ascending=False).head(5)

# Save to known directory
timestamp = datetime.now().strftime("%Y%m%d_%H%M")
output_dir = r'C:\Users\ashis\Documents\Reports'
os.makedirs(output_dir, exist_ok=True)
filename = os.path.join(output_dir, f"Weekly_Sales_Report_{timestamp}.xlsx")

with pd.ExcelWriter(filename) as writer:
    city_summary.to_frame(name='Revenue').to_excel(writer, sheet_name='City Summary')
    top_products.to_frame(name='Revenue').to_excel(writer, sheet_name='Top Products')

print(f"Report saved successfully at: {filename}")