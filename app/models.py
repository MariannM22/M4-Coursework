from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    is_favorite = models.BooleanField()
    
def create_contact(name, email,phone, is_favorite):
    group = Contacts(name=name, email=email, phone=phone, is_favorite=is_favorite)
    group.save()
    return group
    
def all_contacts():
    return Contacts.objects.all()

def find_contact_by_name(name):
    try:
        return Contacts.objects.get(name=name)
    except Contacts.DoesNotExist:
        None

def favorite_contacts():
    return Contacts.objects .filter(is_favorite=True)

def update_contact_email(name, new_email):
    contact = Contacts.objects.get(name=name)
    contact.email = new_email
    contact.save()

def delete_contact(name):
    new = find_contact_by_name(name)
    new.delete()