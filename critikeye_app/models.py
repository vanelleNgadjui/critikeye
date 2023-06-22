from django.contrib.auth.models import Group, Permission
from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
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
    prenom = models.CharField(max_length=100)
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
    est_selectionnee = models.BooleanField(default=False)


# code de la cration de compte
class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='critikeye_users'  # Add a related_name argument
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='critikeye_users'  # Add a related_name argument
    )

class Entreprise(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    # Other fields for the Entreprise model
    numero = models.CharField(max_length=50)
    raison_sociale = models.CharField(max_length=100)
    groups = models.ManyToManyField(Group, related_name='enterprise_users')
    user_permissions = models.ManyToManyField(Permission, related_name='enterprise_users')

class Technophile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    technophile_name = models.CharField(max_length=100)
    groups = models.ManyToManyField(Group, related_name='technophile_users')
    user_permissions = models.ManyToManyField(Permission, related_name='technophile_users')