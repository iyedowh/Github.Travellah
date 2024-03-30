import os
from openai import OpenAI 
import datetime
import time
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

    st.caption("<h1 style='font-family: Rage Italic; text-align: center;'>𝐵𝓊𝒹𝑔𝑒𝓉 𝒟𝑜𝑒𝓈𝓃'𝓉 𝐵𝒾𝓉𝑒</h1>𝐸𝓍𝓅𝓁𝑜𝓇𝑒 𝓌𝒾𝓉𝒽 𝒟𝑒𝓁𝒾𝑔𝒽𝓉</h2>", unsafe_allow_html=True)

    st.divider()

    origin = st.text_input('Origin ⚲ (City,Country)')

    st.divider()

    destination = st.text_input('Destination ✈︎ (City,Country)')

    st.divider()

    num_travellers = st.slider('Number of Travellers 𓀙𓀙𓀙', min_value=1, max_value=30, value=1, step=1)

    st.divider()
    
    today = datetime.datetime.now()
    next_year = today.year + 1
    jan_1 = datetime.date(today.year, 1, 1)
    dec_31 = datetime.date(next_year, 12, 31)

    duration = st.date_input(
        "Select your travelling date 🗓 ",
        (jan_1, datetime.date(next_year, 1, 7)),
        jan_1,
        dec_31,
        format="DD.MM.YYYY",
    )

    st.divider()

    budget_level = st.selectbox(
    'Budget Level 💸 ',
    ('Low', 'Standard', 'High'))

    st.divider()

    if st.button("Estimate Budget"):
            
            total_expenses = (origin, destination, num_travellers, duration, budget_level)

            st.divider()

            with st.spinner(f"""Estimating overall budget for {num_travellers} travelers
                    from {origin} to {destination} with a {budget_level} budget level. 
                    Let me calculate for you, please wait for a second okieee 🧐"""):
                
                time.sleep(7)
                
                st.success('Almost done...')
            
            st.divider()

            output= tm.main_program(client, origin, destination, num_travellers, duration, budget_level) 

            st.write(output)


if __name__ == "__main__":
    main() 

