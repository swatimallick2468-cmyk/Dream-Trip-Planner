def show_itinerary(place, days):

    if place == "Mussoorie":

        itinerary = [
            ["Arrival and hotel check-in",
             "Visit Mall Road",
             "Visit Gun Hill"],

            ["Visit Kempty Falls",
             "Explore Landour",
             "Enjoy Local Cafes"],

            ["Visit Lal Tibba",
             "Explore Landour",
             "Watch the sunset"],

            ["Visit Company Garden",
             "Visit Camel's Back Road",
             "Relax at the hotel"],

            ["Visit George Everest",
             "Explore Nearby Viewpoint",
             "Enjoy sunset"],

            ["Visit Cloud's End",
             "Nature Walk",
             "Enjoy a peaceful evening"],

            ["Explore Mussoorie Lake",
             "Enjoy Boating",
             "Relax in the evening"],

            ["Visit Jharipani Falls",
             "Explore local surroundings",
             "Enjoy local food"],

            ["Free morning and shopping",
             "Explore Mall Road",
             "Enjoy at a local Cafe"],

            ["Relax at the hotel",
             "Last minute sightseeing",
             "Departure"]
        ]


    elif place == "Coorg":

        itinerary = [

            ["Arrive at hotel and check-in",
             "Explore Madikeri",
             "Relax at the Resort"],

            ["Visit Abbey Falls",
             "Explore Coffee Plantation",
             "Enjoy the evening"],

            ["Visit Raja's Seat",
             "Visit Madikeri Fort",
             "Watch the sunset"],

            ["Visit Mandalpatti",
             "Enjoy the scenic views",
             "Relax at Resort"],

            ["Visit Dubare",
             "Enjoy Nature activities",
             "Relax in the evening"],

            ["Visit Talacauvery",
             "Explore Bhagamandala",
             "Enjoy the evening"],

            ["Visit Nisargadhama",
             "Explore the surrounding",
             "Relax at the Resort"],

            ["Coffee plantation tour",
             "Learn about coffee making",
             "Enjoy local dinner"],

            ["Free morning",
             "Shopping and exploration",
             "Enjoy the evening"],

            ["Relax and pack",
             "Last minute sightseeing",
             "Departure"]
        ]


    elif place == "Lakshadweep":

        itinerary = [

            ["Arrival and hotel check-in",
             "Explore the Island",
             "Relax on the Beach"],

            ["Beach Walk",
             "Try snorkelling",
             "Enjoy the sunset"],

            ["Explore coral reefs",
             "Try Kayaking",
             "Relax by the sea"],

            ["Boat Trips",
             "Enjoy water activities",
             "Beach relaxation"],

            ["Try scuba diving",
             "Explore Marine life",
             "Enjoy sunset view"],

            ["Explore local surroundings",
             "Visit nearby Beaches",
             "Relax at the Resort"],

            ["Glass-bottom boat ride",
             "Explore coral reefs",
             "Enjoy evening"],

            ["Enjoy Canoeing",
             "Photoshoot at beach",
             "Watch the sunset"],

            ["Free morning",
             "Shopping and try local foods",
             "Enjoy a beach dinner"],

            ["Relax at the resort",
             "Last beach visit",
             "Departure time"]
        ]


    elif place == "Leh-Ladakh":

        itinerary = [

            ["Arrival and hotel check-in",
             "Explore nearby monasteries",
             "Rest at the hotel"],

            ["Explore Leh Market",
             "Explore Leh Palace",
             "Visit Shanti Stupa"],

            ["Visit Thiksey Monastery",
             "Explore Shey Palace",
             "Enjoy the evening"],

            ["Travel to Nubra Valley",
             "Explore the Valley",
             "Relax at the campsite"],

            ["Visit Diskit Monastery",
             "Camel ride in Nubra",
             "Enjoy the evening"],

            ["Travel towards Pangong Lake",
             "Explore Pangong Lake",
             "Watch the sunset"],

            ["Explore Pangong Lake",
             "Enjoy the scenic views",
             "Relax at the campsite"],

            ["Return towards Leh",
             "Visit local attractions",
             "Relax at the hotel"],

            ["Visit Magnetic Hill",
             "Explore some local food",
             "Enjoy the evening"],

            ["Enjoy the evening",
             "Shopping in Leh",
             "Departure time"]
        ]


    elif place == "Lonavala":

        itinerary = [

            ["Arrival and hotel check-in",
             "Explore Lonavala",
             "Relax in the evening"],

            ["Visit Tiger Point",
             "Explore Khandala",
             "Watch the sunset"],

            ["Visit Bhaja Caves",
             "Explore Lohagad Fort",
             "Relax at the hotel"],

            ["Visit Karla Caves",
             "Explore local surroundings",
             "Enjoy the evening"],

            ["Visit Pawna Lake",
             "Enjoy scenic views",
             "Watch the sunset"],

            ["Visit Bhushi Dam",
             "Explore nearby waterfalls",
             "Relax in the evening"],

            ["Explore Rajmachi",
             "Enjoy nature and views",
             "Relax at the hotel"],

            ["Visit Kune Waterfalls",
             "Explore Khandala",
             "Enjoy the evening"],

            ["Free morning",
             "Shopping and local cafes",
             "Enjoy the sunset"],

            ["Relax and pack",
             "Last-minute sightseeing",
             "Departure time"]
        ]


    print()
    print("=" * 60)
    print("             🫵  YOUR DAY-WISE ITINERARY")
    print("=" * 60)

    
    # 1-day trip
    if days == 1:

        print()
        print("DAY 1")
        print("-" * 40)

        print("Morning   : Arrive and explore the destination")
        print("Afternoon : Visit the main attraction")
        print("Evening   : Return home")
        print("Trip Completed!")
        return

    for day in range(1, days + 1):

        print()
        print("DAY", day)
        print("-" * 40)

        # If this is the last selected day,
        # make it the departure day.

        if day == days:

            print(" 🌅  Morning   : Your last morning")
            print(" 🌤️  Afternoon : Hotel checkout and departure")
            print(" 🌆  Evening   : Reach your home")
            print("Finally Trip Completed! 🤗 💖")

        else:

            activity = itinerary[day - 1]

            print(" 🌅  Morning   :", activity[0])
            print(" 🌤️  Afternoon :", activity[1])
            print(" 🌆  Evening   :", activity[2])