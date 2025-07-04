from datetime import date, timedelta
import pandas as pd

today = date.today()

# five years ago
five_years_ago = today - timedelta(days=365 * 5)
print(f"Five years ago: {five_years_ago}")

# load ufc_event_details.csv into a DataFrame named events
events = pd.read_csv("ufc_event_details.csv")
print(events.head())

# also print the info
events.info()

# change the dtype of the date column to datetime64
events['DATE'] = pd.to_datetime(events['DATE'])

#events.info()

# drop all rows whose date is older thanfive_years_ago
# events.drop(events[events['date'].dt.date < five_years_ago].index, inplace=True)

# A more common and readable way to filter the DataFrame
events = events[events['DATE'].dt.date >= five_years_ago]

events.info()

# save the events dataframe to a csv file named ufc_events.csv
events.to_csv("ufc_events.csv", index=False)

