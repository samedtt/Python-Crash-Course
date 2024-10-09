from name_function11v3 import get_formatted_namev3

def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
    formatted_name=get_formatted_namev3('janis','joplin')
    assert formatted_name=='Janis Joplin'

def test_first_last_middle_name():
    """Do names like 'Wolfgang Amadues Mozar' work?"""
    formatted_name=get_formatted_namev3('wolfgang','mozart','amadeus')
    assert formatted_name=='Wolfgang Amadeus Mozart'
    