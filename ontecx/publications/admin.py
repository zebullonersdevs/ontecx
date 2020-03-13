from django.contrib import admin

# Register your models here.
from .models import Publication, PublicationCategory

admin.site.register(Publication)
admin.site.register(PublicationCategory)
