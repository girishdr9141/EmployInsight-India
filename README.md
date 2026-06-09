# 📈 EmployInsight India: India Unemployment & Industry Analysis (2019–2020)

**EmployInsight India** is a Data Analytics project that provides a complete end-to-end analysis of unemployment trends in India during 2019–2020. It leverages real-world datasets and visualization techniques to uncover regional disparities, analyze industry efficiency, and suggest strategic directions for employment growth.

---

## 📂 Dataset Overview

The project uses **three real-world datasets** sourced from Kaggle:

1. **Unemployment in India.csv**
   - State-wise and area-wise unemployment data (Rural/Urban)
   - 📎 [Dataset Link](https://www.kaggle.com/datasets/gokulrajkmv/unemployment-in-india)

2. **Unemployment Rate upto 11_2020.csv**
   - Includes state-level unemployment rates with latitude/longitude
   - 📎 [Dataset Link](https://www.kaggle.com/datasets/gokulrajkmv/unemployment-in-india)

3. **Industrywisedatasupto_dipp.csv**
   - Industry-wise investment and employment data
   - 📎 [Dataset Link](https://www.kaggle.com/datasets/ravivarmaodugu/data-on-investment-and-employment-in-india)

> 🔒 **Note**: Raw datasets are not uploaded to this repository due to licensing and size restrictions. Access the above links to download them.

---

## 🔍 Project Workflow

### 🔧 Phase 1: Data Loading & Exploration
- Imported datasets and Python libraries
- Previewed structure, types, and missing values

### 🧹 Phase 2: Data Cleaning & Preprocessing
- Standardized column names for consistency across all datasets
- Converted date columns to `datetime` objects
- Dropped nulls and duplicates to ensure data quality
- Cleaned and formatted investment and employment columns numerically

### 📊 Phase 3: Exploratory Data Analysis (EDA)
- Plotted national unemployment trends over time
- Visualized June 2020 unemployment rates by region
- Created correlation heatmaps and bar charts
- Analyzed and compared investment vs. employment across industries

### 🧠 Phase 4: Deep Insights & Strategic Analysis
- Calculated **Jobs per ₹ Crore** as a metric for industry efficiency
- Assessed regional employment strength (e.g., Telangana vs. National average)
- Mapped **opportunity scores** based on unemployment rates to target key regions
- Suggested tailored skill development areas for high-efficiency industries

---

## 📌 Key Findings & Insights

- **National Trend**: A steep national spike in unemployment occurred during the nationwide COVID-19 lockdown in April-May 2020, followed by a gradual recovery.
- **Regional Disparities**:
  - **High Unemployment / High Opportunity Regions**: States like **Haryana (32.49% average in June 2020)** and **Tripura (23.15%)** experienced severe spikes and are classified as High Opportunity areas requiring immediate employment intervention.
  - **Resilient Regions**: **Telangana** showcased high employment stability with a 2019-2020 average unemployment rate of **7.74%** (compared to the national average of **11.79%**), positioning it as a potential model for other regions.
- **Industry Job-Creation Efficiency**:
  - The **Leather, Leather Goods, and Pickers** industry emerged as the most efficient at generating employment per unit of capital investment.
  - Other high-efficiency sectors include **Textiles**, **Scientific Instruments**, and **Paper manufacturing**.
- **Skill Training Priorities**:
  - **Cotton Textiles**: Textile manufacturing, garment production
  - **Paper**: Pulp and paper technology, printing skills
  - **Jute Textiles**: Jute processing, weaving

---

## 📊 Key Visualizations & Metrics

| Insight                    | Description                                                      |
|---------------------------|------------------------------------------------------------------|
| 📈 Trend Plot              | National unemployment rate (monthly) from Jan 2019 – Nov 2020   |
| 🗺️ Geo Map                 | June 2020 state-wise unemployment rate using latitude/longitude |
| 🔥 Top Industries         | Ranked by investment, employment, and efficiency (jobs/crore)    |
| 💼 Efficiency Bar Plot     | Jobs per ₹ crore for each industry                              |
| 🧠 Skill Suggestions        | Based on top job-generating industries                          |
| 📌 Regional Score Mapping  | States categorized by high/medium/low job creation potential    |

---

## ⚙️ Technologies Used

- **Python 3**
  - `pandas`, `numpy` – Data processing
  - `matplotlib`, `seaborn` – Static plots
  - `plotly.express` – Interactive visualizations

- **Google Colab** – Jupyter-based execution and visualization
- **CSV files** – Loaded from Kaggle downloads

---

## 🚀 Possible Extensions

- 🔗 Real-time data integration via **API** from CMIE/NSSO
- 📈 Forecasting future unemployment using **Machine Learning models**
- 🖥️ Build interactive dashboards with **Streamlit, Dash, or Tableau**
- 🔍 Automate skill-gap analysis from active job board data

---

## 📁 Project Structure

- 📦 EmployInsight-India/
  - 📄 README.md
  - 📄 DataAnalysis.ipynb
