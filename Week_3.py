petShop = {
    "animals": {
        "dogs": {"Labrador": 3, "Beagle": 2, "Poodle": 1, "Mastiff": 5},
        "cats": {"Persian": 2, "Siamese": 1, "Maine Coon": 2},
        "fish": {"Goldfish": 12, "Angelfish": 5, "Betta": 3},
        "birds": {"Parakeet": 4, "Canary": 3, "Cockatiel": 7}
    },
    "supplies": {
        "food": {"Dog Food": 20, "Cat Food": 9, "Fish Food": 25},
        "toys": {"Dog Toys": 30, "Cat Toys": 20},
        "habitats": {"Aquariums": 5, "Cat Trees": 8, "Dog Beds": 7}
    },
}
# item_type = ""
# item_type2 = ""
# item_type3 = ""

# while item_type != "animals" and item_type != "supplies":
#     item_type = input("What would you like to buy? [animals/supplies]: ").strip().lower()

# if item_type == "animals":
#     item_type2 = input(f"Which of the {item_type} do you want to buy? (dogs/cats/fish/birds)")
#     item_type3 = input(f"What kind of {item_type2} would you like to buy?: ")
# else:
#     item_type2 = input(f"Which of the {item_type} do you want to buy? (food/toys/habitats)")
#     item_type3 = input(f"What kind of {item_type2} would you like to buy?: ")

# petShop[item_type][item_type2][item_type3] -= 1
# print(petShop)
low_in_stock = []


for items in petShop["animals"]:
    for item in petShop["animals"][items]:
        if petShop["animals"][items][item] < 10:
            low_in_stock.append(item)

for items in petShop["supplies"]:
    for item in petShop["supplies"][items]:
        if petShop["supplies"][items][item] < 10:
            low_in_stock.append(item)

print(low_in_stock)

print("")

# most_variety_by_breeds = ""
# most_breeds = 0
# most_variety_by_headcount = ""
# most_headcount = 0

# for items in petShop["animals"]:
#     if items > most_headcount:
#         most_headcount = items
#         most_variety_by_headcount = items.keys()
    

covid = {
    "countries": {
        "Nigeria": {
            "population": 5000000,
            "total_cases": 250000,
            "active_cases": 16500,
            "deaths": 3500,
            "recoveries": 230000,
            "testing": 1200000,
            "vaccination": {
                "first_dose": 3500000,
                "fully_vaccinated": 3200000,
                "boosters": 1800000
            },
            "monthly_cases": {
                "Jan": 45000,
                "Feb": 32000,
                "Mar": 25000,
                "Apr": 18000,
                "May": 15000,
                "Jun": 10000
            }
        },
        "Ghana": {
            "population": 8000000,
            "total_cases": 420000,
            "active_cases": 23800,
            "deaths": 6200,
            "recoveries": 390000,
            "testing": 1900000,
            "vaccination": {
                "first_dose": 5100000,
                "fully_vaccinated": 4800000,
                "boosters": 2500000
            },
            "monthly_cases": {
                "Jan": 80000,
                "Feb": 65000,
                "Mar": 40000,
                "Apr": 25000,
                "May": 12000,
                "Jun": 8000
            }
        },
        "England": {
            "population": 3000000,
            "total_cases": 180000,
            "active_cases": 5900,
            "deaths": 2100,
            "recoveries": 172000,
            "testing": 950000,
            "vaccination": {
                "first_dose": 2100000,
                "fully_vaccinated": 1950000,
                "boosters": 900000
            },
            "monthly_cases": {
                "Jan": 35000,
                "Feb": 30000,
                "Mar": 20000,
                "Apr": 12000,
                "May": 8000,
                "Jun": 5000
            }
        },
        "Kenya": {
            "population": 6500000,
            "total_cases": 350000,
            "active_cases": 15200,
            "deaths": 4800,
            "recoveries": 330000,
            "testing": 1600000,
            "vaccination": {
                "first_dose": 3900000,
                "fully_vaccinated": 3500000,
                "boosters": 1600000
            },
            "monthly_cases": {
                "Jan": 70000,
                "Feb": 50000,
                "Mar": 35000,
                "Apr": 20000,
                "May": 10000,
                "Jun": 5000
            }
        }
    },
    "global": {
        "total_cases": 1200000,
        "active_cases": 61400,
        "total_deaths": 16600,
        "total_recoveries": 1122000,
        "total_vaccines_distributed": 25000000
    },
    "variants": {
        "Alpha": {"first_detected": "Sep 2020", "transmissibility": "Medium"},
        "Beta": {"first_detected": "Oct 2020", "transmissibility": "Medium"},
        "Delta": {"first_detected": "Dec 2020", "transmissibility": "High"},
        "Omicron": {"first_detected": "Nov 2021", "transmissibility": "Very High"}
    }
}
highest_active_cases = 0
highest_recovery_rate = 0
lots_of_cases = {}
total_active_cases = 0
country_percentages = {}

for country in covid["countries"]:
    if covid["countries"][country]["active_cases"] > highest_active_cases:
        most_cases_country = country
        highest_active_cases = covid["countries"][country]["active_cases"]

for country in covid["countries"]:
    print(f"The ratio of active cases to poulation for {country} is {covid["countries"][country]["active_cases"]}:{covid["countries"][country]["population"]}")

print("")

for country in covid["countries"]:
    recovery_rate = covid["countries"][country]["recoveries"] / covid["countries"][country]["total_cases"]
    if recovery_rate > highest_recovery_rate:
        highest_active_cases = recovery_rate
        best_recovery_rate_country = country

print(f"The country with the highest recovery rate is {best_recovery_rate_country} with a recovery rate of {highest_active_cases:.2f}")

print("-----------------ACTIVE CASES AS A PERCENTAGE OF POPULATION FOR EACH COUNTRY-----------------")

for country in covid["countries"]:
    print(f"{country} : {(covid["countries"][country]["active_cases"] / covid["countries"][country]["population"]) * 100:.2f}%")

for country in covid["countries"]:
    if covid["countries"][country]["active_cases"] > 20000:
        lots_of_cases[country] = covid["countries"][country]["active_cases"]

print(lots_of_cases)
print("")

for country in covid["countries"]:
    total_active_cases += covid["countries"][country]["active_cases"]

print(f"Total active cases: {total_active_cases}")

for country in covid["countries"]:
    covid["countries"][country]["cases_per_million"] = covid["countries"][country]["total_cases"] / 1000000
    print(covid["countries"])

print("")

active_cases = int(input("Input the new amount of active cases in Nigeria: "))
covid["countries"]["Nigeria"]["active_cases"] = active_cases

for country in covid["countries"]:
    country_percentage = (covid["countries"][country]["active_cases"] / covid["global"]["active_cases"] * 100)
    country_percentages[country] = country_percentage

print(country_percentages)
