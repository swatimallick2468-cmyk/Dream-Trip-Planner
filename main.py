import functions
import destinations
import hotels
import budget
import itinerary


# -----------------------------
# WELCOME 🤗
# -----------------------------

functions.welcome()


# -----------------------------
# CHOOSE INTEREST 🫶
# -----------------------------

print("What kind of experience are you looking for?")
print("1. 🏞️  Nature and Peace")
print("2. 🔥  Adventure")
print("3. 🏖️  Beach Escape")
print("4. 📸  Photography")
print("5. 💖  Relaxing Getaway")

interest = input("Enter your choice (1-5): ")

while interest not in ["1", "2", "3", "4", "5"]:

    print("Invalid choice. Please choose between 1 and 5.")

    interest = input("Enter your choice (1-5): ")


# -----------------------------
# DESTINATION 📍
# -----------------------------

destinations.show_destinations(interest)

choice = int(input("Enter your destination: "))


if interest == "1":
    maximum = 3

elif interest == "2":
    maximum = 2

elif interest == "3":
    maximum = 2

elif interest == "4":
    maximum = 3

else:
    maximum = 2


while choice < 1 or choice > maximum:

    print("Please choose one of the recommended destinations.")

    choice = int(input("Enter your destination: "))


selected_destination = destinations.get_destination(
    interest,
    str(choice)
)


print()
print("Your selected destination:", selected_destination)


# ----------------------------
# NUMBER OF PEOPLE 👥
# ----------------------------

print()

people = int(input("Enter number of people: "))

while people <= 0:

    print("Please enter a valid number.")

    people = int(input("Enter number of people: "))


print("Travellers:", people)


# ----------------------------
# NUMBER OF DAYS 🗓️
# ----------------------------

print()

days = int(
    input("Enter how many days is your trip? (1-10): ")
)

while days < 1 or days > 10:

    print("Please enter a number between 1 and 10.")

    days = int(
        input("Enter how many days is your trip? (1-10): ")
    )


print("Trip duration:", days, "days")


# --------------------------
# BUDGET
# --------------------------

print()

user_budget = int(
    input("What is your total budget? ₹")
)

while user_budget <= 0:

    print("Please enter a valid budget.")

    user_budget = int(
        input("What is your total budget? ₹")
    )


print("Your total budget: ₹", user_budget)


# --------------------------
# TRANSPORT
# --------------------------

print()

if selected_destination == "Leh-Ladakh":

    transport = " ✈️  Flight"

elif selected_destination == "Lakshadweep":

    transport = " ✈️  Flight"

else:

    transport = " 🚗 Car"


print("Suggested transport:", transport)


# ---------------------------
# HOTEL
# ---------------------------

hotel = hotels.get_hotel(
    selected_destination,
    user_budget
)


print()
print("Suggested hotel:", hotel)


# ---------------------------
# INTERESTING ACTIVITIES ✨
# ---------------------------

print()
print("Interesting things to do:")

if selected_destination == "Mussoorie":

    print("- Visit Mall Road")
    print("- Explore Camel's Back Road")
    print("- Take the Cable Car to Gun Hill")

elif selected_destination == "Lonavala":

    print("- Thrilling Adventure Parks")
    print("- Scenic Monsoon Treks")
    print("- Peaceful Nature Spots")

elif selected_destination == "Lakshadweep":

    print("- Try Snorkeling")
    print("- Enjoy Boat Trip")
    print("- Enjoy Scuba Diving")

elif selected_destination == "Coorg":

    print("- Go River Rafting")
    print("- Take Jeep Rides to Misty Mountain Peaks")
    print("- Walk Through Aromatic Coffee Estates")

elif selected_destination == "Leh-Ladakh":

    print("- Explore Lakes")
    print("- Drive Across High Altitudes")
    print("- Explore Ancient Monasteries")


# ----------------------------
# BEST SEASON ⛅
# ----------------------------

if selected_destination == "Mussoorie":

    season = "March to June and October to February"

elif selected_destination == "Lonavala":

    season = "July to September"

elif selected_destination == "Coorg":

    season = "October to March"

elif selected_destination == "Leh-Ladakh":

    season = "June to September"

else:

    season = "October to February"


print()
print("Best season to visit:", season)


# -----------------------------
# ESTIMATED COST 💰
# -----------------------------

total_cost = budget.calculate_budget(
    selected_destination,
    people,
    days
)


# -----------------------------
# ITINERARY 📍
# -----------------------------

itinerary.show_itinerary(
    selected_destination,
    days
)


# -----------------------------
# FINAL SUMMARY 🤗
# -----------------------------

print()
print("*" * 60)
print("              YOUR DREAM TRIP SUMMARY")
print("*" * 60)

print()
print("Destination    :", selected_destination)
print("Travellers     :", people)
print("Trip Duration  :", days, "days")
print("Total Budget   : ₹", user_budget)
print("Estimated Cost : ₹", total_cost)
print("Transport      :", transport)
print("Hotel          :", hotel)
print("Best Season    :", season)

print()

if user_budget >= total_cost:

    print("Budget Status  : Within your budget")

else:

    print("Budget Status  : Estimated cost is above your budget")


functions.goodbye()

