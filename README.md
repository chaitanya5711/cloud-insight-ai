# ☁️ CloudInsight AI

### Cloud-Based AI Business Analytics Platform

CloudInsight AI is a cloud-based business analytics platform that transforms raw sales data into meaningful business insights using interactive dashboards and Generative AI.

The platform allows users to analyze sales, profit, customers, products, regions, categories, and sales channels through an interactive Streamlit dashboard. It also uses Groq AI to generate business insights and recommendations from the analyzed data.

## 🚀 Live Demo

**Streamlit Cloud:**
Add your deployed Streamlit application URL here.

## 📌 Project Overview

Businesses generate large amounts of sales data, but raw data alone does not provide actionable insights.

CloudInsight AI solves this problem by combining:

* 📊 Interactive business dashboards
* 🧹 Data processing and analysis
* 🤖 Generative AI-powered business analysis
* 💡 AI-generated recommendations
* ☁️ Cloud deployment

The application provides a simple interface where users can explore business performance and obtain AI-powered insights from their data.

## ✨ Features

### 📊 Interactive Dashboard

The dashboard provides key business performance metrics including:

* Total Sales
* Total Profit
* Profit Margin
* Total Orders
* Total Customers
* Units Sold

### 📈 Data Visualization

Interactive charts are provided for:

* Monthly Sales Trends
* Category Performance
* Regional Performance
* Product Performance
* Sales Channel Performance

### 🎛️ Dynamic Filters

Users can filter the dashboard based on:

* Region
* Category
* Sales Channel

All KPIs and visualizations update automatically according to the selected filters.

### 📂 Dataset Upload

Users can upload their own compatible:

* CSV files
* Excel files (`.xlsx`)

The application validates the uploaded dataset before processing it.

### 🤖 AI Business Analyst

CloudInsight AI integrates Groq's Generative AI capabilities to analyze business data and answer questions such as:

* Which region has the highest sales?
* Which category generates the most profit?
* Which products are performing well?
* What are the major business trends?
* What areas require attention?

### 💡 AI Business Recommendations

The platform generates AI-powered recommendations based on the analyzed business data.

These recommendations can help identify:

* High-performing products
* Weak-performing regions
* Profit opportunities
* Sales trends
* Potential areas for business improvement

## 🏗️ Architecture

```text
CSV / Excel Data
       ↓
Python + Pandas
       ↓
Data Processing & Analysis
       ↓
Streamlit Dashboard
       ↓
Plotly Visualizations
       ↓
Groq Generative AI
       ↓
AI Insights & Recommendations
       ↓
Streamlit Community Cloud
```

## 🛠️ Technologies Used

| Technology                | Purpose                          |
| ------------------------- | -------------------------------- |
| Python                    | Application development          |
| Pandas                    | Data processing and analysis     |
| Plotly                    | Interactive data visualization   |
| Streamlit                 | Dashboard and web application    |
| Groq API                  | Generative AI analysis           |
| OpenPyXL                  | Excel file processing            |
| python-dotenv             | Environment variable management  |
| Git & GitHub              | Version control and code hosting |
| Streamlit Community Cloud | Cloud deployment                 |

## 📁 Project Structure

```text
CloudInsight AI/
│
├── data/
│   └── sales_data.csv
│
├── app.py
├── generate_data.py
├── requirements.txt
├── .gitignore
├── .env
└── venv/
```

> `.env` and `venv/` are excluded from GitHub using `.gitignore`.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/cloudinsight-ai.git
```

### 2. Navigate to the project

```bash
cd cloudinsight-ai
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```powershell
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔐 Environment Variables

Create a `.env` file in the project root:

```text
GROQ_API_KEY=your_groq_api_key_here
```

Never upload your API key to GitHub.

## ▶️ Run Locally

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## ☁️ Cloud Deployment

CloudInsight AI is deployed using **Streamlit Community Cloud**.

Deployment process:

```text
GitHub Repository
       ↓
Streamlit Community Cloud
       ↓
Configure GROQ_API_KEY in Secrets
       ↓
Deploy app.py
       ↓
Public Web Application
```

The application can therefore be accessed through a web browser without requiring the user to run the Python application locally.

## 📊 Sample Dataset

The project includes a generated sales dataset containing information such as:

* Date
* Order ID
* Customer ID
* Product
* Category
* Region
* Sales Channel
* Quantity
* Unit Price
* Discount
* Sales
* Profit

The dataset is intended for demonstrating business analytics and AI-powered insights.

## 🎯 Use Cases

CloudInsight AI can be used for:

* Sales performance analysis
* Business reporting
* Regional analysis
* Product performance analysis
* Profitability analysis
* Customer and order analysis
* AI-assisted business decision-making

## 🔮 Future Improvements

Potential future enhancements include:

* Real-time database integration
* PostgreSQL / MySQL support
* Automated report generation
* PDF business reports
* Advanced forecasting
* Anomaly detection
* Role-based user authentication
* More AI-powered analytics
* Automated data quality checks
* Integration with cloud storage platforms

## 👨‍💻 Author

**Chaitanya Jadhav**

B.E. Information Technology — 2026

Interested in:

* Data Analytics
* Business Intelligence
* Artificial Intelligence
* Generative AI

## ⭐ Project Highlights

* Cloud-based deployment
* Interactive business dashboard
* Generative AI integration
* CSV and Excel data support
* Dynamic business KPIs
* Interactive visualizations
* AI-powered recommendations

---

⭐ If you find this project useful, consider giving the repository a star!
