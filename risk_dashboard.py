import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# --- Part 1: Dashboard Setup ---
st.set_page_config(page_title="Patient Risk Dashboard", layout="centered")
st.title("🩺 Clinical Risk Monitoring Dashboard")
st.write("Welcome to the scan risk analyzer. This dashboard displays cleaned data, risk alerts, and visual charts.")

# --- Part 2: Load and Preview All Patients ---
st.subheader("✅ All Patients (Full Data)")
try:
    data = pd.read_csv("cleaned_scan_results.csv")
    st.write("✅ Data loaded successfully.")
    st.dataframe(data.head(10))
except FileNotFoundError:
    st.error("❌ cleaned_scan_results.csv not found. Make sure it exists in this folder.")

# --- Part 3: Show Flagged Patients Only ---
st.subheader("🚨 Alert Summary: Flagged Patients Only")
try:
    flagged_patients = data[data["Risk Alert"] != "OK: Cleared (Low)"]
    st.dataframe(flagged_patients)
except Exception as e:
    st.error(f"Error loading flagged patients: {e}")

# --- Part 4: Risk Analysis Charts ---
st.subheader("📊 Risk Analysis Charts")
st.write("### 🧪 Number of Patients by Test Type")
test_counts = data['Test'].value_counts()
fig1, ax1 = plt.subplots()
test_counts.plot(kind='bar', ax=ax1, color='skyblue')
ax1.set_xlabel("Test Type")
ax1.set_ylabel("Number of Patients")
ax1.set_title("Patients by Scan Test Type")
st.pyplot(fig1)

st.write("### ⚠️ Risk Alert Breakdown")
risk_counts = data['Risk Alert'].value_counts()
fig2, ax2 = plt.subplots()
ax2.pie(risk_counts, labels=risk_counts.index, autopct='%1.1f%%', startangle=90)
ax2.axis('equal')
st.pyplot(fig2)

# --- Part 5: Dashboard Footer (Timestamp) ---
st.write("---")
timestamp = datetime.now().strftime("%B %d, %Y — %I:%M %p")
st.caption(f"🕒 Dashboard generated on: {timestamp}")
