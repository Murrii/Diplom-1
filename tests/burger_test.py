from praktikum.burger import Burger


class TestBurger:
    # Проверяем, что можно выбрать булку для бургера
    # Изолируем тест и вместо Bun добавляем мок из фикстуры bun_mock
    def test_set_buns_add_bun_in_self_buns(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        assert burger.bun.name == bun_mock.name

    # Проверяем, что можно выбрать ингредиент для бургера
    # Изолируем тест и вместо Ingredient добавляем мок из фикстуры ingredient_mock
    def test_add_ingredient_added_ingredients_in_list(self, ingredient_mock):
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        # Проверяем, что в список добавлен один ингредиент и его название совпадает с названием в моке
        assert burger.ingredients[0].name == ingredient_mock.name and len(burger.ingredients) == 1

    # Проверяем, что можно удалить добавленный ингредиент
    # Изолируем тест и вместо Ingredient добавляем мок из фикстуры ingredient_mock
    def test_remove_ingredient_added_ingredient_remove_from_list(self, ingredient_mock):
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        burger.remove_ingredient(0)
        # Проверяем, что единственный добавленный ингредиент удален
        assert len(burger.ingredients) == 0

    # Проверяем, что ингредиент перемещается на выбранное место и общая длина списка не меняется
    def test_move_ingredient_move_chosen_ingredient_on_right_slot(self, ingredient_mock, second_ingredient_mock):
        burger = Burger()
        burger.add_ingredient(ingredient_mock) # [1_ing]
        burger.add_ingredient(second_ingredient_mock) # [1_ing, 2_ing]
        burger.move_ingredient(1, 0) # [2_ing, 1_ing]
        assert burger.ingredients[0].get_name() == second_ingredient_mock.name and len(burger.ingredients) == 2

    # Проверяем подсчет цены
    # Для ингредиентов и булок используем моки
    def test_get_price_return_summ_prices_of_two_buns_and_all_ingredients(self, bun_mock,
                                                                          ingredient_mock, second_ingredient_mock):
        burger = Burger()
        burger.set_buns(bun_mock) # цена 150,50
        burger.add_ingredient(ingredient_mock) # цена 50,50
        burger.add_ingredient(second_ingredient_mock) # цена 24,50
        final_price = burger.get_price() # 150.50 * 2 + 50,50 + 24,50 =376,00
        assert final_price == 376,50

    # Проверяем, что в рецепте присутствуют все выбранные ингредиенты
    def test_get_receipt_print_all_added_ingredients(self, bun_mock, ingredient_mock, second_ingredient_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        burger.add_ingredient(second_ingredient_mock)
        receipt = burger.get_receipt()
        assert bun_mock.name in receipt and ingredient_mock.name in receipt and second_ingredient_mock.name in receipt
