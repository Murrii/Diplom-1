from praktikum.bun import Bun


class TestBun:
    # Проверяем, что возвращается правильное название булки
    def test_get_name_return_self_name(self):
        bun = Bun(name="Звездный лорд", price=6666.66)
        assert bun.get_name() == "Звездный лорд"

    # Проверяем, что возвращается правильная цена булки
    def test_get_price_return_self_price(self):
        bun = Bun(name="Звездный лорд", price=6666.66)
        assert bun.get_price() == 6666.66
