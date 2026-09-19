# 🚗 Vehicle Sales Analytics

### From raw vehicle transactions to meaningful market insights.

This project explores a large vehicle sales dataset to understand **sales trends, vehicle characteristics, pricing, companies, sellers, and market behavior**.

Rather than jumping straight into a dashboard, the project focuses on the complete analytics workflow:

**Clean → Explore → Analyze → Visualize → Interpret**

---

## 🔍 What I Explored

The analysis investigates questions such as:

* Which companies and sellers sell the most vehicles?
* Which companies generate the highest revenue?
* How does **vehicle age** affect sales, revenue, and condition?
* How does **odometer reading** relate to selling price?
* How closely does **MMR** compare with the actual selling price?
* Which states and body types dominate the market?
* How do vehicle **condition and age** relate to pricing?

---

## 🧹 Data Cleaning & Preparation

Before analysis, the dataset was carefully prepared by:

* Handling missing values
* Investigating missing `body`, `transmission`, and `condition` data
* Removing duplicate VIN records
* Converting `saledate` into a usable datetime format
* Creating **vehicle age** as a derived feature
* Validating unusual values instead of blindly removing them

The cleaned data was then used for further analysis and visualization.

---

## 📊 Exploratory Data Analysis

Most of the analytical work was performed using **Python, Pandas, NumPy and Matplotlib**.

The notebook explores:

### 📈 Sales & Revenue

* Annual revenue trends
* Annual units sold
* Top companies
* Top sellers
* State-wise sales

### 🚘 Vehicle Analysis

* Vehicle age
* Vehicle condition
* Make & model
* Body type
* Odometer
* Year-wise patterns

### 💰 Pricing Analysis

* MMR vs selling price
* Price differences across companies
* Selling price by vehicle age
* Selling price by condition
* Selling price by odometer range

### 🏢 Company & Seller Analysis

* Top companies by units sold
* Top companies by revenue
* Top sellers by units sold
* Top sellers by revenue
* Company–seller relationships
* State-wise seller patterns

---

## 📉 Visual Analysis

The `charts/` folder contains the visualizations created during the analysis.

These charts make it easier to see patterns that are difficult to notice from raw data alone.

**Explore → [`charts/`](charts/)**

---

## 📓 Analysis Notebook

The complete analytical workflow is available in the `notebook/` folder.

It contains the progression from:

**data inspection → cleaning → transformation → analysis → visualization**

**Explore → [`notebook/`](notebook/)**

---

## 💡 One Interesting Part: MMR vs Selling Price

A major part of the analysis compares:

> **MMR — a market/reference valuation**
> **Selling Price — the actual recorded transaction price**

I also examined the difference:

```text
Price Gap = Selling Price − MMR
```

This helps identify patterns where vehicles were sold **above, near, or below their MMR**.

> Price gap is not profit — it only represents the difference between selling price and MMR.

---

## 📊 Power BI

The analysis was also brought together into a Power BI dashboard covering:

**Executive Overview → Vehicle & Market → Company & Seller → Pricing & Valuation**

Since the report could not currently be published through Power BI, dashboard screenshots are included in the repository rather than linking to an unavailable live report.

---

## 🛠️ Tech Stack

| Tool                 | Purpose                                 |
| -------------------- | --------------------------------------- |
| **Python**           | Analysis & preprocessing                |
| **Pandas**           | Data cleaning & manipulation            |
| **NumPy**            | Numerical analysis                      |
| **Matplotlib**       | Data visualization                      |
| **Jupyter Notebook** | Analytical workflow                     |
| **Power BI**         | Interactive dashboard                   |
| **GitHub**           | Project documentation & version control |

---

## 📁 Repository

```text
vehicle_sales_analytics/
│
├── charts/       → Analysis visualizations
├── notebook/     → Complete analysis workflow
├── text_files/   → Supporting project files
└── README.md
```

---

### 👨‍💻 Built by Pranay Authankar

**Data Analytics • Python • Pandas • Data Visualization • Power BI**

> **The dashboard is the final layer. The real story is in the analysis behind it.**
