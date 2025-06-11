import pytest
from unittest.mock import Mock
import random
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE as SAUSE
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING as FILLING

@pytest.fixture
def bun_mock():
    bun_mock = Mock()
    bun_mock.name = "Булка"
    bun_mock.price = 150.50
    bun_mock.get_price.return_value = 150.50
    return bun_mock

@pytest.fixture
def ingredient_mock():
    ingredient_mock = Mock()
    ingredient_mock.name = "Огурчик 'Сила земли'"
    ingredient_mock.price = 50.50
    ingredient_mock.type = random.choice([SAUSE, FILLING])
    ingredient_mock.get_price.return_value = 50.50
    return ingredient_mock

# второй ингредиент для проверки формирования цены бургера
@pytest.fixture
def second_ingredient_mock():
    second_ingredient_mock = Mock()
    second_ingredient_mock.name = "Соус 'Кровь дракона'"
    second_ingredient_mock.price = 24.50
    second_ingredient_mock.type = random.choice([SAUSE, FILLING])
    second_ingredient_mock.get_price.return_value = 24.50
    return second_ingredient_mock
