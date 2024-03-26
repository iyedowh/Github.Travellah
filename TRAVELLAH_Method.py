import streamlit as st
from enum import Enum

class BudgetLevel(Enum):
    LOW = "Low"
    STANDARD = "Standard"
    HIGH = "High"

def get_user_input():
    budget_level_options = list(BudgetLevel)

    st.title("TRAVELLAH!")

    origin = st.text_input("Enter origin city or country (or leave blank for predefined options): ")
    if not origin:
        st.write("Predefined origin options:")
        predefined_origin_options = [
            "France", "Spain", "Italy", "United States", "China", "Thailand", "United Kingdom",
            "Mexico", "Turkey", "Germany", "Japan", "Indonesia", "Austria", "Australia", "Vietnam",
            "Greece", "Portugal", "Canada", "India", "South Africa", "Morocco", "Brazil", "Malaysia",
            "Singapore", "Czech Republic", "Netherlands", "Switzerland", "Egypt", "Poland", "Croatia",
            "Dubai", "New Zealand", "Ireland", "Peru", "Sri Lanka", "Dominican Republic", "Iceland",
            "Argentina", "South Korea", "Hungary", "Philippines", "Costa Rica"
        ]
        origin_choice = st.selectbox("Choose from predefined options:", predefined_origin_options)
        if origin_choice:
            origin = origin_choice

    destination = st.text_input("Enter destination city or country:")
    num_travelers = st.number_input("Enter number of travelers:", min_value=1, step=1)
    duration = st.number_input("Enter duration of travel in days:", min_value=1, step=1)

    st.write("Select your budget level:")
    budget_level_choice = st.selectbox("Choose budget level:", [option.value for option in budget_level_options])

    return origin, destination, num_travelers, duration, BudgetLevel(budget_level_choice)

# Main Streamlit app
st.title("TRAVELLAH!")

origin, destination, num_travelers, duration, budget_level = get_user_input()

if st.button("Estimate Budget"):
    total_expenses = estimate_overall_budget(origin, destination, num_travelers, duration, budget_level)
    st.write(f"Estimated overall budget for {num_travelers} travelers from {origin} to {destination} for {duration} days with a {budget_level} budget level is: ${total_expenses}")