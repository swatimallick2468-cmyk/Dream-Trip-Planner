import budget
import destinations
import hotels

print("Testing Dream Trip Planner...")
print()

# Test 1: Destination
result = destinations.get_destination("1", "1")

if result == "Coorg":
    print("Destination test: PASSED")
else:
    print("Destination test: FAILED")


# Test 2: Hotel
result = hotels.get_hotel("Coorg", 10000)

if result == "Hotel Mayura Valley View":
    print("Hotel test: PASSED")
else:
    print("Hotel test: FAILED")


# Test 3: Budget
result = budget.calculate_budget("Coorg", 2, 3)

if result == 9000:
    print("Budget test: PASSED")
else:
    print("Budget test: FAILED")


print()
print("Testing completed.")