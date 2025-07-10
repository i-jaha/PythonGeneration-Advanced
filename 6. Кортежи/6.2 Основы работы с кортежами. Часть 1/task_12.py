"""
Дополните приведенный ниже код так,
чтобы переменная number
содержала количество вхождений 'Spain' в кортеж countries.
"""

# example
countries = (
    "Russia",
    "Argentina",
    "Spain",
    "Slovakia",
    "Canada",
    "Slovenia",
    "Italy",
    "Spain",
    "Ukraine",
    "Chile",
    "Spain",
    "Cameroon",
)
number = ...
print(number)

# review
countries = (
    "Russia",
    "Argentina",
    "Spain",
    "Slovakia",
    "Canada",
    "Slovenia",
    "Italy",
    "Spain",
    "Ukraine",
    "Chile",
    "Spain",
    "Cameroon",
)
number = countries.count("Spain")
print(number)