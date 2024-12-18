import requests

def get_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    if response.status_code == 200:
        joke = response.json()
        return f"{joke['setup']} - {joke['punchline']}"
    else:
        return "Failed to fetch a joke."

def get_weather():
    api_key = "your_api_key"
    city = "your_city"
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")
    if response.status_code == 200:
        weather = response.json()
        return f"Weather in {city}: {weather['weather'][0]['description']}, Temperature: {weather['main']['temp']}K"
    else:
        return "Failed to fetch weather."

def get_recipe():
    response = requests.get("https://www.themealdb.com/api/json/v1/1/random.php")
    if response.status_code == 200:
        recipe = response.json()
        return f"Recipe: {recipe['meals'][0]['strMeal']}, Instructions: {recipe['meals'][0]['strInstructions']}"
    else:
        return "Failed to fetch a recipe."

def main():
    print(get_joke())
    print(get_weather())
    print(get_recipe())

if __name__ == "__main__":
    main()
