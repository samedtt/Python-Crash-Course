from city_functionsv3 import get_city_country_populationv3

def test_city_country_population():
    """Do city country names and population like 'Santiago, Chile - population 5000000' work?"""
    city_country_population=get_city_country_populationv3('santiago','chile',5000000)
    assert city_country_population== 'Santiago, Chile - population 5000000'