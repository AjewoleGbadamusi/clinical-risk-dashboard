# clinical-risk-dashboard
A Streamlit dashboard for clinical patient scan risk analysis with real-time risk alerts, visualizations, and data audit logs.
 Dashboard Features:- Load and display 100-patient cleaned scan data.- Show full patient table and flagged alert summary.- Risk Alert detection based on Signal score:
 [High] High Risk
 [Moderate] Moderate Risk
 [OK] Cleared (Low)- Interactive bar chart of number of patients by scan test type (MRI, CT, X-ray).- Pie chart showing risk distribution (High, Moderate, Low).- Real-time timestamp showing when dashboard was last generated.
 Technical Stack:- Python- Pandas (for data handling)- Streamlit (for web dashboard)- Matplotlib (for chart plotting)- CSV Files (for data source)
 Project Summary:
 I developed a clinical risk triage dashboard using Python and Streamlit. The dashboard reads and
 processes patient scan data, flags risky patients based on signal strength, and visualizes both
 patient volume by scan type and risk distribution. It updates dynamically and provides real-time
 timestamps to reflect the latest data - simulating a real clinical monitoring system.
 Key Learning Outcomes:- Building real-world dashboards without front-end coding.- Data cleaning, risk logic, and visualization.- Export-ready, audit-friendly clinical reporting
