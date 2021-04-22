from views.flats import get_default_flats

def test_get_default_flats():
    flats = get_default_flats()
    assert all(map(lambda k: isinstance(k, int), flats))