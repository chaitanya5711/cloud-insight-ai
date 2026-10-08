import os
import pandas as pd
import plotly.express as px
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# ==================================================
# LOAD ENVIRONMENT VARIABLES
# ==================================================

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="CloudInsight AI",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown(
    """
    <style>

    .main {
        padding-top: 1rem;
    }

    .dashboard-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 0px;
    }

    .dashboard-subtitle {
        font-size: 18px;
        margin-bottom: 25px;
    }

    .kpi-card {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid rgba(128,128,128,0.25);
        text-align: center;
        margin-bottom: 15px;
    }

    .kpi-title {
        font-size: 14px;
        font-weight: 600;
    }

    .kpi-value {
        font-size: 25px;
        font-weight: 700;
        margin-top: 5px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ==================================================
# HEADER
# ==================================================

st.markdown(
    '<div class="dashboard-title">☁️ CloudInsight AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="dashboard-subtitle">'
    'Cloud-Based AI Business Analytics Platform'
    '</div>',
    unsafe_allow_html=True
)

st.write(
    "Transform raw business data into meaningful insights "
    "using interactive analytics and Generative AI."
)

st.divider()

# ==================================================
# LOAD DEFAULT DATASET
# ==================================================

default_file = "data/sales_data.csv"

try:
    default_df = pd.read_csv(default_file)
except Exception as e:
    st.error(f"Unable to load default dataset: {e}")
    st.stop()

# ==================================================
# FILE UPLOAD
# ==================================================

uploaded_file = st.file_uploader(
    "📂 Upload Sales Dataset",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    try:

        if uploaded_file.name.lower().endswith(".csv"):
            uploaded_df = pd.read_csv(uploaded_file)

        else:
            uploaded_df = pd.read_excel(uploaded_file)

        st.success(
            f"Uploaded file: {uploaded_file.name}"
        )

        # Clean column names
        uploaded_df.columns = (
            uploaded_df.columns
            .astype(str)
            .str.strip()
        )

        df = uploaded_df.copy()

    except Exception as e:

        st.error(
            f"Unable to read the uploaded file: {e}"
        )

        st.info(
            "Using the default sales dataset instead."
        )

        df = default_df.copy()

else:

    df = default_df.copy()

# ==================================================
# COLUMN NAME NORMALIZATION
# ==================================================

df.columns = (
    df.columns
    .astype(str)
    .str.strip()
)

# ==================================================
# DATE COLUMN DETECTION
# ==================================================

date_candidates = [
    "Date",
    "date",
    "Order Date",
    "Order_Date",
    "OrderDate",
    "Transaction Date",
    "Transaction_Date",
    "TransactionDate",
    "Invoice Date",
    "Invoice_Date",
    "InvoiceDate"
]

date_column = None

for column in date_candidates:

    if column in df.columns:
        date_column = column
        break

# ==================================================
# REQUIRED COLUMN CHECK
# ==================================================

required_columns = [
    "Region",
    "Category",
    "Channel",
    "Sales",
    "Profit",
    "Order_ID",
    "Customer_ID",
    "Quantity",
    "Product"
]

missing_columns = [
    column
    for column in required_columns
    if column not in df.columns
]

# ==================================================
# HANDLE INVALID UPLOAD
# ==================================================

if date_column is None or missing_columns:

    if uploaded_file is not None:

        st.warning(
            "⚠️ The uploaded file is not compatible with this dashboard."
        )

        st.write("### Columns found in your file:")

        st.code(
            ", ".join(df.columns.astype(str))
        )

        if date_column is None:

            st.error(
                "Date column was not found."
            )

        if missing_columns:

            st.error(
                "Missing required columns: "
                + ", ".join(missing_columns)
            )

        st.info(
            "The dashboard requires a sales dataset containing "
            "Date, Region, Category, Channel, Sales, Profit, "
            "Order_ID, Customer_ID, Quantity and Product."
        )

        st.info(
            "You can remove the uploaded file to continue "
            "using the project's default dataset."
        )

        st.stop()

    else:

        st.error(
            "The default dataset is missing required columns."
        )

        st.stop()

# ==================================================
# DATA PREPARATION
# ==================================================

df["Date"] = pd.to_datetime(
    df[date_column],
    errors="coerce"
)

# Remove rows with invalid dates

df = df.dropna(
    subset=["Date"]
)

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("⚙️ Dashboard Controls")

st.sidebar.markdown(
    "Use the filters below to explore the business data."
)

regions = st.sidebar.multiselect(
    "🌎 Region",
    sorted(df["Region"].dropna().unique()),
    default=sorted(df["Region"].dropna().unique())
)

categories = st.sidebar.multiselect(
    "🛍️ Category",
    sorted(df["Category"].dropna().unique()),
    default=sorted(df["Category"].dropna().unique())
)

channels = st.sidebar.multiselect(
    "🛒 Channel",
    sorted(df["Channel"].dropna().unique()),
    default=sorted(df["Channel"].dropna().unique())
)

filtered_df = df[
    (df["Region"].isin(regions))
    & (df["Category"].isin(categories))
    & (df["Channel"].isin(channels))
]

# ==================================================
# KPI CALCULATIONS
# ==================================================

total_sales = filtered_df["Sales"].sum()

total_profit = filtered_df["Profit"].sum()

total_orders = filtered_df["Order_ID"].nunique()

total_customers = filtered_df["Customer_ID"].nunique()

total_units = filtered_df["Quantity"].sum()

profit_margin = (
    total_profit / total_sales * 100
    if total_sales > 0
    else 0
)

# ==================================================
# HEADER
# ==================================================

st.markdown("## 📊 Business Overview")

# ==================================================
# KPI CARDS
# ==================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">TOTAL SALES</div>
            <div class="kpi-value">₹{total_sales:,.0f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">TOTAL PROFIT</div>
            <div class="kpi-value">₹{total_profit:,.0f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">PROFIT MARGIN</div>
            <div class="kpi-value">{profit_margin:.2f}%</div>
        </div>
        """,
        unsafe_allow_html=True
    )

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">TOTAL ORDERS</div>
            <div class="kpi-value">{total_orders:,}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">CUSTOMERS</div>
            <div class="kpi-value">{total_customers:,}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">UNITS SOLD</div>
            <div class="kpi-value">{total_units:,}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ==================================================
