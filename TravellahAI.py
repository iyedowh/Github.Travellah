import os
from openai import OpenAI 
from enum import Enum
import streamlit as st
from TravellahMethod import TravellahMethod as tm

client = OpenAI(
    api_key = st.secrets["OPENAI_API_KEY"]
)

def main():

    st.title("TRAVELLAH!")

    origin = st.text_input('Origin')
    destination = st.text_input('Destination')
    num_travellers = st.slider('Number of Travellers', min_value=1, max_value=30, value=1, step=1)
    duration = st.slider('Duration (in days)', min_value=1, max_value=30, value=1, step=1)
    budget_level = st.selectbox(
    'Budget Level?',
    ('Low', 'Standard', 'High'))
   
    if st.markdown("## Estimated Budget Details"):
     total_expenses = (origin, destination, num_travellers, duration, budget_level)
    st.write(f"**Estimated overall budget for {num_travellers} travelers from {origin} to {destination} for {duration} days with a {budget_level} budget level is: ${total_expenses}")
    col1, col2 = st.columns(2)

    with col1:
            st.write("Travel Details:")
            st.write(f"- Origin: {origin}")
            st.write(f"- Destination: {destination}")
    with col2:
            st.write("Budget Information:")
            st.write(f"- Budget Level: {budget_level}")
            st.write(f"- Total Expenses: ${total_expenses}")

            st.write("Here is the breakdown of estimated budget:")
            st.write(f"Total Expenses: ${total_expenses}", unsafe_allow_html=True)

if __name__ == "__main__":
    main() 