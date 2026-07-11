import pytest



@pytest.fixture
def card_number_example() -> str:
    """Фикстура, возвращающая тестовый номер карты."""
    return "1234432156788765"


@pytest.fixture
def account_number_example() -> str:
    """Фикстура, возвращающая тестовый номер счета."""
    return "12345543216789009876"

@pytest.fixture()
def input_data() -> list[dict]:
    """Фикстура задающая базовые значения"""
    return  [
            {
                "id": 414288290,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
            },
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-05-30T02:08:58.425572",
            },
            {
                "id": 414288292,
                "state": "EXECUTED",
                "date": "2020-10-03T18:35:29.512364",
            },
            {
                "id": 939719572,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
            },
            {
                "id": 615064591,
                "state": "CANCELED",
                "date": "2018-10-14T08:21:33.419441",
            },
        ]
