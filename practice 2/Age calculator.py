# Age Calculator:
# Write a function calculate_age(birth_date_str) that takes a birth date string in "YYYY-MM-DD" format. The function should return the person's current age in years.

# Hint: Use the datetime module.

# Example: If today is 2025-07-31, calculate_age("1990-07-31") should return 35.

import datetime

def calculate_age(birth_date_str):
    # Convert the birth date string to a datetime object
    birth_date = datetime.datetime.strptime(birth_date_str, "%Y-%m-%d")
    
    # Get today's date
    today = datetime.datetime.now()
    
    # Calculate age
    age = today.year - birth_date.year 
    
    return age

# Example usage
if __name__ == "__main__":
    birth_date = "1990-07-01"
    age = calculate_age(birth_date)
    print(f"The person's age is: {age} years")