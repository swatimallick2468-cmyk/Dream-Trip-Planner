def show_destinations(interest):

    if interest == "1":
        print()
        print("Beautiful choice! Time to escape into the wild! 😃")
        print()
        print("Recommended destinations:")
        print("1. Coorg")
        print("2. Mussoorie")
        print("3. Lonavala")

    elif interest == "2":
        print()
        print("Get ready for some thrilling memories! 🔥")
        print()
        print("Recommended destinations:")
        print("1. Leh-Ladakh")
        print("2. Lonavala")

    elif interest == "3":
        print()
        print("Get ready for sunshine, waves and sunsets! 🌊")
        print()
        print("Recommended destinations:")
        print("1. Lakshadweep")
        print("2. Lonavala")

    elif interest == "4":
        print()
        print("Let's find places worth capturing! 📸")
        print()
        print("Recommended destinations:")
        print("1. Mussoorie")
        print("2. Leh-Ladakh")
        print("3. Lakshadweep")

    elif interest == "5":
        print()
        print("Time to escape the chaos and recharge! 😜")
        print()
        print("Recommended destinations:")
        print("1. Coorg")
        print("2. Mussoorie")


def get_destination(interest, choice):

    if interest == "1":

        if choice == "1":
            return "Coorg"
        elif choice == "2":
            return "Mussoorie"
        else:
            return "Lonavala"

    elif interest == "2":

        if choice == "1":
            return "Leh-Ladakh"
        else:
            return "Lonavala"

    elif interest == "3":

        if choice == "1":
            return "Lakshadweep"
        else:
            return "Lonavala"

    elif interest == "4":

        if choice == "1":
            return "Mussoorie"
        elif choice == "2":
            return "Leh-Ladakh"
        else:
            return "Lakshadweep"

    else:

        if choice == "1":
            return "Coorg"
        else:
            return "Mussoorie"