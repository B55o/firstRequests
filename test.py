import requests

baseUrl = "https://restcountries.eu/rest/v2/"

do = True
while do:
    print("what info would you like to have :\n")
    choice = int(input("1 Population \n2 Languages \n3 Timezones\n-->"))

    question = input("would you like to get a country list? y/n: \n")

    if question == "y":
        rList = requests.get(baseUrl)
        rListJson = rList.json()
        choiceList = []
        for c in rListJson:
            choiceList.append(c["name"])
        # print(choiceList)
        counter = 0
        firstLetter = input("write first letter:")
        while len(firstLetter) != 1:
            firstLetter = input("write ONLY first letter:")
        else:
            for element in choiceList:
                if element[0] == firstLetter:
                    print(element)

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
            langList.append(lang["name"])
        print(f"native language: {', '.join(langList)}")
    else:
        timezones = countryChoice["timezones"]

        print(f"timezones: ", "\n--> ".join(timezones))
    end = input("want more info? y/n\n")
    if end != "y":
        do = False
        #break
