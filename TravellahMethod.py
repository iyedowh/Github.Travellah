class TravellahMethod:
                      
    def get_user_input(client):
        budget_level_options = ["low", "standard", "high"]

        predefined_origin_options = [
        "France", "Spain", "Italy", "United States", "China", "Thailand", "United Kingdom",
        "Mexico", "Turkey", "Germany", "Japan", "Indonesia", "Austria", "Australia", "Vietnam",
        "Greece", "Portugal", "Canada", "India", "South Africa", "Morocco", "Brazil", "Malaysia",
        "Singapore", "Czech Republic", "Netherlands", "Switzerland", "Egypt", "Poland", "Croatia",
        "Dubai", "New Zealand", "Ireland", "Peru", "Sri Lanka", "Dominican Republic", "Iceland",
        "Argentina", "South Korea", "Hungary", "Philippines", "Costa Rica"
        ]  
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


    def main_program(client, origin, destination, num_travelers, duration, budget_level ):

        # Main program

        response = client.chat.completions.create(
            model='gpt-3.5-turbo',
            max_tokens=2000,
            temperature=0.3,
            messages= [
                {
                    "role":"system",
                    "content":"""You are designed to help users estimate the budget and expenses needed for traveling between 'cities,countries',
        you will describe the flight price in user's origin currency, accommodations cost in user's origin currency,
        meals cost in user's origin currency, transportation cost in user's origin currency, activities cost in user's
        destination and user's origin currency, and overall estimated cost in user's origin currency. 
        You will describe all the costing in details and use Times New Roman font to describe the output.

        Use this format for the output accordingly and neatly:

        Estimated Budget for Traveling from KL, Malaysia to Phuket, Thailand for 3 Travelers from 1st March 2024 to 4th March 2024.

        - Flight Price: The flight ticket price from KL, Malaysia to Phuket, Thailand can be checked on Expedia. Let's assume the total cost for 3 travelers is approximately MYR 2,500.

        - Accommodations Cost: You can explore hotel prices on Booking.com. For a standard budget level, let's estimate the total cost for 3 travelers for 4 days to be around MYR 1,200.

        - Meals Cost: The average cost of meals per day per person in Phuket is around MYR 50. For 3 travelers for 4 days, the total meals cost would be approximately MYR 600.

        - Transportation Cost: The transportation cost within Phuket can vary based on the mode of transport chosen. Let's estimate the total transportation cost for 3 travelers for 4 days to be around MYR 300.

        - Activities Cost: You can explore activity options on ContinentHop. Let's estimate the total cost for activities for 3 travelers for 4 days to be around MYR 1,000.

        - Adding up all the estimated costs:

            --Flight Price: MYR 2,500 - MYR 3,000

            --Accommodations Cost: MYR 1,200 - MYR 2,500

            --Meals Cost: MYR 600 - MYR 800

            --Transportation Cost: MYR 300 - MYR 500

            --Activities Cost: MYR 1,000 - MYR 1,500

            --Total Estimated Cost: MYR 5,600 - MYR 7,500 (THB 43,123 - THB 57,754)

        This estimation is based on a standard budget level and actual prices may vary. It's always recommended to check for the most up-to-date prices and deals on the respective platforms mentioned."""
                },
                {
                    "role":"user",
                    "content": f"""Estimate overall budget in to travel from {origin} to {destination} for {num_travelers} travelers for {duration} days
        with a {budget_level} budget level. You can check flight ticket prices on [Expedia](https://www.expedia.com/). For activities,
        you may explore options on [ContinentHop](https://www.continenthop.com/) and hotel prices on [Booking.com](https://www.booking.com/)."""
                }
            ],
        )

        return response.choices[0].message.content
    