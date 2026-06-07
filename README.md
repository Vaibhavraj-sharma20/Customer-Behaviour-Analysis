

#  Customer Behavior Analysis & Weekly Sales Automation 

##  Project Overview

This project simulates the day-to-day responsibilities of a **Data Analyst**. It focuses on analyzing customer purchasing behavior and automating weekly sales reports using **Power BI** and **Python**. The project mimics a real company scenario, complete with tasks, deliverables, and insights.

---

##  Business Objective

> **Goal**: Help the marketing and operations teams understand how customers interact with the platform and where revenue is concentrated — across customer types, product categories, and cities.

Deliverables included:
- Interactive dashboards
- Automated Excel reports
- Business insights from real transaction patterns

---

##  Tools & Technologies Used

| Purpose             | Tools / Tech                        |
|---------------------|-------------------------------------|
| Data Analysis       | Python (pandas, datetime)           |
| Visualization       | Power BI Desktop                    |
| Data Source         | CSV files (simulated from SQL)      |
| Automation Attempt  | Windows Task Scheduler              |
| Reporting Format    | Excel                               |

---

###  Data Acquisition & Preparation
- Collected raw transactional data: `orders.csv` and `products.csv`
- Parsed date fields and merged datasets in Python
- Used `pandas` to structure data by time, product, and geography

###  Dashboard Development (Power BI)
  - Total Orders, Revenue, AOV
  - City-wise and Category-wise summaries
  - Customer loyalty analysis: One-Time vs Repeat
  - Forecasting for order trends (Analytics pane)

 **File**: `Customer Behaviour Dashboard.pbix`

 - Integrated with slicers for real-time filtering

###  Weekly Reporting Automation (Python)
- Created `weekly_report.py` to:
  - Filter last 7 days of sales
  - Aggregate city revenue and top-selling products
  - Export an Excel file with timestamped filenames

 Output Sample: `Weekly_Sales_Report_20250729_2315`

###  Task Scheduler Integration 
- Created a scheduled task to auto-run the script weekly
---

##  How to Run

### Power BI Dashboard
1. Open `Customer Behaviour Dashboard.pbix` in Power BI Desktop
2. Use slicers to filter by:
   - City
   - Customer Type (Repeat / One-Time)
   - Category

### Python Script
1. Ensure `orders.csv` and `products.csv` are in the same folder
2. Run the script from terminal:
   ```
   python weekly_report.py
   ```
3. Output Excel file will be generated with a timestamped name.

---

##  Dashboard Preview

![Customer Behaviour Dashboard](Screenshots/updated-dashboard.png)

This Power BI dashboard allows for:
- Interactive filtering by category, city, and customer type
- Dynamic KPIs
- Forecasting with upper and lower confidence bounds

---

##  Email Communication Samples

These documents simulate professional communication tasks expected from a data analyst when working with stakeholders or cross-functional teams.

-  [Action Plan for Marketing Team](Mailing%20Content/Action%20plan%20for%20marketing%20team.md)
-  [Insight & Recommendation Report](Mailing%20Content/Insight%20%26%20Recommendation%20Report.md)

---

##  Tasks & Learning Roadmap

This project was completed by simulating real-life tasks assigned to a Data Analyst at an eCommerce company. It follows a hands-on, guided approach covering both business and technical workflows.

| Step | Task Description                                                 | Tools / Skills Used                 |
|------|------------------------------------------------------------------|-------------------------------------|
| 1    | Understand business requirements (customer type, revenue, etc.)  | Stakeholder-style briefing          |
| 2    | Analyze data availability & structure                            | SQL (simulated via CSV)             |
| 3    | Calculate customer loyalty metrics (Repeat vs One-time)          | Power BI, DAX, Measures             |
| 4    | Create interactive dashboard with dynamic slicers                | Power BI                            |
| 5    | Implement forecasting in Power BI visual                         | Analytics pane                      |
| 6    | Export summary data to Excel reports                             | Python (pandas, ExcelWriter)        |
| 7    | Filter and generate 7-day dynamic sales summary                  | Python + datetime                   |
| 8    | Save reports with timestamps for archiving                       | File naming automation              |
| 9    | Attempt task automation using Task Scheduler                     | Windows task setup, path debugging  |
| 10   | Review and interpret business insights                           | KPI reading, business storytelling  |

---

