from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
from data import ingredient_info

class TestIngredient:

    def test_ingridient_init_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, ingredient_info['name'], ingredient_info['price'])
        assert ingredient.get_price() == ingredient_info['price']

    def test_ingridient_init_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, ingredient_info['name'], ingredient_info['price'])
        assert ingredient.get_name() == ingredient_info['name']

    def test_ingridient_init_get_ingredient_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, ingredient_info['name'], ingredient_info['price'])
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE