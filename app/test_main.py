import pytest
import datetime

from unittest import mock

from app.main import outdated_products


@pytest.fixture
def mock_date() -> mock.MagicMock:
    with mock.patch("app.main.datetime.date") as mock_date:
        yield mock_date


@pytest.mark.parametrize("products_input, date_today, products_expected", [
    pytest.param(
        [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 3, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 2, 2),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 2, 1),
                "price": 160
            }
        ],
        datetime.date(2022, 2, 2),
        ["duck"],
        id="should remove product from list if expiration date "
           "less than today and not remove if equal"
    )
])
def test_outdated_products(
        mock_date: mock.MagicMock,
        products_input: list[dict],
        date_today: datetime.date,
        products_expected: list[dict]
) -> None:
    mock_date.today.return_value = date_today
    assert outdated_products(products_input) == products_expected