# MONTHLY SALES
# ==================================================

st.divider()

st.markdown("## 📈 Sales Performance")

monthly_sales = (
    filtered_df
    .groupby(
        filtered_df["Date"].dt.to_period("M")
    )["Sales"]
    .sum()
    .reset_index()
)

monthly_sales["Date"] = (
    monthly_sales["Date"]
    .astype(str)
)

fig_monthly = px.line(
    monthly_sales,
    x="Date",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)

fig_monthly.update_layout(
    hovermode="x unified"
)

st.plotly_chart(
    fig_monthly,
    use_container_width=True
)

# ==================================================
# CATEGORY & REGION
# ==================================================

col1, col2 = st.columns(2)

# CATEGORY

with col1:

    st.markdown("### 🛍️ Category Performance")

    category_sales = (
        filtered_df
        .groupby("Category")["Sales"]
        .sum()
        .reset_index()
        .sort_values(
            "Sales",
            ascending=False
        )
    )

    fig_category = px.bar(
        category_sales,
        x="Category",
        y="Sales",
        title="Sales by Category"
    )

    st.plotly_chart(
        fig_category,
        use_container_width=True
    )

# REGION

with col2:

    st.markdown("### 🌎 Regional Performance")

    region_sales = (
        filtered_df
        .groupby("Region")["Sales"]
        .sum()
        .reset_index()
        .sort_values(
            "Sales",
            ascending=False
        )
    )

    fig_region = px.bar(
        region_sales,
        x="Region",
        y="Sales",
        title="Sales by Region"
    )

    st.plotly_chart(
        fig_region,
        use_container_width=True
    )

# ==================================================
# PRODUCT PERFORMANCE
# ==================================================

st.markdown("### 📦 Product Performance")

product_sales = (
    filtered_df
    .groupby("Product")["Sales"]
    .sum()
    .reset_index()
    .sort_values(
        "Sales",
        ascending=False
    )
)

fig_product = px.bar(
    product_sales,
    x="Sales",
    y="Product",
    orientation="h",
    title="Product Sales Performance"
)

st.plotly_chart(
    fig_product,
    use_container_width=True
)

# ==================================================
# CHANNEL PERFORMANCE
# ==================================================

st.markdown("### 🛒 Sales Channel Performance")

