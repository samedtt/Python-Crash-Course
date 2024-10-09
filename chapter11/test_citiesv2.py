from city_functionsv2 import get_city_countryv2

def test_city_countryv2():    
    """Do city, country names like 'Santiago, Chile' work?"""
    city_country=get_city_countryv2('santiago','chile')
    assert city_country=='Santiago, Chile'
