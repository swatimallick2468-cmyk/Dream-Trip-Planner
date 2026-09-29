def get_hotel(place, budget):

    if place == "Mussoorie":

        if budget < 15000:
            return "The Fern Brentwood Resort"

        elif budget < 40000:
            return "Welcomhotel The Savoy"

        else:
            return "JW Marriott Mussoorie Walnut grove"


    elif place == "Lonavala":

        if budget < 15000:
            return "Chandralok Hotel"

        elif budget < 40000:
            return "The Lagoon Resort"

        else:
            return "Della Resorts"


    elif place == "Coorg":

        if budget < 15000:
            return "Hotel Mayura Valley View"

        elif budget < 40000:
            return "Coorg Cliffs Resort"

        else:
            return "Evolve Back Coorg"


    elif place == "Lakshadweep":

        if budget < 15000:
            return "Kavaratti Island Resort"

        elif budget < 40000:
            return "Kadmat Beach Resort"

        else:
            return "Bangaram Island Resort"


    elif place == "Leh-Ladakh":

        if budget < 15000:
            return "Hotel Shambhala"

        elif budget < 40000:
            return "The Grand Dragon Hotel"

        else:
            return "The Indus River Camp"