import requests

# Philippines, and this is inaccurate btw
# Don't expect this to be 100% accurate. this is fucked up.

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"  # j1 = FUCKING JSON format
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f"\n[!] FUCKING HTTP ERROR SHIT: {http_err}")
        return None
    except requests.exceptions.ConnectionError as conn_err:
        print(f"\n[!] YOUR CONNECTION SUCKS: {conn_err}")
        return None
    except requests.exceptions.Timeout as timeout_err:
        print(f"\n[!] TOOK TOO LONG THIS SHIT SUX: {timeout_err}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"\n[!] IDK WHAT CAUSED THIS ERROR: {err}")
        return None

    try:
        data = resp.json()
    except ValueError:
        print("\n[!] ERROR BEEP BOOP FUCK YOU.")
        return None

    # Simplified info because why not?
    try:
        current = data["current_condition"][0]
        return {
            "temperature": current["temp_C"],
            "humidity": current["humidity"],
            "description": current["weatherDesc"][0]["value"],
            "feels_like": current["FeelsLikeC"]
        }
    except (KeyError, IndexError) as parse_err:
        print(f"\n[!] DATAS FAILED TO FUCK YOU: {parse_err}")
        return None


if __name__ == "__main__":
    city = input("\n[!] Enter city in Philippines: ")
    weather = get_weather(city)
    if weather:
        print(f"\nWeather in {city}:")
        print(f"Temperature: {weather['temperature']}°C (feels like {weather['feels_like']}°C)")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Condition: {weather['description']}\n")
    else:
        print("[!] IM NOT GONNA FETCH THE WEATHERS BECAUSE YOU ARE STUPID SHIT.\n")
