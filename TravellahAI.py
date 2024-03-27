import os
from openai import OpenAI 
from enum import Enum
import streamlit as st
from TravellahMethod import TravellahMethod as tm

client = OpenAI(
    api_key = st.secrets["OPENAI_API_KEY"]
)

def main():

    col1, col2, col3, col4, col5 = st.columns([2, 2, 4, 2, 2])  

    with col3:

        st.markdown(
    "<h1 style='font-family: Rage Italic'>Travellah!</h1>",
    unsafe_allow_html=True
    )

    origin = st.text_input('Origin (City,Country)')
    destination = st.text_input('Destination (City,Country)')
    num_travellers = st.slider('Number of Travellers', min_value=1, max_value=30, value=1, step=1)
    duration = st.slider('Travel Durations (in days)', min_value=1, max_value=30, value=1, step=1)
    budget_level = st.selectbox(
    'Budget Level?',
    ('Low', 'Standard', 'High'))
   
    if st.button("Estimate Budget"):
            total_expenses = (origin, destination, num_travellers, duration, budget_level)
            st.write(f"Estimating overall budget for {num_travellers} travelers from {origin} to {destination} for {duration} days with a {budget_level} budget level. Let me calculate for you, please wait for a second okiee.")
            output= tm.main_program(client, origin, destination, num_travellers, duration, budget_level ) 
            st.write(output)


if __name__ == "__main__":
    main() 