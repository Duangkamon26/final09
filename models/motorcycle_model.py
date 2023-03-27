from pydantic import BaseModel

class Motorcycle(BaseModel):
    motorcycle_code: str
    motorcycle_name: str
    motorcycle_price : str
    down_payment : int