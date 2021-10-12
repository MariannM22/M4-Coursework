from django.db import models

# Create your models here.
class Foods(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    servings = models.IntegerField()
    is_favorite = models.BooleanField()
    
def create_food(name, price,servings, is_favorite):
    group = Foods(name=name, price=price, servings=servings, is_favorite=is_favorite)
    group.save()
    return group
    
def all_foods():
    return Foods.objects.all()

def find_food_by_name(name):
    try:
        return Foods.objects.get(name=name)
    except Foods.DoesNotExist:
        None

def favorite_foods():
    return Foods.objects .filter(is_favorite=True)

def update_food_price(name, new_price):
    food = Foods.objects.get(name=name)
    food.price = new_price
    food.save()

def delete_food(name):
    new = find_food_by_name(name)
    new.delete()