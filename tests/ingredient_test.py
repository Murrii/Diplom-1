import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE as SAUCE
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING as FILLING
import random


class TestIngredient:
    # Проверяем, что возвращается правильный тип ингредиента для обоих ингредиентов
    @pytest.mark.parametrize("ing_type", [SAUCE, FILLING])
    def test_get_type_return_self_type(self, ing_type):
        ingredient = Ingredient(name="Булка", price=150.50, ingredient_type=ing_type)
        assert ingredient.get_type() == ing_type

    # Проверяем, что возвращается правильное название ингредиента
    def test_get_name_return_self_name(self):
        ingredient = Ingredient(name="Булка", price=150.50, ingredient_type=random.choice([SAUCE, FILLING]))
        assert ingredient.get_name() == "Булка"

    # Проверяем, что возвращается правильная цена ингредиента
    def test_get_price_return_self_price(self):
        ingredient = Ingredient(name="Булка", price=150.50, ingredient_type=random.choice([SAUCE, FILLING]))
        assert ingredient.get_price() == 150.50