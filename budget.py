def calculate_budget(place, people, days):

    if place == "Coorg":
        cost_per_person = 1500

    elif place == "Mussoorie":
        cost_per_person = 1800

    elif place == "Lonavala":
        cost_per_person = 1400

    elif place == "Lakshadweep":
        cost_per_person = 3500

    elif place == "Leh-Ladakh":
        cost_per_person = 3000

    total = cost_per_person * people * days

    return total