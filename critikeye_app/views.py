from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseBadRequest
from django.http import HttpResponse
import requests
import json
import openai
import requests
import base64

from .forms import NewsletterSubscriberForm, ProductForm, ContactForm, QuestionnaireForm, TechnophileForm, EntrepriseForm
from .forms import ReponseForm, FinalForm

from .models import Product, Question, Reponse, Technophile, Entreprise

from django.forms.models import modelformset_factory
from django.contrib.auth.models import User


from googletrans import Translator

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



# Le décorateur @csrf_protect est nécessaire pour protéger votre formulaire contre les attaques CSRF (Cross-Site Request Forgery).
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required







# Pages
def about(request):
    return render(request, 'about.html')
def technophilesHome(request):
    return render(request, 'technophilesHome.html')
def entreprises(request):
    return render(request, 'entreprises.html')
def fiche_produit(request):
    return render(request, 'fiche_produit.html')

# Newsletters
def index (request):
    if request.method == 'POST':
        form = NewsletterSubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            # Faites ici les actions nécessaires après l'inscription à la newsletter
            return render(request, 'index.html')
    else:
        form = NewsletterSubscriberForm()
    
    context = {'newsletter_form': form}
    return render(request, 'index.html', context)


# Fiche produit
@csrf_protect
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            # Faites ici les actions nécessaires après la création de la fiche produit
            prompt = form.cleaned_data['description']

            image_generee = appeler_api_dalle(prompt)

            context = {
                'form': form,
                'image_generee': image_generee,
            }

            # Page qui signale a l'utilisateur que nous lui avons envoyé la fiche produit par mail
            # return render(request, 'product_success.html', context)
        else:
            # Le formulaire n'est pas valide, renvoyer une réponse BadRequest avec les erreurs du formulaire
            context = {'product_form': form}
            return HttpResponseBadRequest(render(request, 'fiche_produit.html', context))
    else:
        form = ProductForm()
    
    context = {'product_form': form}
    return render(request, 'fiche_produit.html', context)



def appeler_api_dalle(prompt):
    # Convertir les données du formulaire en format adapté pour l'API DALL·E
    description_produit = prompt
    translator = Translator(service_urls=["translate.google.com"])
    translated_description_produit = translator.translate(description_produit, src="fr", dest="en").text

    # openai.api_key = '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'
    # response = openai.Image.create(
    #     prompt=prompt,
    #     n=2,
    #     size="256x256"
    # )

    prompt = translated_description_produit

    url = "https://stablediffusionapi.com/api/v3/text2img"

    payload = json.dumps({
        "key": "pLn3rhOpWRe9XaB0MYiS0BnVe3wttdbqvtcSdb1AFibpDqSmM0kdWkMpiKS4",
        "prompt": prompt,
        "negative_prompt": None,
        "width": "512",
        "height": "512",
        "samples": "1",
        "num_inference_steps": "20",
        "seed": None,
        "guidance_scale": 7.5,
        "safety_checker": "no",
        "multi_lingual": "no",
        "panorama": "no",
        "self_attention": "no",
        "upscale": "no",
        "embeddings_model": "embeddings_model_id",
        "webhook": None,
        "track_id": None,
        "enhance_prompt": "no"
    })

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, data=payload)
    data = response.json()

    if response.status_code == 200 and data["status"] == "success":
        image_url = data["output"][0]

        # Télécharger l'image à partir de l'URL
        response = requests.get(image_url)
        if response.status_code == 200:
            image_content = response.content
            image_base64 = base64.b64encode(image_content).decode("utf-8")

            send_emails(image_content)  # Modifier pour envoyer l'image binaire au lieu de l'image encodée en base64

            # Stocker l'image dans une variable de session
            # request.session['generated_image'] = image_base64

            # Afficher l'image dans le template en utilisant la variable de session
        else:
            print("Échec du téléchargement de l'image")
    else:
        print("Échec de la génération de l'image")

    return image_base64




