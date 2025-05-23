# Initial Data Gathering Testing with NHL API using POSTMAN and NHL.com endpoints

import requests
import pandas as pd

# r = requests.get("https://api.nhle.com/stats/rest/en/franchise?sort=fullName&include=lastSeason.id&include=firstSeason.id")
# team_data = r.json()

# df = pd.json_normalize(team_data['data'])
# df = df[df["lastSeason.id"].isnull()]
# df = df.drop(columns=["lastSeason", "lastSeason.id"])
# df = df.rename(columns={"teamCommonName": "TeamName", "teamPlaceName": "City", "firstSeason.id": "FirstSeasonID", "id": "ID", "fullName": "FullName"})
# cols = df.columns.to_list()
# cols[2], cols[3] = cols[3], cols[2]
# df = df[cols]

# r = requests.get(f"https://api.nhle.com/stats/rest/en/team/summary?sort=teamFullName&cayenneExp=seasonId=20242025%20and%20gameTypeId=2")
# team_stats = r.json()

# df = pd.json_normalize(team_stats["data"])
# df = df.drop(columns=["ties"])


# cols = df.columns.to_list()
# cols[0], cols[18] = cols[18], cols[0]
# df = df[cols]
# df.to_csv("NHLTeamsBasicStats.csv", index=False)
# headers = {
#     'User-Agent': 'my-app/1.0',
#     'Accept': 'text/csv',
# }
# for i in range(1, 1313):
#     game_id = f"{i:04}"
#     url = f"https://moneypuck.com/moneypuck/gameData/20242025/202402{game_id}.csv"
#     response = requests.get(url, headers=headers)
#     if response.status_code != 200:
#         print(f"Failed to retrieve data for game ID: 202402{game_id}, Status Code: {response.status_code}")
#         continue
#     game_data = response.json()
#     game_df = pd.json_normalize(game_data)
#     game_df.to_csv(f"PBP/202402{game_id}.csv", index=False)
#     print(f"Game 202402{game_id} data saved.")

"""
20242025 Games 
October: 0001-0167 
November: 0168-0387
December: 0388-601
January: 602-825
February: 826-947
March: 948-1181
April: 1182-1312
"""


        # download_playoff_csv_files(BASE_URL+"/"+link, link)
    
def download_reg_csv_files(BASE_URL, DOWNLOAD_DIR):
    import os
    import requests
    from bs4 import BeautifulSoup
    import datetime
    import pandas as pd

    reg_dict = {
        1: "/January",
        2: "/February",
        3: "/March",
        4: "/April",
        10: "/October",
        11: "/November",
        12: "/December"
    }

    # Configuration
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "text/csv"
    }

    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    # Get page content
    response = requests.get(BASE_URL, headers=HEADERS)
    if response.status_code != 200:
        print(f"Failed to retrieve page: {response.status_code}")
        return
    soup = BeautifulSoup(response.text, "html.parser")

    # Find CSV links
    csv_links = [
        link.get("href") for link in soup.find_all("a")
        if link.get("href", "").startswith(f"{DOWNLOAD_DIR[:5]}02") and link.get("href", "").endswith(".csv")
    ]

    # Download files with existence check
    for link in csv_links:
        full_url = f"{BASE_URL}/{link.lstrip('/')}" if not link.startswith("http") else link
        # DOWNLOAD_DIR += playoff_dict.get(link[6:9], "")
        filename = os.path.join(DOWNLOAD_DIR, os.path.basename(link).split("?")[0])
        # DOWNLOAD_DIR = DOWNLOAD_DIR[:-9]  # Reset DOWNLOAD_DIR for next iteration

        if os.path.exists(filename):  # Existence check [1][2][4]
            print(f"Skipping existing file: {filename}")
            continue

        try:
            response = requests.get(full_url, headers=HEADERS)
            response.raise_for_status()
            df = pd.read_csv(response.content.decode('utf-8'))
            game_date = df.game_date[0]
            date_obj = datetime.datetime.strptime(game_date, "%A %B %d %Y")
            month_number = date_obj.month 
            month_name = reg_dict.get(month_number, "Unknown")
            filename.os.path.join(DOWNLOAD_DIR+month_name, os.path.basename(link).split("?")[0])
            
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"Downloaded: {filename}")
            
        except requests.exceptions.RequestException as e:
            print(f"Download failed: {full_url} - {e}")

