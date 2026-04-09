# Coffee Sales Dashboard Project ☕📊

This project demonstrates **end-to-end data analysis and dashboard creation** for a coffee shop, using **Python, Excel, and Power BI**.  
It covers everything from raw sales data to interactive visualizations, highlighting top-selling coffee types, city-wise revenue, and sales trends.

---

## 📁 Project Files

### 1. Python Script
**`coffee_dashboard_analysis.py`**  
- Loads and processes the coffee sales dataset from Excel (`coffee_data.xlsx`)  
- Calculates **Total Sales** for each coffee type  
- Groups and summarizes data by **Coffee Type, City, and Date**  
- Outputs cleaned and aggregated data ready for **dashboard visualization**  

**Libraries Used:**
- `pandas`  
- `numpy`  
- `matplotlib` / `seaborn` (optional for local plots)  

---

### 2. Excel Dataset
**`coffee_data.xlsx`**  
Contains sales records for the coffee shop.

**Columns:**
- `Date` → Date of sale  
- `Coffee_Type` → Type of coffee sold (Espresso, Latte, Cappuccino, etc.)  
- `Quantity` → Number of units sold  
- `Price` → Price per unit  
- `City` → City where the sale occurred  

**Purpose:**
- Input dataset for Python analysis  
- Provides real-world data for **Power BI dashboards**  
- Enables visualization of **top-selling coffee types, total revenue, and city-wise trends**

---

## 📊 Power BI Dashboard

You can view the interactive **Coffee Sales Dashboard** here:

[Open Dashboard in Power BI](https://app.powerbi.com/links/zt6a76Y0jp?ctid=f4129d1d-77c1-46e4-a2c6-11923930d023&pbi_source=linkShare)

**Features:**
- Top coffee types and revenue trends  
- City-wise sales analysis  
- Forecasting and KPI cards  
- Animated and interactive visuals for better insights  

---

## ⚡ How to Run Python Script
1. Install required libraries:
```bash
pip install pandas numpy matplotlib openpyxl
