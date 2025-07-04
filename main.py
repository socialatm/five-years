from datetime import date, timedelta
import pandas as pd

today = date.today()

# five years ago
five_years_ago = today - timedelta(days=365 * 5)

# load ufc_event_details.csv into a DataFrame named events
events = pd.read_csv("ufc_event_details.csv")

# change the dtype of the date column to datetime64
events['DATE'] = pd.to_datetime(events['DATE'])

# only keep events that are 5 years old or newer
events = events[events['DATE'].dt.date >= five_years_ago]

# change all column names to lowercase
events.columns = events.columns.str.lower()

# save the events dataframe to a csv file named ufc_events.csv
events.to_csv("ufc_events.csv", index=False)
