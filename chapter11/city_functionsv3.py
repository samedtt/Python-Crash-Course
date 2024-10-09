def get_city_country_populationv3(city,country,population=None):
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"