def send_emails(image_generee):
    users = Product.objects.all()
    for user in users:
        subject = "De l'idée à l'image !"
        message = "Salut {0} !\n\nNous avons remarqué que vous avez visité notre site récemment et renseigné la description de votre produit de rêve. Nous sommes ravis de vous annoncer que nous avons pris l'initiative de le réaliser pour vous.\n\n"
        message += "Notre équipe talentueuse a travaillé avec soin pour créer une représentation visuelle de votre idée, et nous sommes impatients de vous la présenter.\n\n"
        message += "N'hésitez pas à nous contacter si vous avez des questions ou si vous souhaitez discuter davantage de votre projet.\n\n"
        message += "Merci encore de votre confiance et de votre intérêt pour notre service.\n\n"
        message += "Cordialement,\nL'équipe de Mifuro"
        message = message.format(user.name)

        # ou message = "Salut " + user.name + "!\nVoici l'image générée pour vous."
        from_email = "mifuro.dc@gmail.com"
        to_email = user.email

        # Créer l'objet MIMEMultipart pour le mail
        msg = MIMEMultipart()
        msg["From"] = from_email
        msg["To"] = to_email
        msg["Subject"] = subject

        # Ajouter le corps du message
        msg.attach(MIMEText(message, "plain"))

        # Ajouter l'image générée en tant que pièce jointe
        part = MIMEBase("image", "png")  # Modifier le type MIME si nécessaire
        part.set_payload(image_generee)
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", "attachment", filename="mon_produit_de_reve.png")
        msg.attach(part)

        # Envoyer le mail en utilisant SMTP
        smtp_host = "smtp.gmail.com"
        smtp_port = 587
        smtp_username = "mifuro.dc@gmail.com"
        smtp_password = "ruhxqzyendunbdvl"

        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(from_email, to_email, msg.as_string())



