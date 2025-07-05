from datetime import date, timedelta
import pandas as pd

today = date.today()

# five years ago
five_years_ago = today.replace(year=today.year - 5)

# load ufc_event_details.csv into a DataFrame named events
events = pd.read_csv("ufc_event_details.csv")

# change the dtype of the date column to datetime64
events['DATE'] = pd.to_datetime(events['DATE'])

# only keep events that are 5 years old or newer
events = events[events['DATE'].dt.date >= five_years_ago]

# change all column names to lowercase
events.columns = events.columns.str.lower()

# save the events dataframe to a csv file named fight_events.csv
events.to_csv("fight_events.csv", index=False)

# load ufc_fight_details.csv into a DataFrame named fights
fights = pd.read_csv("ufc_fight_details.csv")
#print(fights.head())
#fights.info()

# only keep the rows where fight['EVENT'] isin events['event']
fights = fights[fights['EVENT'].isin(events['event'])]

# change all column names to lowercase
fights.columns = fights.columns.str.lower()

# save the fights dataframe to a csv file named fight_details.csv
fights.to_csv("fight_details.csv", index=False)

#fights.info()
#print(fights.head())

# load ufc_fight_results,csv into a DataFrame named fight_results
fight_results = pd.read_csv("ufc_fight_results.csv")
fight_results.info()
# print(fight_results.head())

# change all column names to lowercase
fight_results.columns = fight_results.columns.str.lower()

# only keep the rows where fight_results['event'] isin events['event']
fight_results = fight_results[fight_results['event'].isin(events['event'])]



# save the fight_results dataframe to a csv file named fight_results.csv
fight_results.to_csv("fight_results.csv", index=False)

fight_results.info()
print(fight_results.head())




