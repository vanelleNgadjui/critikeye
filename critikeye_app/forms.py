from django import forms

from .models import NewsletterSubscriber
from .models import Product
from .models import Contact
from .models import Entreprise, Technophile


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
        fields = ['nom', 'prenom', 'email', 'raison_sociale', 'numero', 'message']


#  QCM
class QuestionnaireForm(forms.Form):
    def __init__(self, questions, *args, **kwargs):
        super(QuestionnaireForm, self).__init__(*args, **kwargs)
        
        for question in questions:
            reponses = question.reponse_set.all()
            choices = [(reponse.id, reponse.reponse_text) for reponse in reponses]
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                label=question.question_text,
                choices=choices,
                widget=forms.RadioSelect
            )



# creation de compte
class EntrepriseForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Entreprise
        fields = ['username', 'email', 'raison_sociale', 'numero', 'password']

class TechnophileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Technophile
        fields = ['username', 'email', 'password']
