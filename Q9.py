def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5

    if speed <= 60:
        return "No Challan"
    elif 61 <= speed <= 80:
        return "Small Challan"
    else:
        return "Heavy Challan"

# Example usage:
result1 = caught_speeding(81, True)
result2 = caught_speeding(81, False)

print("Result 1:", result1)  # Output: "Small Challan"
print("Result 2:", result2)  # Output: "Heavy Challan"



