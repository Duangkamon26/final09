def motorcycle_serializer(motorcycle) -> dict:
    return {
        "id": str(motorcycle["_id"]),
        "motorcycle_code": motorcycle["motorcycle_code"],
        "motorcycle_name": motorcycle["motorcycle_name"],
        "motorcycle_price": motorcycle["motorcycle_price"],
        "down_payment": motorcycle["down_payment"],
    }

def motorcycles_serializers(motorcycles) -> list:
    return [motorcycle_serializer(motorcycle) for motorcycle in motorcycles]