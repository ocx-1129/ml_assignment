import requests
import pandas as pd

lat = 51.5074
lon = -0.1278

url = "https://archive-api.open-meteo.com/v1/archive"

params = {
    "latitude": lat,
    "longitude": lon,
    "start_date": "2023-01-01",
    "end_date": "2024-12-31",
    "hourly": "temperature_2m,relativehumidity_2m,pressure_msl,wind_speed_10m,wind_direction_10m,precipitation",
    "timezone": "UTC"
}

r = requests.get(url, params=params)
data = r.json()

df = pd.DataFrame(data["hourly"])
df["time"] = pd.to_datetime(df["time"])
df = df.set_index("time")

# Resample to 30 minutes
df_30 = df.resample("30min").interpolate()

df_30.to_csv("london_2023_24_halfhour_interp.csv")

print(df_30.head())
