from django import forms

from .models import NewsletterSubscriber
from .models import Product
from .models import Contact
from .models import Entreprise, Technophile, Question, Reponse
from django.contrib.auth.forms import UserCreationForm


# Newsletters
class NewsletterSubscriberForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']
        widgets = { 
            'email': forms.EmailInput(attrs={'class': "w-full rounded-xl text-white  ", 'placeholder': 'Votre email'}),
        }
# Fiche produit


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'email', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': "w-full   py-2 px-4 rounded-xl text-white", 'placeholder': 'Votre nom'}),
            'email': forms.EmailInput(attrs={'class': "w-full rounded-xl text-white  ", 'placeholder': 'Votre email'}),
            'description': forms.Textarea(attrs={'class': "w-full h-full rounded-xl text-white  ", 'placeholder': 'Description de votre produit'}),
        }
# formulaire de contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nom', 'email',
                  'raison_sociale', 'numero', 'message']
        widgets = {
            'nom': forms.TextInput(attrs={'class': "w-full   py-2 px-4 rounded-xl text-white", 'placeholder': 'Nom et prenom'}),
            'email': forms.EmailInput(attrs={'class': "w-full rounded-xl text-white  ", 'placeholder': 'Email'}),
            'raison_sociale': forms.TextInput(attrs={'class': "w-full h-full rounded-xl text-white  ", 'placeholder': 'raison sociale'}),
            'numero': forms.NumberInput(attrs={'class': "w-full h-full rounded-xl text-white  ", 'placeholder': 'numéro de téléphone'}),
            'message': forms.Textarea(attrs={'class': "w-full h-full rounded-xl text-white  ", 'placeholder': 'Message'}),
        }

# creation de compte


class EntrepriseForm(UserCreationForm):
    class Meta:
        model = Entreprise
        fields = ['username', 'email', 'raison_sociale',
                  'numero', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': "w-full   py-2 px-4 rounded-xl text-white", 'placeholder': 'Nom d\'utilisateur'}),
            'email': forms.EmailInput(attrs={'class': "w-full py-2 px-4 rounded-xl text-white  ", 'placeholder': 'Email'}),
            'raison_sociale': forms.TextInput(attrs={'class': "w-full h-full rounded-xl text-white  ", 'placeholder': 'raison sociale'}),
            'numero': forms.NumberInput(attrs={'class': "w-full h-full rounded-xl text-white  ", 'placeholder': 'numéro de téléphone'}),
            'password1': forms.PasswordInput(attrs={'class': "w-full h-full rounded-xl text-white  ", 'placeholder': '**********'}),
            'password2': forms.PasswordInput(attrs={'class': "w-full h-full rounded-xl text-white  ", 'placeholder': '*********'}),
        }

class TechnophileForm(UserCreationForm):
    class Meta:
        model = Technophile
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': "w-full   py-2 px-4 rounded-xl text-white", 'placeholder': 'Nom d\'utilisateur'}),
            'email': forms.EmailInput(attrs={'class': "w-full py-2 px-4 rounded-xl text-white  ", 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': "w-full h-full rounded-xl text-white  ", 'placeholder': '**********'}),
            'password2': forms.PasswordInput(attrs={'class': "w-full h-full rounded-xl text-white  ", 'placeholder': '*********'}),
        }

#  QCM


class QuestionnaireForm(forms.Form):
    def __init__(self, questions, *args, **kwargs):
        super(QuestionnaireForm, self).__init__(*args, **kwargs)

        for question in questions:
            reponses = question.reponse_set.all()
            choices = [(reponse.id, reponse.reponse_text)
                       for reponse in reponses]
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                label=question.question_text,
                choices=choices,
                widget=forms.RadioSelect
            )




class CookiePreferencesForm(forms.Form):
    cookie_consent = forms.BooleanField(label='Accepter les cookies', required=False)
    third_party_cookies = forms.BooleanField(label='Cookies tiers', required=False)
    analytics_cookies = forms.BooleanField(label='Cookies d\'analyse', required=False)
    refuse_cookies = forms.BooleanField(label='Refuser les cookies', required=False)