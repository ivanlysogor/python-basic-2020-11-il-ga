from pydantic import BaseModel, validator, ValidationError


class Flat(BaseModel):
    """
    A Flat object
    """

    id: int
    name: str
    address: str
    electricity_t1: int
    hot_water: int
    cold_water: int
