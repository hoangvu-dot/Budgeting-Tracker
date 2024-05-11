import streamlit as st
import pandas as pd
import plotly.express as px
from Database import *
from streamlit_extras.metric_cards import style_metric_cards
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")


with st.sidebar:
    st.title("💵 Budgeting Tracker")

    box_date = st.date_input("What's the date today: ", value=None, format="DD/MM/YYYY")
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
    st.button("Save & Reset month record", on_click=reset_month)


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
                "date": [x[0] for x in retrieve_data("Trackers")],
                "payment": [x[1] for x in retrieve_data("Trackers")],
                "cost": [x[2] for x in retrieve_data("Trackers")],
                "reason": [x[3] for x in retrieve_data("Trackers")],
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
        labels = [x for x in stats]
        pie_data = [y for x, y in stats.items()]

        fig, ax1 = plt.subplots()
        fig.set_figheight(9)
        ax1.pie(
            pie_data,
            autopct="%1.1f%%",
            startangle=90,
            textprops={"color": "white", "size": 15, "weight": "bold"},
        )
        ax1.axis("equal")
        ax1.legend(
            labels, title="Item", loc="upper left", bbox_to_anchor=(0, 0, 1.2, 1.2)
        )
        fig.set_facecolor("lightgrey")
        st.pyplot(fig)

with col3:
    st.subheader(":orange[Monthly Spending]", divider="green")
    with st.container(height=450):
        stats = retrieve_data("Month")
        data_name = [x[0] for x in stats]
        data_stats = [x[1] for x in stats]

        Df_table = {"Month": data_name, "Total Cost": data_stats}

        bar_chart = pd.DataFrame(Df_table)
        st.bar_chart(
            bar_chart, x="Month", y="Total Cost", use_container_width=True, height=440
        )
