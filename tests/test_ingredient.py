import pytest 
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

class TestIngredient: 

    @pytest.mark.parametrize('ingredient_type, name, price', [
        (INGREDIENT_TYPE_FILLING, 'Мясо бессмертных малюсков', 1337),
        (INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90)
    ])
    def test_ingridient_init(self, ingredient_type, name, price): 
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price
        assert ingredient.get_name() == name
        assert ingredient.get_type() == ingredient_type