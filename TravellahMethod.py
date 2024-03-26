class TravellahMethod:
  
    from enum import Enum  
  
    class BudgetLevel(Enum):
        LOW = 1
        STANDARD = 2
        HIGH = 3

    def get_user_input(self,client):
        budget_level_options = list(self.BudgetLevel)

        while True:
            origin = input("Enter origin city or country (or leave blank for predefined options): ")
            if origin or len(predefined_origin_options) > 0:
                break
            print("Please enter a valid origin or choose from predefined options (if available).")

        while True:
            destination = input("Enter destination city or country: ")
            if destination:
                break
            print("Please enter a valid destination.")

        num_travelers = int(input("Enter number of travelers: "))

        duration = int(input("Enter duration of travel in days: ")) 

        print("Select your budget level:")
        for i, option in enumerate(budget_level_options):
            print(f"{i+1}. {option.value}")

        while True:
            try:
                budget_level_choice = int(input("Enter your choice (1-3): "))
                if 1 <= budget_level_choice <= len(budget_level_options):
                    budget_level = budget_level_options[budget_level_choice - 1]
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        return origin, destination, num_travelers, duration, budget_level 

predefined_origin_options = [
    "France", "Spain", "Italy", "United States", "China", "Thailand", "United Kingdom",
    "Mexico", "Turkey", "Germany", "Japan", "Indonesia", "Austria", "Australia", "Vietnam",
    "Greece", "Portugal", "Canada", "India", "South Africa", "Morocco", "Brazil", "Malaysia",
    "Singapore", "Czech Republic", "Netherlands", "Switzerland", "Egypt", "Poland", "Croatia",
    "Dubai", "New Zealand", "Ireland", "Peru", "Sri Lanka", "Dominican Republic", "Iceland",
    "Argentina", "South Korea", "Hungary", "Philippines", "Costa Rica"
]  

# Main program
travellah = TravellahMethod()
origin, destination, num_travelers, duration, budget_level = travellah.get_user_input() 

response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    max_tokens=1000,
    temperature=0.5,
    messages= [
        {
            "role":"system",
            "content":"""You are designed to help users estimate the budget and expenses needed for traveling between countries,
you will describe the flight price, accommodations cost, meals cost, transportation cost, activities cost, and overall estimated cost."""
        },
        {
            "role":"user",
            "content": f"""Estimate overall budget to travel from {origin} to {destination} for {num_travelers} travelers for {duration} days
with a {budget_level.value} budget level. You can check flight ticket prices on [Expedia](https://www.expedia.com/). For activities,
you may explore options on [ContinentHop](https://www.continenthop.com/) and hotel prices on [Booking.com](https://www.booking.com/)."""
        }
    ],
)

print(response.choices[0].message.content)
