from django.contrib.auth.models import Group, Permission
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils.translation import gettext_lazy as _

#  Newsletter


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)


# Fiche produit
class Product(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()


# Formualaire de contact
class Contact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    raison_sociale = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    message = models.TextField()


# code du qcm:
class Question(models.Model):
    question_text = models.CharField(max_length=200)


class Reponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    reponse_text = models.CharField(max_length=200)
    est_correcte = models.BooleanField(default=False)


# code de la cration de comptefrom django.contrib.auth.models import AbstractUser
class Entreprise(AbstractUser):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)  # Champ username ajouté
    password = models.CharField(max_length=128, default='default_password')
    USERNAME_FIELD = 'email'
    numero = models.CharField(max_length=50)
    raison_sociale = models.CharField(max_length=100)
    # Autres champs pour le modèle Entreprise
    groups = models.ManyToManyField(Group, related_name='entreprise_users')
    user_permissions = models.ManyToManyField(
        Permission, related_name='entreprise_users')

    def __str__(self):
        return self.username


class Technophile(AbstractUser):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)  # Champ username ajouté
    # password = models.CharField(max_length=128, default='default_password')

    USERNAME_FIELD = 'email'

    # Other fields for the Technophile model
    groups = models.ManyToManyField(Group, related_name='technophile_users')
    user_permissions = models.ManyToManyField(Permission, related_name='technophile_users')

    def __str__(self):
        return self.username

