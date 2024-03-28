import os
from openai import OpenAI 
import datetime
import streamlit as st
from TravellahMethod import TravellahMethod as tm

client = OpenAI(
    api_key = st.secrets["OPENAI_API_KEY"]
)

def main():

    st.markdown(
    "<h1 style='font-family: Rage Italic; text-align: center;'>Travellah!</h1>",
    unsafe_allow_html=True
    )

    st.divider()

    st.caption("<h1 style='font-family: Rage Italic; text-align: center;'>This app is designed to revolutionize the way users estimate budgets and expenses for international travel.</h1>", unsafe_allow_html=True)

    st.divider()

    origin = st.text_input('Origin (City,Country)')

    st.divider()

    destination = st.text_input('Destination (City,Country)')

    st.divider()

    num_travellers = st.slider('Number of Travellers', min_value=1, max_value=30, value=1, step=1)

    st.divider()

    duration = st.slider('Travel Durations (in days)', min_value=1, max_value=30, value=1, step=1)

    st.divider()

    budget_level = st.selectbox(
    'Budget Level?',
    ('Low', 'Standard', 'High'))

    st.divider()

    today = datetime.datetime.now()
    next_year = today.year + 1
    jan_1 = datetime.date(next_year, 1, 1)
    dec_31 = datetime.date(next_year, 12, 31)

    date = st.date_input(
        "Select your travelling time: ",
        (jan_1, datetime.date(next_year, 1, 7)),
        jan_1,
        dec_31,
        format="MM.DD.YYYY",
    )

    st.divider()

    if st.button("Estimate Budget"):
            
            total_expenses = (origin, destination, num_travellers, duration, budget_level)

            st.write(f"""Estimating overall budget for {num_travellers} travelers
                    from {origin} to {destination} for {duration} days with a {budget_level} budget level on {date}. 
                    Let me calculate for you, please wait for a second okiee.""")
            
            st.divider()

            output= tm.main_program(client, origin, destination, num_travellers, duration, budget_level, date) 

            st.write(output)


if __name__ == "__main__":
    main() 