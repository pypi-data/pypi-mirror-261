import unittest
from datetime import date

from flysearch.trip import Trip


class TestFlightOffer(unittest.TestCase):
    def test_from_dict(self):
        test_data = {
            "Klucz": "AYT",
            "TerminWyjazdu": "2024-05-01T00:00:00Z",
            "Cena": 1000,
            "DataLayerV4": {"currency": "PLN", "item_category3": "bgz"},
        }
        expected_result = Trip(
            departure_iata="BGZ",
            arrival_iata="AYT",
            departure_date=date(2024, 5, 1),
            price=1000,
            currency="PLN",
        )
        result = Trip.from_dict(data_dict=test_data)
        self.assertEqual(result, expected_result)
