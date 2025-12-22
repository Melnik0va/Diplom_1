import pytest 

from praktikum.bun import Bun 

class TestBun: 

    @pytest.mark.parametrize('name, price', [('Белая', 50), ('Черная', 100), ('Зеленая', 150) ])
    def test_class_Bun(self, name, price): 
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price
