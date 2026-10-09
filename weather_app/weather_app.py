import requests

def get_info(place):
    url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": place,
        "format": "jsonv2",
        "limit": 1
    }

    headers = {
        "User-Agent": "LocFinder/1.0"
    }

    try:
        # Send GET request to the API
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=10
        )
        response.raise_for_status()

        results = response.json()

        if not results:
            return None

        return {
            "latitude": float(results[0]["lat"]),
            "longitude": float(results[0]["lon"]),
            "name": results[0]["display_name"]
        }
    except requests.RequestException as error:
        print("API request failed:", error)
        return None

def find_weather(latitude , longitude):

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

    # Make the request
    response = requests.get(url)
    data = response.json()

    print(data)

def start():
    print("Welcome to the weather finder.")
    while(True):
        place = input("Location : ")
        loc = get_info(place)
        if loc:
            print(f"Current weather of {loc['name']}: \n")
            find_weather(loc["latitude"] , loc["longitude"])
        repeat = input("Find for new location?(y/n):")
        if repeat.lower()=="y":
            continue
        else:
            print("Thank you for using the weather app.")
            break

start()
