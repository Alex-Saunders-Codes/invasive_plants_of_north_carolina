from bs4 import BeautifulSoup
import requests
import pandas as pd


invasive_df = pd.read_csv('Invasives/north_carolina_composites.csv')
invasive_df.head()
failed = []
def get_distribution(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    results = soup.find('table', class_='distribution')
    return results

extended_invasives = []

for spec in invasive_df.itertuples():
    url = spec.Datasheet_URL
    try: 
        dist_table = str(get_distribution(url))
        countries_df = pd.read_html(dist_table)[0]
    except:
        failed.append(spec._asdict())
        pass
    countries_df.rename(columns={'Continent/Country/Region':'country'}, inplace=True)
    native_countries = []
    introduced_countries = []
    invasive_countries = []
    last_reported = []
    first_reported = []
    present = []
    species= spec._asdict()
    for row in countries_df.itertuples():
        if pd.isnull(row.Distribution):
            pass
        elif "Present" in row.Distribution:
            if row.Origin == "Native":
                native_countries.append(row.country)
            elif row.Origin == "Introduced":
                introduced_countries.append(row.country)
            elif row.Invasive == "Invasive":
                invasive_countries.append(row.country)
            present.append(row.country)         
            species['native'] = native_countries
            species['introduced'] = introduced_countries
            species['invasive'] = invasive_countries
            species['present'] = present
    extended_invasives.append(species)


invasive_locs = pd.DataFrame(extended_invasives)

failed_tables = pd.DataFrame(failed)

invasive_locs.to_csv("invasives/invasive_locs.csv")

failed_tables.to_csv('invasives/failed_tables.csv')