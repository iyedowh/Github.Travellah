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
    duration = st.slider('Travel Durations (in days)', min_value=1, max_value=30, value=1, step=1)
    budget_level = st.selectbox(
    'Budget Level?',
    ('Low', 'Standard', 'High'))
   
    if st.button("Estimate Budget"):
     
        total_expenses = tm.main_program(client, origin, destination, num_travellers, duration, budget_level)

    st.markdown("## Estimated Budget Details")

    st.write("Travel Details:")
    st.write(f"- Origin: {origin}")
    st.write(f"- Destination: {destination}")
    st.write(f"- Budget Level: {budget_level}")
    st.write(f"- Number of travellers: {num_travellers}")
    st.write(f"- Travel Durations (in days): {duration} days")
    st.write(f"- Total Estimate Budget: ${total_expenses}$")


    output= tm.main_program(client, origin, destination, num_travellers, duration, budget_level ) 
    st.write(output)

if __name__ == "__main__":
    main() 