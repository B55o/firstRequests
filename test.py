import requests
import random

baseUrl = "https://restcountries.eu/rest/v2/"
do ="yes"

while do =="yes":
    print("what info would you like to have :\n")
    print("1 Population \n2 Languages \n3 Timezones\n")
    choice = int(input("-->"))
    countryChoice = input("what country you want that information for? \n")
    if choice == 1:
        params = {"fields": "population", "fullText": "true"}
        r= requests.get(baseUrl + f"name/{countryChoice}", params=params)
        print(r.text)
    elif choice == 2:
        params = {"fields": "languages", "fullText": "true"}
        r= requests.get(baseUrl + f"name/{countryChoice}", params=params)
        print(r.text)
    else:
        params = {"fields": "timezones", "fullText": "true"}
        r= requests.get(baseUrl + f"name/{countryChoice}", params=params)
        print(r.text)
    end = input("want more info? y/n\n")
    if end != "y":
        break