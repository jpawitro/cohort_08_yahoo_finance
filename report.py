import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.title("Cohort 08 Data Analyst")

col1, col2 = st.columns(2)

with col1:
    saham = st.text_input("Kode Saham")

with col2:
    waktu = st.selectbox("Periode",['1d','5d','1mo','1y','5y','10y','ytd','max'],4)

data = yf.Ticker(saham).history(period=waktu).reset_index()

fig = go.Figure(data=[go.Candlestick(x=data['Date'],
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'])])

st.plotly_chart(fig, use_container_width=True)