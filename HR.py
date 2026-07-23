import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="HR Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 HR Analytics Dashboard")

# Load Data
@st.cache_data
def load_data():
    return pd.read_excel("Book1.xlsx")

df = load_data()

# Sidebar
st.sidebar.header("Filters")

department = st.sidebar.multiselect(
    "Department",
    df["Department"].unique(),
    default=df["Department"].unique()
)

gender = st.sidebar.multiselect(
    "Gender",
    df["Gender"].unique(),
    default=df["Gender"].unique()
)

filtered_df = df[
    (df["Department"].isin(department)) &
    (df["Gender"].isin(gender))
]

# KPIs
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Employees", len(filtered_df))
col2.metric("Average Age", round(filtered_df["Age"].mean(),1))
col3.metric("Average Monthly Income",
            f"{filtered_df['Monthly Income'].mean():,.0f}")

attrition = filtered_df["Attrition"].value_counts().get("Yes",0)
col4.metric("Attrition", attrition)

st.markdown("---")

# Charts

c1, c2 = st.columns(2)

with c1:
    fig = px.pie(
        filtered_df,
        names="Attrition",
        title="Employee Attrition"
    )
    st.plotly_chart(fig, use_container_width=True)

with c2:
    fig = px.bar(
        filtered_df.groupby("Department").size().reset_index(name="Employees"),
        x="Department",
        y="Employees",
        title="Employees by Department"
    )
    st.plotly_chart(fig, use_container_width=True)

c3, c4 = st.columns(2)

with c3:
    fig = px.histogram(
        filtered_df,
        x="Age",
        title="Age Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

with c4:
    fig = px.box(
        filtered_df,
        x="Job Role",
        y="Monthly Income",
        title="Monthly Income by Job Role"
    )
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Employee Details")
st.dataframe(filtered_df, use_container_width=True)
job_attrition = pd.crosstab(
    df["Job Role"],
    df["Attrition"]
)

print("\nJob Role Attrition:")
print(job_attrition)

job_attrition.plot(
    kind="bar",
    figsize=(12, 6)
)
plt.title("Job Role-wise Attrition")
plt.xlabel("Job Role")
plt.ylabel("Employee Count")
plt.xticks(rotation=45)
plt.show()
plt.figure(figsize=(8, 5))

df.boxplot(
    column="Monthly Income",
    by="Attrition"
)

plt.title("Monthly Income vs Attrition")
plt.suptitle("")
plt.xlabel("Attrition")
plt.ylabel("Monthly Income")
plt.show()
overtime_attrition = pd.crosstab(
    df["Over Time"],
    df["Attrition"]
)

print("\nOvertime vs Attrition:")
print(overtime_attrition)

overtime_attrition.plot(
    kind="bar",
    figsize=(6, 4)
)
plt.title("Overtime Impact on Attrition")
plt.xlabel("Over Time")
plt.ylabel("Employee Count")
plt.show()