from django.test import TestCase
from app import models
class TestFoods(TestCase):
    def test_can_create_food(self):
        food = models.create_food(
            "Tacos",
            15,
            5,
            True,
        )
        self.assertEqual(food.servings, 5)
        self.assertEqual(food.name, "Tacos")
        self.assertEqual(food.price, 15)
        self.assertTrue(food.is_favorite)
    def test_can_view_all_foods_at_once(self):
        foods_data = [
            {
                "name": "Steak and Potatoes",
                "price": 50,
                "servings": 2,
                "is_favorite": True,
            },
            {
                "name": "Veggie Burgers",
                "price": 30,
                "servings": 4,
                "is_favorite": False,
            },
            {
                "name": "Chocolate Cake",
                "price": 8,
                "servings": 8,
                "is_favorite": True,
            },
        ]
        for food_data in foods_data:
            models.create_food(
                food_data["name"],
                food_data["price"],
                food_data["servings"],
                food_data["is_favorite"],
            )
        foods = models.all_foods()
        self.assertEqual(len(foods), len(foods_data))
        foods_data = sorted(foods_data, key=lambda c: c["name"])
        foods = sorted(foods, key=lambda c: c.name)
        for data, food in zip(foods_data, foods):
            self.assertEqual(data["name"], food.name)
            self.assertEqual(data["price"], food.price)
            self.assertEqual(data["servings"], food.servings)
            self.assertEqual(data["is_favorite"], food.is_favorite)
    def test_can_search_by_name(self):
        foods_data = [
            {
                "name": "Steak and Potatoes",
                "price": 50,
                "servings": 2,
                "is_favorite": True,
            },
            {
                "name": "Veggie Burgers",
                "price": 30,
                "servings": 4,
                "is_favorite": False,
            },
            {
                "name": "Chocolate Cake",
                "price": 8,
                "servings": 8,
                "is_favorite": True,
            },
        ]
        for food_data in foods_data:
            models.create_food(
                food_data["name"],
                food_data["price"],
                food_data["servings"],
                food_data["is_favorite"],
            )
        self.assertIsNone(models.find_food_by_name("aousnth"))
        food = models.find_food_by_name("Chocolate Cake")
        self.assertIsNotNone(food)
        self.assertEqual(food.price, 8)
    def test_can_view_favorites(self):
        foods_data = [
            {
                "name": "Steak and Potatoes",
                "price": 50,
                "servings": 2,
                "is_favorite": True,
            },
            {
                "name": "Veggie Burgers",
                "price": 30,
                "servings": 4,
                "is_favorite": False,
            },
            {
                "name": "Chocolate Cake",
                "price": 8,
                "servings": 8,
                "is_favorite": True,
            },
        ]
        for food_data in foods_data:
            models.create_food(
                food_data["name"],
                food_data["price"],
                food_data["servings"],
                food_data["is_favorite"],
            )
        self.assertEqual(len(models.favorite_foods()), 2)
    def test_can_update_foods_price(self):
        foods_data = [
            {
                "name": "Steak and Potatoes",
                "price": 50,
                "servings": 2,
                "is_favorite": True,
            },
            {
                "name": "Veggie Burgers",
                "price": 30,
                "servings": 4,
                "is_favorite": False,
            },
            {
                "name": "Chocolate Cake",
                "price": 8,
                "servings": 8,
                "is_favorite": True,
            },
        ]
        for food_data in foods_data:
            models.create_food(
                food_data["name"],
                food_data["price"],
                food_data["servings"],
                food_data["is_favorite"],
            )
        models.update_food_price("Steak and Potatoes", 60)
        self.assertEqual(
            models.find_food_by_name("Steak and Potatoes").price, 60
        )
    def test_can_delete_food(self):
        foods_data = [
            {
                "name": "Steak and Potatoes",
                "price": 50,
                "servings": 2,
                "is_favorite": True,
            },
            {
                "name": "Veggie Burgers",
                "price": 30,
                "servings": 4,
                "is_favorite": False,
            },
            {
                "name": "Chocolate Cake",
                "price": 8,
                "servings": 8,
                "is_favorite": True,
            },
        ]
        for food_data in foods_data:
            models.create_food(
                food_data["name"],
                food_data["price"],
                food_data["servings"],
                food_data["is_favorite"],
            )
        models.delete_food("Veggie Burgers")
        self.assertEqual(len(models.all_foods()), 2)
