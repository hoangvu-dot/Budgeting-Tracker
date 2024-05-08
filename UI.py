import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
from Database import *


alt.themes.enable("dark")

with st.sidebar:
    st.title("💵 Budgeting Tracker")


    box_date = st.text_input("What's the date today: ")
    box_payment = st.text_input("What's the payment method: ")
    box_cost = st.number_input(
        "How much does it cost: ", value=None, placeholder="Type a number..."
    )
    box_product = st.text_input("What did you spend on: ")

    st.button(
        "Another Spending day 🥲",
        on_click=create_database,
        args=(box_date, box_payment, box_cost, box_product)
    )
    