def download_playoff_csv_files(BASE_URL, DOWNLOAD_DIR):
    import os
    import requests
    from bs4 import BeautifulSoup
    import datetime
    import pandas as pd

    # playoff_dict = {
    #     "11": "/TORvsOTT",
    #     "012": "/FLAvsTBL",
    #     "013": "/WSHvsMTL",
    #     "014": "/CARvsNJD",
    #     "015": "/WPGvsSTL",
    #     "016": "/DALvsCOL",
    #     "017": "/VGKvsMIN",
    #     "018": "/LAKvsEDM"
    # }
    # Configuration
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "text/csv"
    }

    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    # Get page content
    response = requests.get(BASE_URL, headers=HEADERS)
    if response.status_code != 200:
        print(f"Failed to retrieve page: {response.status_code}")
        return
    soup = BeautifulSoup(response.text, "html.parser")

    # Find CSV links
    csv_links = [
        link.get("href") for link in soup.find_all("a")
        if link.get("href", "").startswith(f"{DOWNLOAD_DIR[:5]}03") and link.get("href", "").endswith(".csv")
    ]

    # Download files with existence check
    for link in csv_links:
        full_url = f"{BASE_URL}/{link.lstrip('/')}" if not link.startswith("http") else link
        # DOWNLOAD_DIR += playoff_dict.get(link[6:9], "")
        filename = os.path.join(DOWNLOAD_DIR, os.path.basename(link).split("?")[0])
        # DOWNLOAD_DIR = DOWNLOAD_DIR[:-9]  # Reset DOWNLOAD_DIR for next iteration

        if os.path.exists(filename):  # Existence check [1][2][4]
            print(f"Skipping existing file: {filename}")
            continue

        try:
            response = requests.get(full_url, headers=HEADERS)
            response.raise_for_status()
            df = pd.read_csv(response.content.decode('utf-8'))
            
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"Downloaded: {filename}")
            
        except requests.exceptions.RequestException as e:
            print(f"Download failed: {full_url} - {e}")

def get_season_header(BASE_URL):
    import requests
    from bs4 import BeautifulSoup

    # Configuration
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "text/csv"
    }

    # Get page content
    response = requests.get(BASE_URL, headers=HEADERS)
    if response.status_code != 200:
        print(f"Failed to retrieve page: {response.status_code}")
        return None
    soup = BeautifulSoup(response.text, "html.parser")
    
    season_links = [
        link.get("href") for link in soup.find_all("a")
        if link.get("href", "").startswith("20")
    ]

    # Extract header from the response
    for link in season_links:
        if link != "20242025":
            download_reg_csv_files(BASE_URL+link+"/", "NHLGameDataPBP/"+link)

get_season_header("https://moneypuck.com/moneypuck/gameData/") 

def download_new_playoff_csv_files(BASE_URL, DOWNLOAD_DIR):
    import os
    import requests
    from bs4 import BeautifulSoup

    playoff_dict = {
        "011": "/TORvsOTT",
        "012": "/FLAvsTBL",
        "013": "/WSHvsMTL",
        "014": "/CARvsNJD",
        "015": "/WPGvsSTL",
        "016": "/DALvsCOL",
        "017": "/VGKvsMIN",
        "018": "/LAKvsEDM",
        "021": "/TORvsFLA",
        "022": "/WSHvsCAR",
        "023": "/WPGvsDAL",
        "024": "/VGKvsEDM",
        "031": "/CARvsFLA",
        "032": "/DALvsEDM"
    }

    # Configuration
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "text/csv"
    }

    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    # Get page content
    response = requests.get(BASE_URL, headers=HEADERS)
    if response.status_code != 200:
        print(f"Failed to retrieve page: {response.status_code}")
        return
    soup = BeautifulSoup(response.text, "html.parser")

    # Find CSV links
    csv_links = [
        link.get("href") for link in soup.find_all("a")
        if link.get("href", "").startswith("202403") and link.get("href", "").endswith(".csv")
    ]

    # Download files with existence check
    for link in csv_links:
        full_url = f"{BASE_URL}/{link.lstrip('/')}" if not link.startswith("http") else link
        DOWNLOAD_DIR += playoff_dict.get(link[6:9], "")
        filename = os.path.join(DOWNLOAD_DIR, os.path.basename(link).split("?")[0])
        DOWNLOAD_DIR = DOWNLOAD_DIR[:-9]  # Reset DOWNLOAD_DIR for next iteration

        if os.path.exists(filename):  # Existence check [1][2][4]
            print(f"Skipping existing file: {filename}")
            continue

        try:
            response = requests.get(full_url, headers=HEADERS)
            response.raise_for_status()
            
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"Downloaded: {filename}")
            
        except requests.exceptions.RequestException as e:
            print(f"Download failed: {full_url} - {e}")

# def download_new_playoff_csv_files(BASE_URL, DOWNLOAD_DIR):
#     import os
#     import requests
#     from bs4 import BeautifulSoup

#     playoff_dict = {
#         "011": "/TORvsOTT",
#         "012": "/FLAvsTBL",
#         "013": "/WSHvsMTL",
#         "014": "/CARvsNJD",
#         "015": "/WPGvsSTL",
#         "016": "/DALvsCOL",
#         "017": "/VGKvsMIN",
#         "018": "/LAKvsEDM"
#     }

#     # Configuration
#     HEADERS = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
#         "Accept": "text/csv"
#     }

#     os.makedirs(DOWNLOAD_DIR, exist_ok=True)

#     # Get page content
#     response = requests.get(BASE_URL, headers=HEADERS)
#     if response.status_code != 200:
#         print(f"Failed to retrieve page: {response.status_code}")
#         return
#     soup = BeautifulSoup(response.text, "html.parser")

