def weight_conversion(value, from_unit, to_unit):
    # Define conversion rates
    conversion_rates = {
        'kilograms': 1,
        'grams': 1000,
        'pounds': 2.20462,
        'ounces': 35.274
    }

    # Convert the value to kilograms first
    if from_unit not in conversion_rates or to_unit not in conversion_rates:
        raise ValueError("Invalid units provided. Use 'kilograms', 'grams', 'pounds', or 'ounces'.")

    value_in_kilograms = value / conversion_rates[from_unit]

    # Convert from kilograms to the desired unit
    converted_value = value_in_kilograms * conversion_rates[to_unit]

    return converted_value

# Example usage
if __name__ == "__main__":
    try:
        weight = float(input("Enter the weight: "))
        from_unit = input("Convert from (kilograms, grams, pounds, ounces): ").lower()
        to_unit = input("Convert to (kilograms, grams, pounds, ounces): ").lower()

        converted_weight = weight_conversion(weight, from_unit, to_unit)
        print(f"{weight} {from_unit} is equal to {converted_weight:.2f} {to_unit}.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print("An error occurred:", e)
