from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from  django.db import  models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=150)
    avatar = models.URLField(default="https://images.unsplash.com/photo-1536137011311-182058a260ba?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2550&q=80", null=True, blank=True)
    username = CharField(_("username"), blank=True, max_length=150)
    email = models.EmailField(_("email"), unique=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [ "password", "username"]
