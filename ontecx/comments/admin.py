from django.contrib import admin

# Register your models here.
from .models import Comments, RepliedComment

admin.site.register(Comments)
admin.site.register(RepliedComment)
