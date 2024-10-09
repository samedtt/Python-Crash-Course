from city_functions import get_city_country

def test_city_country():    
    """Do city, country names like 'Santiago, Chile' work?"""
    city_country=get_city_country('santiago','chile')
    assert city_country=='Santiago, Chile'

