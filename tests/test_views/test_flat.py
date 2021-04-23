from pytest import fixture
from flask import url_for
from views.flats import get_default_flats
from app import app


@fixture()
def flats():
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_get_default_flats():
    flats = get_default_flats()
    assert all(map(lambda k: isinstance(k, int), flats))

def test_reset_flats(flats):
    url = url_for("flat_app.reset")
    res = flats.delete(url)
    data = res.json
    assert data == {"ok": True}