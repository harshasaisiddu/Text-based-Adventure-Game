import requests
import json
import time
from datetime import datetime

API_KEY="61f539fae57e4a9da2f182140230509"

WEATHER_API_URL="http://api.weatherapi.com/v1/current.json"
FORECAST_API_URL="http://api.weatherapi.com/v1/forecast.json"

favorite_cities = []

def check_weather(city_name):
    try:
        params={"key": API_KEY, "q": city_name}
        response=requests.get(WEATHER_API_URL,params=params)
        data = response.json()

        if "error" in data:
            print(f"Error: {data['error']['message']}")
        else:
            city=data["location"]["name"]
            country=data["location"]["country"]
            temperature=data["current"]["temp_c"]
            condition=data["current"]["condition"]["text"]

            print(f"Weather in {city}, {country}:")
            print(f"Temperature: {temperature}°C")
            print(f"Condition: {condition}")
            print(f"Last Updated: {data['current']['last_updated']}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def add_favorite(city_name):
    if city_name not in favorite_cities:
        favorite_cities.append(city_name)
        print(f"{city_name} added to favorites.")
    else:
        print(f"{city_name} is already in favorites.")

def remove_favorite(city_name):
    if city_name in favorite_cities:
        favorite_cities.remove(city_name)
        print(f"{city_name} removed from favorites.")
    else:
        print(f"{city_name} is not in favorites.")

def list_favorites():
    print("Favorite Cities:")
    for city in favorite_cities:
        print(city)

def main():
    print("Welcome to the Weather Checking App!")

    while True:
        print("\nMenu:")
        print("1. Check Weather by City")
        print("2. Add City to Favorites")
        print("3. Remove City from Favorites")
        print("4. List Favorite Cities")
        print("5. Exit")
        choice=input("Enter your choice: ")

        if choice=="1":
            city_name=input("Enter the city name: ")
            check_weather(city_name)
        elif choice=="2":
            city_name=input("Enter the city name to add to favorites: ")
            add_favorite(city_name)
        elif choice=="3":
            city_name=input("Enter the city name to remove from favorites: ")
            remove_favorite(city_name)
        elif choice=="4":
            list_favorites()
        elif choice=="5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__=="__main__":
    main()
