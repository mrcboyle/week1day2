united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.
united_kingdom["name"]["capital"] = "Cardiff"
print(united_kingdom["Erik"]["home_town"])

# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000)
# create a dictionary with new country details
norn_irn={"name": "Northern Ireland",
         "population": 1811000,
         "capital": "Belfast"
}
#append the new country dictionary to the original list
united_kingdom.append(norn_irn)
print(united_kingdom)

# 3. Use a loop to print the names of all the countries in the UK.
for names in united_kingdom.values():
  print(names)


# 4. Use a loop to find the total population of the UK.

