import requests
import pandas as pd
import time
from datetime import datetime

API_KEY = "3d82af7e0daee7c11d99bd357720ebbb"
START_YEAR = 2017
END_YEAR = 2025
NETFLIX_PROVIDER_ID = 8  # Netflix provider ID on TMDB
NETFLIX_NETWORK_ID = 213  # Only used for TV
REGIONS = ["US", "IN", "BR", "GB", "CA", "AU", "MX", "DE", "FR", "JP"]  # Top 10 Netflix markets
MIN_VOTE_COUNT = 5
SLEEP_BETWEEN_CALLS = 0.25

def fetch_netflix_content(media_type="tv"):
    all_data = []

    for region in REGIONS:
        for year in range(START_YEAR, END_YEAR + 1):
            print(f"\n📡 Fetching {media_type.upper()} for {year} in {region}")
            page = 1
            total_pages = 1

            while page <= total_pages and page <= 500:
                url = f"https://api.themoviedb.org/3/discover/{media_type}"
                params = {
                    "api_key": API_KEY,
                    "sort_by": "popularity.desc",
                    "vote_count.gte": MIN_VOTE_COUNT,
                    "with_original_language": "en",
                    "page": page,
                    "region": region,
                    "watch_region": region,
                    "with_watch_providers": NETFLIX_PROVIDER_ID
                }

                if media_type == "tv":
                    params["first_air_date_year"] = year
                    params["with_networks"] = NETFLIX_NETWORK_ID
                else:
                    params["primary_release_year"] = year

                response = requests.get(url, params=params)
                if response.status_code != 200:
                    print(f"❌ Error: {response.status_code} on page {page}")
                    break

                data = response.json()
                total_pages = data.get("total_pages", 1)

                for item in data.get("results", []):
                    all_data.append({
                        "title": item.get("name") if media_type == "tv" else item.get("title"),
                        "media_type": media_type,
                        "release_date": item.get("first_air_date") if media_type == "tv" else item.get("release_date"),
                        "popularity": item.get("popularity"),
                        "overview": item.get("overview"),
                        "language": item.get("original_language"),
                        "genre_ids": item.get("genre_ids", []),
                        "vote_count": item.get("vote_count"),
                        "region": region
                    })

                page += 1
                time.sleep(SLEEP_BETWEEN_CALLS)

    return all_data

def get_genre_mapping(media_type="movie"):
    url = f"https://api.themoviedb.org/3/genre/{media_type}/list"
    params = {"api_key": API_KEY}
    response = requests.get(url, params=params)
    genre_dict = {}
    if response.status_code == 200:
        for genre in response.json()["genres"]:
            genre_dict[genre["id"]] = genre["name"]
    return genre_dict

# Fetch TV and movie data
tv_data = fetch_netflix_content("tv")
movie_data = fetch_netflix_content("movie")
all_data = tv_data + movie_data

# Clean and enrich
df = pd.DataFrame(all_data)
df.dropna(subset=["release_date"], inplace=True)
df["release_year"] = pd.to_datetime(df["release_date"]).dt.year

# Genre mapping
movie_genres = get_genre_mapping("movie")
tv_genres = get_genre_mapping("tv")
genre_lookup = {**movie_genres, **tv_genres}
df["genres"] = df["genre_ids"].apply(lambda ids: [genre_lookup.get(gid) for gid in ids if gid in genre_lookup])
df.drop(columns=["genre_ids"], inplace=True)

# Save
output_path = "/Users/chaitanya/Desktop/NETFLIX/netflix_releases_top10regions_2017_2025.csv"
df.to_csv(output_path, index=False)
print(f"\n✅ Data saved to '{output_path}' with regions: {REGIONS}")
