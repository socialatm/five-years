from datetime import date, timedelta

today = date.today()

# Add a duration to a date
future_date = today + timedelta(days=10)
print(f"Date in 10 days: {future_date}")

# five years ago
five_years_ago = today - timedelta(days=365 * 5)
print(f"Five years ago: {five_years_ago}")