#  Envoie du mail pour le formulaire contact
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            raison_sociale = form.cleaned_data['raison_sociale']
            numero = form.cleaned_data['numero']
            message = form.cleaned_data['message']

            subject = 'Nouveau message de contact'
            message = f"Nom: {nom}\nEmail: {email}\nRaison sociale: {raison_sociale}\nNuméro: {numero}\nMessage: {message}"
            from_email = email  # Utilisateur comme expéditeur
            to_email = 'mifuro.dc@gmail.com'  # Votre adresse e-mail

            # Créer l'objet MIMEMultipart pour le mail
            msg = MIMEMultipart()
            msg["From"] = from_email
            msg["To"] = to_email
            msg["Subject"] = subject

            # Ajouter le corps du message
            msg.attach(MIMEText(message, "plain"))

            # Envoyer le mail en utilisant SMTP
            smtp_host = "smtp.gmail.com"
            smtp_port = 587
            smtp_username = "mifuro.dc@gmail.com"
            smtp_password = "ruhxqzyendunbdvl"

            with smtplib.SMTP(smtp_host, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.sendmail(from_email, to_email, msg.as_string())

            # a faire quand ca réussi
            # return render(request, 'contact_success.html')
    else:
        form = ContactForm()

    context = {'contact_form': form}
    return render(request, 'contact.html', context)





def user_login(request):
    if request.method == 'POST':
        # Traitement des requêtes POST
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            # Faites ici les actions nécessaires après la connexion
            return redirect('compte')
        else:
            # Gérer l'authentification invalide
            # return HttpResponse("Authentification invalide")
            return render(request, 'login.html')
    else:
        # Gérer les requêtes GET
        return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('index')


# user cennected  ?
def my_view(request):
    if request.user.is_authenticated:
        # L'utilisateur est connecté, effectuez les actions nécessaires
        # ...
        return render(request, 'compte')
    else:
        # L'utilisateur n'est pas connecté, redirigez-le vers la page de connexion
        return redirect('login')

@login_required    
def compte(request):
    # Récupérer les informations du compte
    user = request.user
    # Passer les informations du compte au contexte
    context = {'user': user}
    return render(request, 'compte.html', context)


def technophiles(request):
    if request.method == 'POST':
        if 'questionnaire_form' in request.POST:
            questions = Question.objects.all()
            questionnaire_form = QuestionnaireForm(request.POST, questions=questions)
            if questionnaire_form.is_valid():
                for question in questions:
                    selected_reponse_id = questionnaire_form.cleaned_data.get(f'question_{question.id}')
                    selected_reponse = question.reponse_set.get(id=selected_reponse_id)
                    selected_reponse.est_selectionnee = True
                    selected_reponse.save()

                reponses_correctes = Reponse.objects.filter(
                    question__in=questions,
                    est_selectionnee=True,
                    est_correcte=True
                )
                score = len(reponses_correctes)

                technophile_form = TechnophileForm(request.POST)
                if technophile_form.is_valid():
                    technophile = technophile_form.save(commit=False)
                    username = technophile_form.cleaned_data.get('username')
                    password = technophile_form.cleaned_data.get('password1')
                    technophile.set_password(password)
                    technophile.save()
                    user = authenticate(request, username=username, password=password)
                    login(request, user)
                    return redirect('compte')

                context = {
                    'questionnaire_form': questionnaire_form,
                    'technophile_form': technophile_form,
                    'questions': questions,
                    'reponses_correctes': reponses_correctes,
                    'score': score
                }
                return render(request, 'technophiles.html', context)
        elif 'technophile_form' in request.POST:
            technophile_form = TechnophileForm(request.POST)
            if technophile_form.is_valid():
                user = technophile_form.save()  # Enregistrement de l'utilisateur Technophile
                login(request, user)  # Connexion de l'utilisateur
                return redirect('compte')
            else:
                # Gérer le cas où le formulaire n'est pas valide
                questions = Question.objects.all()
                questionnaire_form = QuestionnaireForm(questions=questions)
                context = {
                    'questionnaire_form': questionnaire_form,
                    'technophile_form': technophile_form,
                    'questions': questions,
                    'errors': technophile_form.errors
                }
                return render(request, 'technophiles.html', context)

    else:
        # Affichage initial de la page avec les formulaires
        questions = Question.objects.all()
        questionnaire_form = QuestionnaireForm(questions=questions)
        technophile_form = TechnophileForm()
        context = {
            'questionnaire_form': questionnaire_form,
            'technophile_form': technophile_form,
            'questions': questions,
            'errors': technophile_form.errors
        }
        return render(request, 'technophiles.html', context)

    return render(request, 'technophiles.html')




def creer_compte_technophile(request):
    if request.method == 'POST':
        technophile_form = TechnophileForm(request.POST)
        if technophile_form.is_valid():
            username = technophile_form.cleaned_data.get('username')
            password = technophile_form.cleaned_data.get('password1')
            email = technophile_form.cleaned_data.get('email')

            # Créer un nouvel utilisateur Django
            user = User.objects.create_user(username=username, password=password, email=email)

            # Créer une instance de Technophile et associer l'utilisateur
            technophile = Technophile(user=user, email=email, username=username)
            technophile.set_password(password)
            technophile.save()

            # Authentifier et connecter l'utilisateur
            user = authenticate(request, username=username, password=password)
            login(request, user)

            return redirect('compte')
        else:
            context = {
                'technophile_form': technophile_form,
                'errors': technophile_form.errors
            }
            return render(request, 'create_accountTechnophiles.html', context)
    else:
        technophile_form = TechnophileForm()
        context = {
            'technophile_form': technophile_form,
        }
        return render(request, 'create_accountTechnophiles.html', context)


def creer_compte_entrerpise(request):
    if request.method == 'POST':
        entreprise_form = EntrepriseForm(request.POST)
        if entreprise_form.is_valid():
            username = entreprise_form.cleaned_data.get('username')
            password = entreprise_form.cleaned_data.get('password1')
            email = entreprise_form.cleaned_data.get('email')
            numero = entreprise_form.cleaned_data.get('numero')
            raison_sociale = entreprise_form.cleaned_data.get('raison_sociale')

            # Créer un nouvel utilisateur Django
            user = User.objects.create_user(username=username, password=password, email=email)

            # Créer une instance de Entreprise et associer l'utilisateur
            entreprise = Entreprise(user=user, email=email, username=username, numero=numero,  raison_sociale=raison_sociale)
            entreprise.set_password(password)
            entreprise.save()

            # Authentifier et connecter l'utilisateur
            user = authenticate(request, username=username, password=password)
            login(request, user)

            return redirect('compte')
        else:
            context = {
                'entreprise_form': entreprise_form,
                'errors': entreprise_form.errors
            }
            return render(request, 'create_accountEntreprises.html', context)
    else:
        entreprise_form = EntrepriseForm()
        context = {
            'entreprise_form': entreprise_form,
        }
        return render(request, 'create_accountEntreprises.html', context)


def page_not_found(request, exception):
    return render(request, '404.html', status=404)