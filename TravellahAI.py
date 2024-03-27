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

    origin, destination, num_travelers, duration, budget_level = tm.get_user_input(client)

    if st.button("Estimate Budget"):
        total_expenses = (origin, destination, num_travelers, duration, budget_level)
        st.write(f"Estimated overall budget for {num_travelers} travelers from {origin} to {destination} for {duration} days with a {budget_level} budget level is: ${total_expenses}")
        output= tm.main_program(client, origin, destination, num_travelers, duration, budget_level ) 
        st.write(output)

if __name__ == "__main__":
    main() 