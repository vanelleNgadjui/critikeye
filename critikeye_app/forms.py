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

# Fiche produit


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'email', 'description']

# formulaire de contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nom', 'prenom', 'email',
                  'raison_sociale', 'numero', 'message']


# creation de compte
class EntrepriseForm(UserCreationForm):
    class Meta:
        model = Entreprise
        fields = ['username', 'email', 'raison_sociale',
                  'numero', 'password1', 'password2']


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


class ReponseForm(forms.ModelForm):
    class Meta:
        model = Reponse
        fields = ['reponse_text', 'est_correcte']


class FinalForm(forms.Form):
    # Ajoutez les champs requis pour le formulaire final
    pass
