from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product
from .models import NewsletterSubscriber
from .models import Contact
from .models import Question
from .models import Reponse
from .models import Entreprise
from .models import Technophile
# Register your models here.

admin.site.register(Product)
admin.site.register(NewsletterSubscriber)
admin.site.register(Contact)
admin.site.register(Question)
admin.site.register(Reponse)
admin.site.register(Entreprise)
admin.site.register(Technophile)
