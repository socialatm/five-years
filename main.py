from datetime import date, timedelta

today = date.today()

# five years ago
five_years_ago = today - timedelta(days=365 * 5)
print(f"Five years ago: {five_years_ago}")
