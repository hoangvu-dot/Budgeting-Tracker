import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
from SAVING import take_value

alt.themes.enable("dark")

with st.sidebar:
    st.title("💵 Budgeting Tracker")

    color_theme_list = [
        "blues",
        "cividis",
        "greens",
        "inferno",
        "magma",
        "plasma",
        "reds",
        "rainbow",
        "turbo",
        "viridis",
    ]
    selected_color_theme = st.selectbox("Select a color theme", color_theme_list)

    box_date = st.text_input("What's the date today: ")
    box_payment = st.text_input("What's the payment method: ")
    box_cost = st.number_input(
        "How much does it cost: ", value=None, placeholder="Type a number..."
    )
    box_product = st.text_input("What did you spend on: ")

    st.button(
        "Another Spending day 🥲",
        on_click=take_value,
        args=(box_date, box_payment, box_cost, box_product),
    )
