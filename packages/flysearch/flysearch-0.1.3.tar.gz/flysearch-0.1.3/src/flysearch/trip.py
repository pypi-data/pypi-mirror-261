from dataclasses import dataclass
from datetime import date, datetime
from typing import Dict, Union


@dataclass
class Trip:
    departure_iata: str
    arrival_iata: str
    departure_date: date
    price: float
    currency: str

    @staticmethod
    def from_dict(data_dict: Dict[str, Union[str, Dict[str, str]]]) -> "Trip":
        data_layer = data_dict.get("DataLayerV4", {})
        departure_iata = data_layer.get('item_category3').upper()
        currency = data_layer.get("currency", "PLN").upper()
        departure_date = datetime.strptime(
            data_dict.get("TerminWyjazdu"), "%Y-%m-%dT%H:%M:%SZ"
        ).date()
        return Trip(
            departure_iata=departure_iata,
            arrival_iata=data_dict.get("Klucz"),
            departure_date=departure_date,
            price=data_dict.get("Cena"),
            currency=currency,
        )
