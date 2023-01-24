import requests as requests

hulk_url = 'https://akabab.github.io/superhero-api/api/id/25.json'
captain_url = 'https://akabab.github.io/superhero-api/api/id/24.json'
thanos_url = 'https://akabab.github.io/superhero-api/api/id/29.json'
hulk_response = requests.get(hulk_url)
hulk_data = hulk_response.json()
hulk_intelligence = hulk_data["powerstats"]["intelligence"]

captain_response = requests.get(captain_url)
captain_data = captain_response.json()
captain_intelligence = captain_data["powerstats"]["intelligence"]

thanos_response = requests.get(thanos_url)
thanos_data = thanos_response.json()
thanos_intelligence = thanos_data["powerstats"]["intelligence"]

if hulk_intelligence > captain_intelligence and hulk_intelligence > thanos_intelligence:
    print("Hulk is the smartest")
elif captain_intelligence > hulk_intelligence and captain_intelligence > thanos_intelligence:
    print("Captain America is the smartest")
else:
    print("Thanos is the smartest")