#     # Find CSV links
#     csv_links = [
#         link.get("href") for link in soup.find_all("a")
#         if link.get("href", "").startswith("202403") and link.get("href", "").endswith(".csv")
#     ]

#     # Download files with existence check
#     for link in csv_links:
#         full_url = f"{BASE_URL}/{link.lstrip('/')}" if not link.startswith("http") else link
#         # DOWNLOAD_DIR += playoff_dict.get(link[6:9], "")
#         filename = os.path.join(DOWNLOAD_DIR, os.path.basename(link).split("?")[0])
#         # DOWNLOAD_DIR = DOWNLOAD_DIR[:-9]  # Reset DOWNLOAD_DIR for next iteration

#         if os.path.exists(filename):  # Existence check [1][2][4]
#             print(f"Skipping existing file: {filename}")
#             continue

#         try:
#             response = requests.get(full_url, headers=HEADERS)
#             response.raise_for_status()
            
#             with open(filename, "wb") as f:
#                 f.write(response.content)
#             print(f"Downloaded: {filename}")
            
#         except requests.exceptions.RequestException as e:
#             print(f"Download failed: {full_url} - {e}")


def json_files_to_csv(BASE_URL, DOWNLOAD_DIR):
    import os
    import json

    # Configuration
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/json"  # Prioritize JSON responses
    }

    # Ensure download directory exists
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    # Step 1: Get page content
    response = requests.get(BASE_URL, headers=HEADERS)
    if response.status_code != 200:
        print(f"Failed to retrieve the page, status code: {response.status_code}")
        exit()

    # Step 2: Parse JSON data
    try:
        json_data = response.json()
    except json.JSONDecodeError:
        print("Failed to decode JSON data.")
        exit()

    # Step 3: Save JSON data to file
    # filename = os.path.join(DOWNLOAD_DIR, "data.json")
    # with open(filename, "w") as f:
    #     json.dump(json_data, f, indent=4)

    # print(f"Downloaded JSON data to {filename}")

    schedule_df = pd.json_normalize(json_data)
    schedule_df = schedule_df.sort_values(by=["id"])
    schedule_df.rename(columns={"h": "homeAbbrev", "a": "awayAbbrev"}, inplace=True)
    schedule_df['est'] = pd.to_datetime(schedule_df['est'], format='%Y%m%d %H:%M:%S').dt.strftime('%Y %B %d %H:%M:%S')
    schedule_df = schedule_df[["id", "homeAbbrev", "awayAbbrev", "est"]]
    schedule_df.to_csv(os.path.join(DOWNLOAD_DIR, f"{season}.csv"), index=False)

season = "20242025"
BASE_URL =f"https://www.moneypuck.com/moneypuck/OldSeasonScheduleJson/SeasonSchedule-{season}.json"
dir = "NHLGameDataPBP/20242025/Playoffs"
download_new_playoff_csv_files(f"https://moneypuck.com/moneypuck/gameData/20242025/", dir)
json_files_to_csv(BASE_URL, dir)



# def merge_goalie_csv_files(game_id):
#     import os
#     import pandas as pd
#     try:
#         away_df = pd.read_csv(f"{directory}/{game_id}A.csv")
#         away_df.drop(columns=["author_id", "text"], inplace=True)
#         away_df = away_df.rename(columns={"tweet_id": "a_tweet_id", "handle": "a_handle", "created_at": "a_created_at", "found_at": "a_found_at", "goalie_id": "a_goalie_id", "goalie_name": "a_goalie_name"})    
#         home_df = pd.read_csv(f"{directory}/{game_id}H.csv")
#         home_df.drop(columns=["author_id", "text"], inplace=True)
#         home_df = home_df.rename(columns={"tweet_id": "h_tweet_id", "handle": "h_handle", "created_at": "h_created_at", "found_at": "h_found_at", "goalie_id": "h_goalie_id", "goalie_name": "h_goalie_name"})


#         # Concatenate all DataFrames into one
#         merged_df = away_df.join(home_df, how='inner')

#         # Save the merged DataFrame to a new CSV file
#         merged_df.to_csv(os.path.join(directory, f"{game_id}.csv"), index=False)

#     except Exception as e:
#         print(f"Error processing game {game_id}: {e}")

# # for i in range(190000, 200008):
# #     game_id = f"2023{i:06}"
# #     merge_goalie_csv_files(game_id)
# #     print(f"Game {game_id} data saved.")

# def delete_partial_csv_files():
#     import os
#     import pandas as pd

#     # Directory containing the CSV files
    

#     for file in os.listdir(directory):
#         if file.endswith("A.csv") or file.endswith("H.csv"):
#             base_id = file[:-5]  # Remove the last 5 characters (e.g., "A.csv" or "H.csv")
#             combined_file = f"{base_id}.csv"
#             if os.path.exists(os.path.join(directory, combined_file)):
#                 os.remove(os.path.join(directory, file))
#                 print(f"Deleted partial file: {file}")

# # delete_partial_csv_files()

