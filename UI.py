import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
from Database import *
from streamlit_extras.metric_cards import style_metric_cards

st.set_page_config(layout="wide")


with st.sidebar:
    st.title("💵 Budgeting Tracker")

    box_date = st.date_input("What's the date today: ", value= None, format='DD/MM/YYYY')
    box_payment = st.text_input("What's the payment method: ")
    box_cost = st.number_input(
        "How much does it cost: ", value=None, placeholder="Type a number..."
    )
    box_product = st.text_input("What did you spend on: ")

    col = st.columns([3, 1], gap="small")
    with col[0]:
        st.button(
            "Another Spending day 🥲",
            on_click=create_databases,
            args=(f"{box_date}", box_payment, box_cost, box_product),
        )
    with col[1]:
        st.button(
            "Undo",
            on_click=delete_data,
        )
    st.button("Save & Reset this month record", on_click= reset_month)
    

col1, col2, col3 = st.columns(3, gap="medium")
with col1:
    with st.container(height=200):
        st.subheader(":orange[Current Month Damage]")
        st.metric(
            label="Idontknow",
            value=f"{monthly_spend()}.000 VND",
            label_visibility="hidden",
        )
        color = 0
        if monthly_spend() > 3000:
            color = "#E74C3C"
        else:
            color = "#27AE60"
        style_metric_cards(
            background_color=color, border_left_color=color, border_color=color
        )

    with st.container(height=300):
        st.markdown(":orange[**Transactions**]")
        df = pd.DataFrame(
            {
                "date": [x[0] for x in retrieve_data()],
                "payment": [x[1] for x in retrieve_data()],
                "cost": [x[2] for x in retrieve_data()],
                "reason": [x[3] for x in retrieve_data()],
            }
        )
        df_reversed = df[::-1]
        st.dataframe(
            df_reversed,
            column_config={
                "date": "Date",
                "payment": "Payment",
                "cost": "Cost",
                "reason": "Item ",
            },
            hide_index=True,
            use_container_width=True,
        )

with col2:
    st.subheader(":orange[Spending Purposes]", divider="green")
    with st.container(height=450):
        stats = unique_item()
        data_name = [x for x in stats]
        data_stats = [y for x, y in stats.items()]
        
        Df_table = {"Item": data_name, "Percentage": data_stats}

        bar_chart = pd.DataFrame(Df_table)
        st.bar_chart(
            bar_chart, x="Item", y="Percentage", use_container_width=True, height=440
        )

with col3:
    ...
