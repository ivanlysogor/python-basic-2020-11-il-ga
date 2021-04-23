from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.exceptions import NotFound
from flat import Flat


flat_app = Blueprint("flat_app", __name__)

def get_default_flats():
    return {
        0: Flat(id=0, name="First",
                address="Moscow",
                electricity_t1=10,
                hot_water=10,
                cold_water=10),
        1: Flat(id=0, name="Second",
                address="SPB",
                electricity_t1=20,
                hot_water=20,
                cold_water=20)
    }

FLATS = get_default_flats()

next_index = iter(range(len(FLATS), 100))

@flat_app.route("/", endpoint="list")
def flats_list():
    return render_template("flats/index.html", flats=FLATS.values())

@flat_app.route("/<int:flat_id>/", methods=["GET", "POST"], endpoint="details")
def flat_details(flat_id):
    if flat_id not in FLATS:
        raise NotFound(f"A flat with id {flat_id} doesn't exist!")
    if request.method == "GET":
        return render_template(
            "flats/details.html",
            flat=FLATS[flat_id]
        )
    FLATS[flat_id].name = request.form.get("flat_name")
    FLATS[flat_id].address = request.form.get("flat_address")
    FLATS[flat_id].electricity_t1 = request.form.get("electricity_t1")
    FLATS[flat_id].hot_water = request.form.get("hot_water")
    FLATS[flat_id].cold_water = request.form.get("cold_water")
    return redirect(url_for("flat_app.list"))


@flat_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def flat_add():
    if request.method == "GET":
        return render_template("flats/add.html")
    next_id = next(next_index)
    new_flat = Flat(id=next_id,
                    name=request.form.get("flat_name"),
                    address=request.form.get("flat_address"),
                    electricity_t1=request.form.get("electricity_t1"),
                    hot_water=request.form.get("hot_water"),
                    cold_water=request.form.get("cold_water"))
    FLATS[next_id] = new_flat
    return redirect(url_for("flat_app.list"))

@flat_app.route("/reset/",  methods=["DELETE"], endpoint="reset")
def flats_reset():
    FLATS.clear()
    FLATS.update(get_default_flats())
    return {"ok": True}
