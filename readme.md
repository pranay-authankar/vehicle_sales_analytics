# 🚗 Vehicle Sales Analytics

### Exploring vehicle sales, pricing, companies, sellers, and market patterns through data.

This project is an end-to-end **data analytics exploration of vehicle sales data**, covering data cleaning, exploratory analysis, visualization, and business intelligence.

The project follows:

**Clean → Explore → Analyze → Visualize → Understand**

---

## 🔍 What This Project Explores

* 📈 Sales and revenue trends
* 🚘 Vehicle age, condition, mileage, make, model, and body type
* 💰 MMR vs actual selling price
* 🏢 Company and seller performance
* 🌎 State-wise and regional sales patterns
* 📊 Relationships between vehicle characteristics and pricing

---

## 🧹 Data Preparation

The dataset was prepared before analysis by:

* Handling missing values
* Investigating missing `body`, `transmission`, and `condition`
* Removing duplicate VIN records
* Converting `saledate` into datetime format
* Creating a **vehicle age** feature
* Investigating unusual values and data inconsistencies

---

## 📊 Exploratory Data Analysis

The main analytical work was performed using **Python, Pandas, NumPy and Matplotlib**.

The analysis covers:

### Sales & Market

* Annual revenue and units sold
* Top companies and sellers
* State-wise sales
* Body-type distribution

### Vehicle Analysis

* Vehicle age
* Condition
* Make & model
* Odometer
* Body type
* Year-wise patterns

### Pricing Analysis

* MMR vs selling price
* Price gap analysis
* Selling price by vehicle age
* Selling price by condition
* Selling price by odometer range

### Company & Seller Analysis

* Top companies by sales and revenue
* Top sellers by sales and revenue
* Company–seller relationships
* Seller performance across states

---

## 💰 MMR vs Selling Price

One of the key parts of the project is comparing:

**MMR** → market/reference valuation
**Selling Price** → actual recorded transaction price

The analysis also uses:

```text
Price Gap = Selling Price − MMR
```

This helps explore vehicles selling **above, near, or below their MMR**.

> The price gap is not profit; it only represents the difference between selling price and MMR.

---

## 📈 Visualizations

The `charts/` folder contains the **Matplotlib visualizations created during the analysis**.

These charts provide the visual evidence behind the patterns explored in the notebook.

👉 **[Explore the charts](charts/)**

---

## 📓 Analysis Notebook

The `notebook/` folder contains the main analytical workflow — from data inspection and cleaning to exploration and visualization.

👉 **[Explore the notebook](notebook/)**

---

## 📊 Power BI Dashboard

The analysis was also transformed into a **4-page Power BI dashboard**:

1. **Executive Overview**
2. **Vehicle & Market Analysis**
3. **Company & Seller Analysis**
4. **Pricing & Valuation Analysis**

Because the Power BI report cannot currently be published online, **dashboard screenshots are included in the `powerBI/` folder**.

👉 **[Explore the Power BI dashboard](powerBI/)**

---

## 🛠️ Tech Stack

**Python · Pandas · NumPy · Matplotlib · Jupyter Notebook · Power BI · DAX · GitHub**

---

## 📁 Repository Structure

```text
vehicle_sales_analytics/
│
├── charts/        → Matplotlib visualizations
├── notebook/      → Analysis & data preparation
├── powerBI/       → Power BI dashboard screenshots
├── text_files/    → Supporting project files
└── README.md
```

---

### 👨‍💻 Built by Pranay Authankar

**Data Analytics | Python | Data Visualization | Power BI**

> **The charts show the patterns. The notebook explains them. The dashboard brings them together.**
