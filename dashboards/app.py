import streamlit as st
import pandas as pd

with open("../logs/server_logs.txt", "r") as file:
    logs = file.readlines()

data = {"logs": [log.strip() for log in logs]}
df = pd.DataFrame(data)

df["type"] = df["logs"].apply(
    lambda x: "ERROR" if "ERROR" in x else ("WARNING" if "WARNING" in x else "INFO")
)

st.title("Cloud Log Analyzer Dashboard")

st.write(df)

summary = df["type"].value_counts()

st.bar_chart(summary)