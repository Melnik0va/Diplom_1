import pytest 
from praktikum.database import Database
from praktikum.burger import Burger
from unittest.mock import Mock

@pytest.fixture
def bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = 'Просто булка'
    mock_bun.get_price.return_value = 50.0
    return mock_bun

@pytest.fixture
def ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get_type.return_value = 'filling'
    mock_ingredient.get_name.return_value = 'Сыр'
    mock_ingredient.get_price.return_value = 60.0
    return mock_ingredient

@pytest.fixture
def burger(bun):
    burger = Burger()
    burger.set_buns(bun)
    return burger

@pytest.fixture
def database(): 
    database = Database()
    return database
