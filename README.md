# clinical-risk-dashboard
A Streamlit dashboard for clinical patient scan risk analysis with real-time risk alerts, visualizations, and data audit logs. A real-time clinical risk triage dashboard built with Python and Streamlit.
This dashboard allows clinicians to:
Import and clean patient scan data.
Flag patients at high or moderate risk based on signal thresholds.
Display full patient data and flag alerts dynamically.
Visualize scan types and risk distributions using bar and pie charts.
Maintain a full audit log of missing or invalid records for compliance purposes.

 Features:- Upload and clean patient scan data.
Risk Alert detection:
High Risk
Moderate Risk
Cleared (Low Risk)
Interactive bar chart of patient distribution by scan test type (MRI, CT, X-ray).
Pie chart showing risk distribution.
Audit log for rows with missing Signal scores.
Real-time dashboard generation timestamp.
 
 Technical Stack:- Python- Pandas (for data handling)- Streamlit (for web dashboard)- Matplotlib (for chart plotting)- CSV Files (for data source)

 Project Summary:
This project simulates a real clinical workflow where patient scan data is triaged for potential risk based on signal strength. The dashboard processes raw CSV files, flags high/moderate risk patients, visualizes the distribution of scan types and risk levels, and provides a timestamped audit-ready report.
 
 Key Learning Outcomes:- Building real-world dashboards without front-end coding.- Data cleaning, risk logic, and visualization.- Export-ready, audit-friendly clinical reporting
