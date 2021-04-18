import requests

baseUrl = "https://restcountries.eu/rest/v2/"

do = "yes"
while do == "yes":
    print("what info would you like to have :\n")
    print("1 Population \n2 Languages \n3 Timezones\n")
    choice = int(input("-->"))

    question = input("would you like to get a country list? y/n: \n")
    if question == "y":
        firstLetter = input("write first letter:")
        rList = requests.get(baseUrl)
        jsonChoice = rList.json()
        choiceList = []
        counter = 0
        for c in jsonChoice:
            choiceList.append(c["name"])
        for country in choiceList:
            if country[0] == firstLetter:
                print(country)
    countryChoice = input("what country you want that information for? \n")

    params = {"fields": "population;languages;timezones", "fullText": "true"}
    r = requests.get(baseUrl + f"name/{countryChoice}", params=params)
    json_response = r.json()
    #print(json_response)
    countryChoice = json_response[0]

    if choice == 1:
        population = countryChoice['population']
        print(f'population is {population}')
    elif choice == 2:
        langList = []
        for lang in countryChoice["languages"]:
            langList.append(lang["nativeName"])
        print(f"native language: {''.join(langList)}")
    else:
        timezones = countryChoice["timezones"]

        print(f"timezones: {timezones}")
    end = input("want more info? y/n\n")
    if end != "y":
        break
