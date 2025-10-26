import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["2025/1", "2025/2", "2025/3", "2025/4", "2025/5", "2025/6"],
    "Item A": [100, 120, 150, 130, 160, 180],
    "Item B": [80, 90, 85, 110, 130, 120]
}

df = pd.DataFrame(data).set_index("Month")

st.header("グラフのサンプル表示")

st.table(df)
st.line_chart(df)
st.bar_chart(df)