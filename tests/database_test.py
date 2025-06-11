from praktikum.database import Database


class TestDatabase:
    # Проверяем, что метод available_buns возвращает все булки из базы
    def test_available_buns_return_all_added_buns(self):
        database = Database()
        # собираем в список имена всех булочек, которые возвращает метод available_buns
        list_of_bun_names_in_database = [bun.name for bun in database.available_buns()]
        # проверяем, что вернулись все булочки
        assert list_of_bun_names_in_database == ["black bun", "white bun", "red bun"]

    # Проверяем, что метод available_ingredients возвращает все ингредиенты из базы
    def test_available_ingredients_return_all_added_ingredients(self):
        database = Database()
        # собираем в список имена всех ингредиентов, которые возвращает метод available_ingredients
        list_of_ingredient_names_in_database = [ingredient.name for ingredient in database.available_ingredients()]
        # проверяем, что вернулись все ингредиенты
        assert list_of_ingredient_names_in_database == ["hot sauce", "sour cream", "chili sauce",
                                                        "cutlet", "dinosaur", "sausage"]