channel_sales = (
    filtered_df
    .groupby("Channel")["Sales"]
    .sum()
    .reset_index()
)

fig_channel = px.pie(
    channel_sales,
    names="Channel",
    values="Sales",
    hole=0.4,
    title="Sales Distribution by Channel"
)

st.plotly_chart(
    fig_channel,
    use_container_width=True
)

# ==================================================
# AI BUSINESS ANALYST
# ==================================================

st.divider()

st.markdown("## 🤖 AI Business Analyst")

st.write(
    "Ask questions about your business data and receive "
    "AI-powered analysis."
)

if not GROQ_API_KEY:

    st.warning(
        "Groq API key not found. Please configure your .env file."
    )

else:

    question = st.text_input(
        "💬 Ask your business question",
        placeholder="Example: Which region has the highest sales?"
    )

    if st.button("🤖 Analyze"):

        if question.strip() == "":

            st.warning(
                "Please enter a question."
            )

        else:

            summary = f"""
BUSINESS DATA

Total Sales: ₹{total_sales:,.2f}
Total Profit: ₹{total_profit:,.2f}
Total Orders: {total_orders}
Total Customers: {total_customers}
Units Sold: {total_units}
Profit Margin: {profit_margin:.2f}%

REGION SALES
{region_sales.to_string(index=False)}

CATEGORY SALES
{category_sales.to_string(index=False)}

PRODUCT SALES
{product_sales.to_string(index=False)}

CHANNEL SALES
{channel_sales.to_string(index=False)}
"""

            try:

                client = Groq(
                    api_key=GROQ_API_KEY
                )

                prompt = f"""
You are an experienced business analyst.

Analyze the following business data.

{summary}

Answer this question:

{question}

Instructions:

- Give a clear answer.
- Use actual numbers.
- Explain the reasoning briefly.
- Do not invent data.
- Keep the answer easy to understand.
"""

                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    temperature=0.2
                )

                answer = response.choices[0].message.content

                st.success("AI Analysis")

                st.write(answer)

            except Exception as e:

                st.error(
                    f"AI analysis failed: {e}"
                )

# ==================================================
# AI BUSINESS RECOMMENDATIONS
# ==================================================

st.divider()

st.markdown("## 💡 AI Business Recommendations")

st.write(
    "Generate practical recommendations based on the current "
    "business performance."
)

if GROQ_API_KEY:

    if st.button("💡 Generate Recommendations"):

        recommendation_summary = f"""
BUSINESS PERFORMANCE

Total Sales: ₹{total_sales:,.2f}
Total Profit: ₹{total_profit:,.2f}
Orders: {total_orders}
Customers: {total_customers}
Units Sold: {total_units}
Profit Margin: {profit_margin:.2f}%

REGION PERFORMANCE
{region_sales.to_string(index=False)}

CATEGORY PERFORMANCE
{category_sales.to_string(index=False)}

PRODUCT PERFORMANCE
{product_sales.to_string(index=False)}

CHANNEL PERFORMANCE
{channel_sales.to_string(index=False)}
"""

        try:

            client = Groq(
                api_key=GROQ_API_KEY
            )

            recommendation_prompt = f"""
You are a professional business consultant.

Analyze this business data:

{recommendation_summary}

Provide 5 practical recommendations.

Focus on:

1. Increasing sales
2. Improving profit
3. Improving product performance
4. Improving regional performance
5. Improving sales channels

Use actual numbers where possible.

Do not invent information.

Keep the recommendations concise and practical.
"""

            response = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=[
                    {
                        "role": "user",
                        "content": recommendation_prompt
                    }
                ],
                temperature=0.3
            )

            recommendations = response.choices[0].message.content

            st.success(
                "AI Business Recommendations"
            )

            st.write(
                recommendations
            )

        except Exception as e:

            st.error(
                f"Recommendation generation failed: {e}"
            )

# ==================================================
# DATA PREVIEW
# ==================================================

st.divider()

st.markdown("## 📋 Dataset Preview")

st.dataframe(
    filtered_df.head(100),
    use_container_width=True
)

st.caption(
    f"Showing {len(filtered_df):,} records after applying filters."
)

# ==================================================
# FOOTER
# ==================================================

st.divider()

st.caption(
    "CloudInsight AI • Cloud-Based AI Business Analytics Platform"
)