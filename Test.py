# Initial parameters
monthly_savings = 10000  # Initial monthly savings
annual_increase_rate = 0.10  # Annual increase rate for monthly savings
annual_return_rate = 0.40  # Annual return rate on savings
extra_income_rate = 0.30  # Extra income as percentage of monthly savings
years_to_calculate = [1, 2, 3, 5, 15, 30]  # Years for which to calculate savings

# Initialize savings and extra income
total_savings = 0
extra_income_savings = 0

# Monthly compound interest factor
monthly_return_factor = (1 + annual_return_rate) ** (1 / 12) - 1


# Function to calculate compound interest
def compound_interest(principal, rate, periods):
    return principal * ((1 + rate) ** periods)


# Dictionary to store results
results = {}

# Reset monthly savings to initial value
monthly_savings = 10000

# Calculate savings for each year
for year in range(1, 31 + 1):
    for month in range(1, 12 + 1):
        # Calculate new savings for the month
        total_savings += monthly_savings
        total_savings *= (1 + monthly_return_factor)

        # Calculate extra income for the month
        extra_income = monthly_savings * extra_income_rate
        extra_income_savings += extra_income
        extra_income_savings *= (1 + monthly_return_factor)

    # Increase monthly savings for the next year
    monthly_savings *= (1 + annual_increase_rate)

    # Store results for the specified years
    if year in years_to_calculate:
        results[year] = {
            'total_savings': total_savings,
            'extra_income_savings': extra_income_savings,
            'combined_savings': total_savings + extra_income_savings
        }

print(results)